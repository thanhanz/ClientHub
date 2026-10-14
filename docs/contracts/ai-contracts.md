# AI Inference Contracts — Python service (future milestone)

> Status: REVIEW CANDIDATE. **Not required for Backend Foundation M1.** Defined now to protect the later backend/AI boundary. Python has no direct database, Jira, email, chat or meeting-provider credentials.

## 1. General transport and trust

- Private HTTP API called only by the ASP.NET backend using service authentication (mechanism TBD) and request correlation ID.
- Backend authorizes project/source access and computes any retrieval budgets **before** sending payload.
- Python validates structural input, calls model, validates structured result against schema, returns JSON; **does not persist authoritative business entities**.
- Backend revalidates the returned content, evidence refs, ownership, business rules and human review requirements.
- AI outputs are **proposals**, never authority to mutate Jira, review a mapping, commit a deadline or change project permissions.
- `schema_version="1.0"` and `request_id` echoed on all inference responses. Timeouts, cancellation and token limits are backend-controlled; model configuration is not user-controlled.
- Do not log raw transcripts/prompts indiscriminately; retain only permitted metadata and redacted diagnostics.

## 2. Proposed inference endpoints

| Method | Endpoint | Input | Output |
| --- | --- | --- | --- |
| `POST` | `/v1/extract-events` | Permitted `NormalizedSource` + verified actor metadata + project context, no DB key required | `ExtractionOutput`, zero-to-many proposed atomic events |
| `POST` | `/v1/suggest-mappings` | Reviewed event, bounded authorized Jira candidates and explicit available refs | `MappingSuggestionsOutput`, unapproved suggested links |
| `POST` | `/v1/synthesize-investigation` | Authorized `ContextBundle` | `InvestigationResult`, factual/hypothetical/unknown findings with provided refs |

Backend can choose to avoid `/suggest-mappings` when deterministic explicit-ID matching is sufficiently clear. AI may not perform unbounded iterative Jira discovery.

## 3. Extraction contract

Input must contain `request_id`, `schema_version`, `project_id`, normalized source with source `ref_id`, verified speaker/sender `actor_kind`, permitted text/approved notes and retention level. For transient transcript processing, the transport must enforce a no-retention policy; absent compliant processing, use approved notes only.

Output schema: `schemas/extraction-output.schema.json`.

Each proposed event includes `event_type`, `business_status`, `summary`, `occurred_at`, `source_refs`, `review_required`. Backend verifies source refs and trustable actor attribution. Example: a client-requested due date and PO deferral must produce `REQUESTED_NOT_COMMITTED`; not a fictitious PO promise. Model-provided summary is not automatically an approved business fact.

## 4. Mapping contract

Input contains reviewed event + bounded list of candidate Jira DTOs/refs. Output schema: `schemas/mapping-suggestions.schema.json`.

Each suggestion has candidate Jira locator, relationship type, rationale, evidence refs and non-authoritative confidence between 0 and 1. Backend checks candidate membership, duplicates, permitted project and supporting refs, then creates mapping `PROPOSED` only. Reviewer is a PO/PM, not the AI service.

## 5. Investigation synthesis contract

Input schema: `schemas/context-bundle.schema.json`. Output schema: `schemas/investigation-result.schema.json`.

Output findings use `FACT | HYPOTHESIS | UNKNOWN` and `evidence_refs` from input registry, never fabricated IDs. Significant `FACT` findings need appropriately typed refs: an explicit Jira blocker relationship needs a `jira-link` ref; same-assignee context is not evidence of causation. When sources are incomplete, include meaningful `unknowns` and `warnings` instead of false closure.

A deterministic backend validator MUST:

1. Reject schema-invalid JSON or mismatched request IDs/schema versions.
2. Reject evidence refs absent from the original authorized backend evidence registry.
3. Reject refs to stale, inaccessible or project-mismatched items when freshness/access invalidates claim.
4. Check claims against attributable source fields / issue-link relation types. Since structural checks cannot prove all semantics, high-risk causation/commitment assertions need additional semantic evaluator or human review.
5. Never silently upgrade proposed mappings to confirmed or requested deadlines to commitments.

## 6. Error and retries

- `400/422` invalid input; `401/403` invalid internal caller; `429` model/provider rate budget; `503` temporary dependency outage; `504` timeout.
- Backend retries only idempotent inference operations under bounded policy; outputs have `request_id`, no side-effect approval.
- If inference fails, the backend retains original business state and reports an incomplete result; no fabricated fallback answer.
- Backend may use deterministic fixtures/stubs for AI responses in M1 integration testing.

## 7. Evaluation gates

Use synthetic ground truth to test extraction precision/recall, requested-vs-committed deadline accuracy, mapping precision over wrong-feature distractors, ref validity and supported FACT rate. The Google Login, Sales Export and Discount scope scenarios must all be represented. A schema-valid result is not automatically a semantically correct result.
