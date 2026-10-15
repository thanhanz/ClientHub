# 004 - Checklist

Current planning and evidence index. No new approvals or verified results are recorded. Existing checked document-review items retain their limited meaning; they are not runtime verification.

## Task index

Task decomposition awaits prerequisite acceptance and the decisions below. Split the listed feature deliverables with the [task template](../../task-template.md), one independently testable outcome per session. This checklist is not a dispatch queue.

## Decisions and readiness

- [ ] Approve model/provider choice, service authentication, schema/versioning, and timeout/error contracts.
- [ ] Define event business/review transitions, review permissions, concurrency, and extraction retry semantics.
- [ ] Define source reference validation and occurrence-time timeline tie-breakers.
- [ ] Approve repeatable extraction evaluation cases and pass criteria.
- [ ] Record owner approval of this milestone goal, resolved design, and verification gates against their revision.

## Deliverables and acceptance

- [ ] Implement stateless Python extraction receiving only backend-authorized context.
- [ ] Validate and persist events with source provenance and separate review/business state.
- [ ] Implement authorized review and occurrence-ordered timeline preserving history.
- [ ] Test multiple events, requested versus committed dates, late arrivals, and absent transcript details.
- [ ] Test invalid AI payloads/references, denied review, duplicate retries, and service failure; run real extraction evaluations.
- [ ] Record required focused checks and applicable earlier regression gates with actual results.
- [ ] Present milestone evidence to the owner and stop before the next milestone.

### Approved MVP revision checks

- [ ] Require at least one source per persisted event; commit event/provenance atomically and deny cross-project links.
- [ ] Hide events when any supporting source is inaccessible; MEMBER sees APPROVED events only.
- [ ] Round-trip requested/committed deadlines and occurrence precision; manual and extracted events cannot bypass authorized review.

## Approval and milestone acceptance

- Approved specification commit, task scopes/checks, approver/date: pending.
- Milestone acceptance evidence and owner/date: pending.
- Runner verification evidence: none recorded.

The Runner owns verified completion links. Before it exists, an independent operator records bootstrap checks explicitly as operator verification; coding agents never mark VERIFIED.
