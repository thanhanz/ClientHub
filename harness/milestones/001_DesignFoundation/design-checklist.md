# 001 — Design checklist

Status: AGENT REVIEWED WITH OPEN FINDINGS — DF-001-R2 (2026-10-15). Check an item only with exact document/section and review evidence. This checklist does not describe execution state.

Review evidence: [DF-001-R2 findings and check results](review.md), [runtime scenario inputs](../../../docs/scenarios/fixture-inputs.md), and [AC-01–12 assertions and gate allocation](../../../docs/scenarios/expected-outcomes.md). Checked review items record the agent’s document review, including linked findings; they do not mean owner approval, resolved findings, or passing runtime tests. Unchecked items remain incomplete. DF-01–11 identify remaining decisions and blocking milestones.

## Product Requirement Coverage

- [ ] Approve or revise the proposed Product Goal and supply or formally supersede its missing handoff.
- [x] Review concrete inputs and expected outcomes for all three selected scenarios. — Review evidence: fixture-inputs.md §§G/S/D; expected-outcomes.md §Semantic expectations; DF-10 rubric remains pending.

## System Architecture

- [x] Review backend/AI ownership, minimal persistence choice, and transaction boundaries. — Review evidence: system-design.md §§1–4; erd.md §3; decisions.md ADR-001–005; DF-02/05/06 remain open.
- [ ] Confirm fake source and Jira adapters exercise normal application workflows without scenario-specific business logic.

## Database / ERD

- [x] Review keys, cardinalities, uniqueness, and prevention of cross-project references. — Review evidence: erd.md §§2–3/5; domain-contracts.md §§1/3/6; DF-05 exact DB enforcement remains open.
- [x] Review provenance, occurrence/persistence timestamps, historical changes, and retention behavior. — Review evidence: erd.md §§3/5; domain-contracts.md §§4–6; DF-03/05/06 remain open.
- [x] Review separate business/review states and many-to-many event–ticket associations. — Review evidence: domain-contracts.md §§2–3; erd.md §§1–4; expected-outcomes.md REVIEW.

## Workflows

- [x] Review extraction, mapping, and investigation happy paths and state transitions. — Review evidence: workflows.md WF-01–03; domain-contracts.md §3; DF-07/08/09 remain open.
- [x] Define reviewed-event eligibility, mapping rejection/remapping, and concurrent review behavior. — Review evidence: domain-contracts.md §§3–4/6; api-contracts.md §§1/3–4; terminal review, deferred reopening, expected-version 409.

## Contracts and Interfaces

- [x] Review normalized-source and read-only Jira interface boundaries and error behavior. — Review evidence: provider-contracts.md §§1–5; DF-03/04 envelopes and precision remain open.
- [x] Review backend–AI and evidence-bundle contracts, including versioning and reference validation. — Review evidence: ai-contracts.md §§1–5; domain-contracts.md §§4/7; contracts/README.md §Ownership and compatibility; DF-08/09/11 remain open.

## Security and Authorization

- [ ] Approve project roles, review permissions, identity handling, and Jira visibility rules.
- [ ] Define service credentials, safe logging, and treatment of untrusted source instructions.

## Failure Handling

- [ ] Define duplicate requests, timeouts, partial failures, retry ownership, and recovery.
- [ ] Define missing, stale, inaccessible, conflicting, and truncated evidence behavior.

## Testability

- [x] Allocate all twelve acceptance cases to scenario fixtures and milestone gates. — Review evidence: expected-outcomes.md §All twelve acceptance cases; traceability.md acceptance table; SC-AC01–12.
- [x] Separate runtime inputs from expected answers and deterministic checks from real AI evaluations. — Review evidence: fixture-inputs.md introductory boundary; expected-outcomes.md §Evaluation protocol to approve.

## Cross-Document Consistency

- [x] Verify lifecycle names and workflow ownership agree across product, architecture, ERD, and contracts. — Review evidence: product/goal.md §§5–8; system-design.md §§1/3/9; workflows.md WF-01–03; erd.md §4; domain-contracts.md §§2–4; initial manual event review decision remains DF-09.
- [ ] Verify every workflow has supporting data/interfaces and every entity has a business purpose.

## Design Readiness

- [ ] Resolve blocking findings and record explicit deferrals with their affected milestones.
- [ ] Record owner approval of this milestone goal, resolved design, and verification gates against their revision.

## Consolidated design-pack review gates

- [x] Review each proposed technology decision separately from the approved MVP revision rules. — Review evidence: decisions.md ADR-004–011 versus Owner-approved MVP revision; DF-02 approval remains pending.
- [ ] Verify schema examples and negative contract checks with recorded commands/results.
- [ ] Confirm 003 runs without Python and 006 deterministic context is tested separately from real AI synthesis.
- [x] Record mock-versus-real provider limitations; production sandbox integration is deferred. — Review evidence: provider-contracts.md §Real integration migration gate; scenarios/README.md §Adapter boundary; mocks do not establish real provider/model quality.

## Review sign-off

- Review date: 2026-10-15 (agent document review)
- Reviewer: Codex (document reviewer; not owner approver)
- Approved document revision: pending owner approval; reviewed candidate DF-001-R2
- Remaining findings and explicit conditions: DF-01–11 in review.md; failed contract validation; no implementation/provider/AI test evidence.
- Readiness decision: deliverable for owner review; not ready for milestone approval or implementation authorization.

The owner approved the specific revision rules recorded in docs/architecture/decisions.md. This does not complete every review item or verify a milestone.
