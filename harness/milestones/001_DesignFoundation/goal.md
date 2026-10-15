# 001 — Design and scenario baseline

Status: DRAFT — pending milestone review; not execution authorization.

## Goal

Prepare the minimum reviewable architecture and three scenario specifications before business-feature implementation.

## Dependencies and requirements

- Dependency: None; documentation setup is explicitly authorized.
- Coverage: FR-01–07; AC-01–12 design coverage.
- Authority: [Product Goal](../../../docs/product/goal.md), [roadmap](../../README.md), and [execution policy](../../policies/execution.md).

## Review and exit gate

Review the [checklist](checklist.md), resolve relevant decisions, and approve exact task scopes/checks at a Git revision before dispatch. Tasks may be prepared while BLOCKED; file existence is not authorization. A build alone does not establish completion.

Stop at this milestone boundary for owner review. 001/002 bootstrap uses explicitly assigned setup work until independent Runner verification exists.

Current review candidate: [remaining findings](#open-findings) and [historical check results](checklist.md#historical-verification-evidence); [scenario inputs](../../../docs/scenarios/fixture-inputs.md) and [separate expected outcomes](../../../docs/scenarios/expected-outcomes.md). Candidate delivery is not owner approval or Runner verification.

## Exclusions

No application features, migrations, live connectors, or Runner implementation.

## Session and context rules

One task is one fresh session and one cohesive, independently testable outcome. Follow [execution policy](../../policies/execution.md#session-context-and-task-sizing). Starting context target: 10,000-30,000 tokens; ceiling: strictly below 100,000 tokens including supplied instructions, task, selected references and dependency handoffs. This is not a guaranteed total-session token cap. Split oversized work before dispatch. Update these canonical files directly; Git retains history.

## Open findings

These are findings/proposals, not contract amendments. Approving scenarios alone does not resolve them. Each decision needs a recorded choice and updated canonical contract before dependent executable tasks.

| ID | Evidence / gap | Proposed resolution for review | Blocks / deferral |
| --- | --- | --- | --- |
| DF-01 | Product Goal remains proposed and references an unavailable architecture handoff | Approve the current Product Goal explicitly and formally supersede the missing handoff, or supply it and reconcile differences | 001 sign-off; all dependent milestone approvals |
| DF-02 | ADR-004–011 and technology baseline remain proposed, despite approved semantic revision rules | Approve/revise each separately: .NET modular monolith, PostgreSQL/EF, mock Jira port, code-controlled orchestration, synchronous demo operations, guarded test identity, deterministic search, Compose | Persistence/auth/provider choices before 003; no silent framework adoption |
| DF-03 | Source schema permits but does not require occurred_at_precision; provider required fields and source ERD omit it, so date-only precision can be lost before extraction | Require/preserve source occurrence precision in normalized input and persistence, including DATE UTC normalization; explicitly define UNKNOWN occurrence handling before freezing v1 | 003 source contract freeze and 004 extraction; D-03 exposes this gap |
| DF-04 | Provider contracts describe freshness, partial results and errors, but return signatures do not define complete page/coverage/error envelopes; duplicate §6 headings are ambiguous | Define DTOs, cursor/snapshot semantics, field availability and timeout/error envelopes; distinguish not-found from denied and absent fields from empty collections; renumber sections when canonical contract edits are authorized | 003 provider contract freeze; 006 partial-context policy |
| DF-05 | ERD calls for same-project constraints “where feasible” and nonempty provenance; exact relational enforcement and retention cleanup are not fixed | Specify composite keys/FKs and transaction checks; reject approved-event edits initially; define cleanup of derived summaries and stored investigations when evidence access/content changes | 003 DB design, 004 provenance/history, 006 persisted result access; organization retention durations may remain deferred to real integration |
| DF-06 | Investigation snapshots/results and audit are described, but persistence entity, retained payload, access revalidation and failure transaction boundaries are incomplete | Approve minimal result/audit persistence schema, permitted retention, request/result association, and revalidation on later reads; never retain forbidden evidence via audit | 006; not needed to implement 003 source intake |
| DF-07 | Backend budgets are proposed; traversal relevance/ranking, retries and partial-vs-error behavior are not exact | Approve demo defaults 2/10/12; count every provider attempt/page; use visited locators; approve deterministic ranking and stable pagination; choose no automatic demo retries or an explicit bounded policy and safe partial-result rules | 005 candidate discovery; 006 bounded retrieval; V-BOUNDS intentionally does not dictate a call sequence |
| DF-08 | Freshness timestamps exist, but stale thresholds/conflict handling and semantic claim rejection/repair authority remain unspecified | Attribute historical Jira observations without labeling them current; disclose discrepancies; define thresholds and reject unsupported high-risk FACT claims rather than publish; decide validation failure response without unbounded AI repair | 006, real synthesis evaluation |
| DF-09 | API inventory lacks an exact synthesis endpoint request/response entry and event manual-review policy is less strict than the extraction default | Complete synthesis route contract and request schemas; explicitly choose whether manual creation can atomically approve with authorized audit or must always enter PENDING_REVIEW | 004 manual event creation; 006 synthesis |
| DF-10 | No quantitative real-AI gate or frozen annotation rubric; scenario statements can support multiple atomic representations | Approve allowed enum/annotation alternatives, model/configuration, repetitions, dataset, precision/support thresholds and failure criteria; require no critical isolation/false-commitment cases in this selected suite | 004/005/006 AI gates; these three synthetic demos alone do not establish production quality |
| DF-11 | Service authentication, token/time limits and safe prompt diagnostics are still TBD | Specify private backend-to-Python credentials, cancellation/timeout/token budgets and logging policy before inference; production identity, real Jira credentials/visibility and connectors require later sandbox decisions | 004 inference security; production provisioning/connector details deferred to real integration |

Existing decisions already resolve PO_PM vs MEMBER permissions, nonempty event provenance, immutable duplicate imports, unique mappings across all states, terminal mapping review, and approved-event/confirmed-association synthesis eligibility. Do not reopen these as blank design questions. API §4 already chooses non-disclosing 404 for inaccessible projects and 403 for forbidden operations in accessible projects; workflows should refer to it rather than offer an independent policy choice.
