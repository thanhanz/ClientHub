# Backend API Contracts — ASP.NET Core

> Status: REVIEW CANDIDATE · API version prefix `/api/v1`. Routes describe expected behavior; they are **not implemented yet**. Versioning/schema changes require review.

## 1. Common HTTP conventions

- HTTPS in real deployments. JSON request/response bodies, snake_case JSON field names, UTC ISO-8601 `Z` timestamps and opaque UUID strings.
- Authentication: server-verified principal (JWT/OIDC TBD), guarded Test/Development fixture identity for mock phase only. Never treat a caller-supplied `X-User-Id`, `role`, or `project_id` as sufficient authorization.
- Every route scoped by `projects/{project_id}` verifies membership/role and finer source visibility. Deny before reading protected data.
- Standard errors use `application/problem+json` with `type`, `title`, `status`, `detail` (safe), `instance`, `trace_id`, optionally `errors`. Do not leak whether inaccessible resources exist.
- Pagination: `limit` bounded server-side; opaque `cursor` in responses; order stable and deterministic.
- Mutations accept `Idempotency-Key` where relevant; review transitions require `expected_version` optimistic concurrency. `409` on stale version.
- API responses include `schema_version: "1.0"` for top-level contract objects. See `schemas/`.

## 2. M1 endpoints (Backend Foundation)

| Method | Route | Authorization | Request / response | Errors |
| --- | --- | --- | --- | --- |
| `GET` | `/health/live` | none | liveness text/status only | `503` when not alive |
| `GET` | `/health/ready` | deployment policy | DB/provider readiness status | `503` when not ready |
| `GET` | `/api/v1/projects/{project_id}/sources` | project member + source ACL | query `limit,cursor`; page of source metadata/approved notes the caller may access | `401,403,404` |
| `POST` | `/api/v1/projects/{project_id}/sources` | permitted source creator | normalized permitted source; returns source ID and deduplication flag (`201` new / `200` duplicate) | `400,403,409,422` |
| `GET` | `/api/v1/projects/{project_id}/events` | permitted project/source read | `limit,cursor,review_status`; page sorted `occurred_at`, stable ID | `403,404` |
| `POST` | `/api/v1/projects/{project_id}/events` | permitted creator | structured event + source IDs; returns new event `201` | `400,403,404,422` |
| `POST` | `/api/v1/projects/{project_id}/events/{event_id}/review` | PO/PM reviewer | `{decision: APPROVE\|REJECT, expected_version}`; audited review | `403,404,409` |
| `GET` | `/api/v1/projects/{project_id}/mappings` | project member + evidence ACL | filtered mappings with review status and source refs | `403,404` |
| `POST` | `/api/v1/projects/{project_id}/mappings` | permitted proposer | event ID + composite Jira issue identity + relationship type + origin, status set server-side `PROPOSED`; returns link `201` | `403,404,409,422` |
| `POST` | `/api/v1/projects/{project_id}/mappings/{mapping_id}/review` | PO/PM reviewer | `{decision: CONFIRM\|REJECT, expected_version}`; audited `CONFIRMED`/`REJECTED` | `403,404,409` |
| `POST` | `/api/v1/projects/{project_id}/investigations/context` | permitted investigator | query/question, optional issue key, bounded retrieval policy override only if within server policy; returns evidence bundle | `400,403,404,422,503` |

`POST /investigations/context` deliberately returns **deterministic retrieval context**, not an LLM-generated final answer. A `/investigations` synthesis endpoint is a later milestone.

### Example — mapping propose

```json
{
  "event_id": "11111111-1111-4111-8111-111111111111",
  "jira_instance_key": "mock-jira",
  "jira_issue_key": "AUTH-101",
  "relationship_type": "ADDRESSES_REPORTED_ISSUE",
  "origin": "MANUAL"
}
```

Server assigns mapping ID, `PROPOSED` status, `version=1`, creator from principal and creation timestamp. `AI_INFERRED` origin may only be created by the trusted backend AI pipeline in M3; do not trust arbitrary clients claiming AI origin.

### Example — mapping review

```json
{
  "decision": "CONFIRM",
  "expected_version": 1
}
```

Allowed: `PROPOSED -> CONFIRMED` and `PROPOSED -> REJECTED`; with reviewer/time/version/audit in one transaction. A mapping confirmation **does not change** `events.business_status` or approve any deadline/scope.

### Example — deterministic context request

```json
{
  "question": "Why is Google Login blocked?",
  "jira_instance_key": "mock-jira",
  "issue_key": "AUTH-101"
}
```

Backend derives authorized project ID from URL and principal; it does not accept a `user_id` from the request. Returned `ContextBundle` must conform to `schemas/context-bundle.schema.json` and cannot contain evidence that the requester is not allowed to view.

## 3. API rules by use case

**Sources:** source reference metadata is persisted with normalized verified actor role. When `retention_mode=METADATA_ONLY`, do not accept raw body retention. `visibility_class` (`PROJECT_MEMBERS` or `PO_PM_ONLY`) limits both source and derived event disclosure. Under `APPROVED_NOTES` only `approved_notes` is retained; under `PERMITTED_CONTENT` only policy-permitted `permitted_text` is retained. When meeting approved notes exist, the source is a meeting-level reference, not a verbatim transcript. Identical provider composite ID within a project must be idempotent.

**Events:** `occurred_at` and `created_at` differ. Event may be unmapped. `source_refs` cannot refer across projects. Event is `PENDING_REVIEW` unless backend explicitly records an authorized/manual reviewed decision. Incoming event type/status are checked for coherence, not accepted blindly.

**Mappings:** validate normalized Jira locator via the allowed provider; a link is between event and Jira issue, **not Jira-to-Jira**. Reject duplicates or return existing link according to idempotency contract. Store mapping origin and review evidence.

**Investigation context:** build from authorized events and explicit Jira links. Do not infer causal relationships or generate final claims in M1. Return `truncated`, `warnings`, policy usage, observed times and evidence registry for auditing/verifier use.

## 4. Authorization and errors

| Condition | Response |
| --- | --- |
| No authenticated principal | `401 Unauthorized` |
| Project membership absent or role forbidden | `404 Not Found` if project itself is inaccessible; `403 Forbidden` if project is accessible but actor lacks operation permission |
| Linked source belongs to different project | `422` for an invalid cross-project association after access checks, without exposing the other project |
| Missing permitted entity | `404 Not Found` |
| Invalid payload/enum | `400 Bad Request` for malformed JSON/schema; `422 Unprocessable Entity` for structurally valid but invalid business inputs |
| State transition/version conflict | `409 Conflict` |
| Jira provider unavailable without safe partial output | `503 Service Unavailable` with retry-safe metadata |
| Policy stops a partial retrieval | Successful bundle with explicit `truncated=true` and warning, not false completeness |

## 5. API contract acceptance tests

`API-01` cross-project data denied, `API-02` source-level hidden evidence omitted, `API-03` duplicate ingestion idempotent, `API-04` event chronology by occurred time, `API-05` mapping creation proposed, `API-06` authorized confirmation audited, `API-07` confirmation does not change commitment state, `API-08` concurrent version mismatch 409, `API-09` context refuses invented Jira links, `API-10` investigation budget honored, `API-11` source reference registry valid, `API-12` context endpoint works with mock Jira and no Python.
