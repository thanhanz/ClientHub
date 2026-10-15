# 005 - Checklist

Current planning and evidence index. No new approvals or verified results are recorded. Existing checked document-review items retain their limited meaning; they are not runtime verification.

## Task index

Task decomposition awaits prerequisite acceptance and the decisions below. Split the listed feature deliverables with the [task template](../../task-template.md), one independently testable outcome per session. This checklist is not a dispatch queue.

## Decisions and readiness

- [ ] Approve deterministic candidate signals, explicit-ID treatment, and optional AI adjudication criteria.
- [ ] Define proposal/confirmation/rejection transitions and reviewer permissions.
- [ ] Verify uniqueness across all statuses, concurrent review checks, and unchanged rejected duplicates; reopening/remapping is deferred.
- [ ] Approve precision-focused mapping tests and AI evaluation criteria if adjudication is enabled.
- [ ] Record owner approval of this milestone goal, resolved design, and verification gates against their revision.

## Deliverables and acceptance

- [ ] Implement discovery of existing Jira issues even without prior event mappings.
- [ ] Implement deterministic matching and approved optional AI adjudication.
- [ ] Persist link type, origin, provenance, and authorized human review decisions.
- [ ] Test pre-existing QA issues, Google/Apple distinction, many-to-many/unmapped states, and review concurrency.
- [ ] Verify mapping confirmation cannot approve business commitments; test candidate-provider failures.
- [ ] Record required focused checks and applicable earlier regression gates with actual results.
- [ ] Present milestone evidence to the owner and stop before the next milestone.

### Approved MVP revision checks

- [ ] MEMBER reads only CONFIRMED mappings of accessible APPROVED events; PO_PM alone proposes/reviews.
- [ ] Duplicate proposals return the existing mapping unchanged even after rejection; review version and audit changes commit atomically.
- [ ] Verify many-to-many/unmapped cases and association confirmation never changes commitment status.

## Approval and milestone acceptance

- Approved specification commit, task scopes/checks, approver/date: pending.
- Milestone acceptance evidence and owner/date: pending.
- Runner verification evidence: none recorded.

The Runner owns verified completion links. Before it exists, an independent operator records bootstrap checks explicitly as operator verification; coding agents never mark VERIFIED.
