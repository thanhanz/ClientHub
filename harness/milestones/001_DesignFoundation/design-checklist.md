# 001 — Design checklist

Status: UNREVIEWED. Check an item only with exact document/section and review evidence. This checklist does not describe execution state.

## Product Requirement Coverage

- [ ] Approve or revise the proposed Product Goal and supply or formally supersede its missing handoff.
- [ ] Review concrete inputs and expected outcomes for all three selected scenarios.

## System Architecture

- [ ] Review backend/AI ownership, minimal persistence choice, and transaction boundaries.
- [ ] Confirm fake source and Jira adapters exercise normal application workflows without scenario-specific business logic.

## Database / ERD

- [ ] Review keys, cardinalities, uniqueness, and prevention of cross-project references.
- [ ] Review provenance, occurrence/persistence timestamps, historical changes, and retention behavior.
- [ ] Review separate business/review states and many-to-many event–ticket associations.

## Workflows

- [ ] Review extraction, mapping, and investigation happy paths and state transitions.
- [ ] Define reviewed-event eligibility, mapping rejection/remapping, and concurrent review behavior.

## Contracts and Interfaces

- [ ] Review normalized-source and read-only Jira interface boundaries and error behavior.
- [ ] Review backend–AI and evidence-bundle contracts, including versioning and reference validation.

## Security and Authorization

- [ ] Approve project roles, review permissions, identity handling, and Jira visibility rules.
- [ ] Define service credentials, safe logging, and treatment of untrusted source instructions.

## Failure Handling

- [ ] Define duplicate requests, timeouts, partial failures, retry ownership, and recovery.
- [ ] Define missing, stale, inaccessible, conflicting, and truncated evidence behavior.

## Testability

- [ ] Allocate all twelve acceptance cases to scenario fixtures and milestone gates.
- [ ] Separate runtime inputs from expected answers and deterministic checks from real AI evaluations.

## Cross-Document Consistency

- [ ] Verify lifecycle names and workflow ownership agree across product, architecture, ERD, and contracts.
- [ ] Verify every workflow has supporting data/interfaces and every entity has a business purpose.

## Design Readiness

- [ ] Resolve blocking findings and record explicit deferrals with their affected milestones.
- [ ] Record owner approval of this milestone goal, resolved design, and verification gates against their revision.

## Consolidated design-pack review gates

- [ ] Review each proposed technology decision separately from the approved MVP revision rules.
- [ ] Verify schema examples and negative contract checks with recorded commands/results.
- [ ] Confirm 003 runs without Python and 006 deterministic context is tested separately from real AI synthesis.
- [ ] Record mock-versus-real provider limitations; production sandbox integration is deferred.

## Review sign-off

- Review date:
- Reviewer:
- Approved document revision:
- Remaining findings and explicit conditions:
- Readiness decision:

The owner approved the specific revision rules recorded in docs/architecture/decisions.md. This does not complete every review item or verify a milestone.
