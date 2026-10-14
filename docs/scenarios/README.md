# MVP scenario baseline

Status: selected narratives; concrete fixture content awaits 001 review. Authority: [Product Goal §9](../product/goal.md) and owner selection on 2026-10-14.

## Runtime inputs and expected outcomes

| Scenario | Fixture inputs to prepare | Expected behavior to assert separately |
|---|---|---|
| Google Login | Client report; earlier QA-created Google Login issue; explicit blocker; parallel Apple Login issue sharing an assignee | Discover the earlier issue, avoid false Apple mapping, use explicit blockers, and do not infer delay causation from shared assignment |
| Sales Export deadline | Client-requested date; PO deferral; separate explicit commitment example; internal Jira due date | Preserve requested versus committed versus Jira-recorded dates; deferral stays REQUESTED_NOT_COMMITTED |
| Discount scope change | Initial first-order discount agreement and delivered ticket; later returning-customer request | Preserve historical agreement and new request; Done does not approve expanded scope |

001 must define source text, synthetic actors and dates, stable IDs, project membership, Jira records, and expected assertions. Include approved meeting notes yielding multiple events, late-arriving records, unmapped records, unavailable evidence, and a second unauthorized project as targeted acceptance variants. No real customer data is needed.

## Adapter boundary

The backend owns two narrow interfaces: normalized source ingestion and read-only Jira retrieval. Exact types and signatures require 001 contract review. Source inputs preserve identity, project, content, source type, available actor/time metadata, and permitted provenance. Jira supports candidate search, details/history, explicit links, and freshness/partial-result metadata required by the workflows.

Fixture adapters provide data through the same application boundaries intended for future real providers. Authorization, persistence, review, validation, and budgets remain backend behavior. Do not branch business rules on scenario names or seed expected extraction/mapping results as a substitute for exercising those workflows.

Expected events, mappings, and findings belong in test/evaluation assets, separate from runtime fixtures and AI context. Reusable adapter contract tests must cover both fixture and future real implementations. Provider authentication, polling, webhooks, and production connectors are deferred.

Deterministic AI doubles are allowed for backend tests. Real extraction and synthesis must have separate repeatable evaluations before their milestones pass; a fake provider passing a test is not evidence of model quality.
