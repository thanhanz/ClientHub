# 003 - Checklist

Current planning and evidence index. No new approvals or verified results are recorded. Existing checked document-review items retain their limited meaning; they are not runtime verification.

## Task index

| Task | Readiness | Prerequisite | Verified commit/evidence |
| --- | --- | --- | --- |
| [003-P01](tasks/01-contracts.md) | BLOCKED | Entry gates and task-specific gaps/dependencies | None |
| [003-P02](tasks/02-persistence.md) | BLOCKED | Entry gates and task-specific gaps/dependencies | None |
| [003-P03](tasks/03-authorization.md) | BLOCKED | Entry gates and task-specific gaps/dependencies | None |
| [003-P04](tasks/04-ingestion.md) | BLOCKED | Entry gates and task-specific gaps/dependencies | None |
| [003-P05](tasks/05-source-fixtures.md) | BLOCKED | Entry gates and task-specific gaps/dependencies | None |
| [003-P06](tasks/06-source-api.md) | BLOCKED | Entry gates and task-specific gaps/dependencies | None |
| [003-P07](tasks/07-jira-adapter.md) | BLOCKED | Entry gates and task-specific gaps/dependencies | None |
| [003-P08](tasks/08-demo-smoke.md) | BLOCKED | Entry gates and task-specific gaps/dependencies | None |

## Decisions and readiness

- [ ] Approve database choice, minimal schema, project membership/identity model, and API authorization rules.
- [ ] Verify required fixture external IDs and return-existing duplicate behavior against the approved contract; ID-less intake and general idempotency-key storage are deferred.
- [ ] Approve source and Jira adapter contracts including inaccessible/missing/partial responses.
- [ ] Approve fixture configuration and keep expected answers outside runtime data.
- [ ] Record owner approval of this milestone goal, resolved design, and verification gates against their revision.

## Deliverables and acceptance

- [ ] Implement persistence, project membership checks, and normalized source ingestion behind an interface.
- [ ] Implement scenario source provider and read-only fake Jira provider through dependency injection.
- [ ] Test repeat imports, unauthorized project access, provenance, timestamps, and failed imports.
- [ ] Add reusable adapter contract tests for search, details, explicit links, and freshness.
- [ ] Record required focused checks and applicable earlier regression gates with actual results.
- [ ] Present milestone evidence to the owner and stop before the next milestone.

### Approved MVP revision checks

- [ ] Fresh isolated persistence setup and repeatable fixture loading pass; repeated composite source IDs return the existing stored record unchanged.
- [ ] PO_PM can ingest; MEMBER cannot mutate or investigate. Source visibility denies inaccessible project/source reads.
- [ ] Reusable source/Jira adapter tests check canonical identity, explicit link direction, missing/forbidden/timeout fixtures, and no provider writes.

## Approval and milestone acceptance

- Approved specification commit, task scopes/checks, approver/date: pending.
- Milestone acceptance evidence and owner/date: pending.
- Runner verification evidence: none recorded.

The Runner owns verified completion links. Before it exists, an independent operator records bootstrap checks explicitly as operator verification; coding agents never mark VERIFIED.
