# Domain Contracts — ClientHub

> Status: REVIEW CANDIDATE. Backend domain invariants and DTO semantics. `docs/product/goal.md` overrides any proposed behavior here.

## 1. Identifiers and isolation

- `project_id`: opaque internal UUID string; all Hub-owned objects belong to **exactly one** project.
- `actor_id`: verified principal ID (string), not caller-provided display name; may appear only where allowed by source policy.
- `source_id`, `event_id`, `mapping_id`: opaque Hub UUID strings. Examples such as `EVT-001` are synthetic aliases only; actual wire IDs should conform to UUID format where schema requires them.
- Jira external identity: composite `{jira_instance_key, jira_issue_key}`. An issue key is NOT guaranteed globally unique across Jira installations.
- Provider source identity: `{project_id, source_type, provider_instance_key, external_source_id}` is required for demo intake. Fixture authors supply a stable external ID, including for approved notes. Re-import returns the stored source without updating content or metadata. Changed fixture content needs a new external ID or an explicit demo reset. Intake without an external ID and general idempotency-key storage are deferred.
- A mapping, source link or Jira traversal may not cross unauthorized project/source boundaries.

## 2. Enumerations (canonical spelling)

```text
SourceType: EMAIL | CHAT | MEETING
RetentionMode: METADATA_ONLY | APPROVED_NOTES | PERMITTED_CONTENT
SourceVisibilityClass: PROJECT_MEMBERS | PO_PM_ONLY
ProjectRole: PO_PM | MEMBER
ActorKind: CLIENT | INTERNAL | UNKNOWN
EventType: BUG_REPORTED | FEATURE_REQUESTED | SCOPE_CHANGE_REQUESTED |
           DEADLINE_REQUESTED | COMMITMENT_MADE | PROPOSAL_MADE |
           PROPOSAL_REJECTED | ESTIMATE_PENDING | OTHER
BusinessStatus: REPORTED | REQUESTED_NOT_COMMITTED | PROPOSED |
                PENDING_ESTIMATE | COMMITTED | REJECTED | OUT_OF_SCOPE | UNKNOWN
EventReviewStatus: PENDING_REVIEW | APPROVED | REJECTED
MappingVerificationStatus: PROPOSED | CONFIRMED | REJECTED
MappingOrigin: AI_INFERRED | MANUAL | EXPLICIT_REFERENCE | TICKET_CREATED_FROM_EVENT
MappingRelationshipType: ADDRESSES_REPORTED_ISSUE | IMPLEMENTS_REQUEST |
                         HAS_REQUESTED_DEADLINE_FOR | COMMITMENT_COVERS_WORK |
                         RELATED_TO
FindingType: FACT | HYPOTHESIS | UNKNOWN
```

These values are *designed* initial enums, not exhaustive business ontologies. New values require contract/version review, not agent improvisation. Prefer explicit UNKNOWN over a false inference.

## 3. Review lifecycles

**Event review:** `PENDING_REVIEW -> APPROVED` or `PENDING_REVIEW -> REJECTED`. Review metadata and project authorization are required. Editing an approved event requires a new revision/audited action; 004 may reject edits rather than implementing amendment.

**Mapping review:** `PROPOSED -> CONFIRMED` or `PROPOSED -> REJECTED`. A terminal status is not silently reopened. A rejected suggestion does not become confirmed as a side effect of a new AI recommendation. Every review change includes actor, time, optimistic version and audit entry.

**Business state:** NOT a review workflow. `REQUESTED_NOT_COMMITTED` remains so until **new explicit commitment evidence** and an authorized business decision support a separate `COMMITMENT_MADE` event/status. A mapping confirmation cannot update it.

All new associations start `PROPOSED`, with origin and actor recorded. Keep one mapping per `(event_id, jira_instance_key, jira_issue_key, relationship_type)` across every status. A repeated proposal returns the existing mapping without changing origin, status, version, or review metadata. Rejected mappings remain rejected; reopening/remapping is deferred. Review updates and their audit entry commit in one transaction.

## 4. Evidence reference contract

Evidence registry entries are assigned by the backend, stable **within a bundle**; persistent entities remain identifiable across bundles. Allowed ref forms:

```text
source:{source_uuid}
event:{event_uuid}
jira:{jira_instance_key}:{issue_key}
jira-link:{jira_instance_key}:{from_key}:{relationship}:{to_key}
jira-excerpt:{jira_instance_key}:{issue_key}:{DESCRIPTION|HISTORY|COMMENT}:{item_id}
```

Values cannot contain arbitrary user-controlled path syntax, colon or whitespace in identifier components; the backend encodes/sanitizes provider identifiers. A Jira blocker claim needs an **explicit issue-link ref** with matching direction/relation. Merely listing two Jira issue refs is not adequate proof of blockage.

`evidence_level` differentiates approved notes, message-level and meeting-level references. An event based only on meeting metadata may support *that an approved summary exists*, **not an exact quote or minute-level speaker attribution**. Only `APPROVED` events may enter investigation synthesis. Pending/rejected events remain available to authorized PO/PM reviewers but are excluded from the bundle. Proposed mappings may assist backend candidate discovery only; only confirmed associations enter the synthesis bundle.

## 5. Time/freshness conventions

- Persist UTC instants with timezone-aware types and expose ISO-8601 `Z` timestamps.
- `occurred_at`: the source/event business occurrence, **not the Hub ingestion time**.
- `created_at`: Hub entity creation; `ingested_at`: source ingestion; `observed_at`: time Jira adapter observed ticket/links.
- If the source gives only a date or uncertain time, represent precision explicitly (e.g. `occurred_at_precision=DATE` and a documented normalized UTC instant) rather than inventing minute-level evidence. `UNKNOWN` is acceptable for uncertain origin.
- Timeline primary ordering: `occurred_at ASC`, then stable ID tie-breaker. Provide timezone transformation only at presentation layer.
- Snapshot freshness must be shown if important; stale data never silently becomes current fact.

## 6. Data access policies

| Operation | PO_PM | MEMBER |
| --- | --- | --- |
| Read accessible sources | Yes | Yes |
| Read events | All review states, subject to source access | APPROVED only, subject to source access |
| Read mappings | All review states, subject to source access | CONFIRMED only, for an accessible APPROVED event |
| Ingest sources; create/review events; propose/review mappings | Yes | No |
| Request context or AI investigation | Yes | No |

An event must have at least one source, including manually created events. Creation writes the event and source links atomically. A caller must be authorized for **every** supporting source to read an event or its mappings. If any source is inaccessible, omit the entire derived event/mapping and exclude it from AI context; do not partially redact it. Project membership alone cannot override this rule.
- Unauthorized users receive no source content, ticket context, or evidence reference for that project. Sensitive source ACLs can be stricter than project membership.
- Test identity may be injected only in guarded Test/Development; in Production all `actor_id` and roles derive from validated authentication.
- `PO_PM_ONLY` sources and derived event facts are not returned to ordinary project members; a context bundle includes only refs the caller may access. With `METADATA_ONLY`, do not store source bodies. `APPROVED_NOTES` permits only approved notes; `PERMITTED_CONTENT` permits text specifically allowed by source policy. Source retention applies to content, copies, logs and AI payload capture. An audit log must not become an unregulated transcript archive.

## 7. Backend deterministic validation

Validate required fields, enum values, timestamp parsing, project ownership, source provenance, review transitions, version concurrency, Jira external keys, retrieval limits, bundle ref existence/accessibility, and mapping-origin rules. LLM schema success alone does **not** establish semantic validity or a causal explanation. Unsupported FACT claims must be rejected or downgraded via controlled validation/human review, never silently published as facts.
