# 002 - Checklist

Current planning and evidence index. No new approvals or verified results are recorded. Existing checked document-review items retain their limited meaning; they are not runtime verification.

## Task index

| Task | Readiness | Prerequisite | Verified commit/evidence |
| --- | --- | --- | --- |
| [HF-002-01](tasks/01-task-inputs.md) | BLOCKED | Prerequisite acceptance and task approval pending | None |
| [HF-002-02](tasks/02-session-execution.md) | BLOCKED | Prerequisite acceptance and task approval pending | None |
| [HF-002-03](tasks/03-commits-and-continuation.md) | BLOCKED | Prerequisite acceptance and task approval pending | None |

## Decisions and readiness

- [ ] Approve one PowerShell Runner, dedicated clean workspace and fresh Codex session per task.
- [ ] Approve compact tasks, Git revision binding and dependency context packets.
- [ ] Define scope checks, protected inputs and independent task/regression gates.
- [ ] Approve Runner-owned commits, local handoffs and checkpoint publication after commit validation.
- [ ] Define single-writer locking, timeouts, stop-on-failure and manual reconciliation/continuation.
- [ ] Record prerequisite disposition and owner approval of exact revision, tasks and checks.

## Deliverables and acceptance

- [ ] Load approved tasks and relevant dependency context; reject missing prerequisites and dirty starts.
- [ ] Start one fresh session per task and collect the AGENTS.md handoff.
- [ ] Independently check scope, source stability and prescribed task/regression tests.
- [ ] Commit only verified task changes and publish the completed record after commit validation.
- [ ] Demonstrate failed checks, scope violations, agent commits and commit failures stop advancement.
- [ ] Demonstrate timeout/cancellation, incomplete records, stale inputs and concurrent-run rejection.
- [ ] Require manual reconciliation after interruption; never infer success from a commit alone.
- [ ] Demonstrate two-task success and a hard stop at the approved milestone boundary.
- [ ] Present actual check evidence and CLI smoke results for owner review.

## Approval and milestone acceptance

- Approved specification commit, task scopes/checks, approver/date: pending.
- Milestone acceptance evidence and owner/date: pending.
- Runner verification evidence: none recorded.

The Runner owns verified completion links. Before it exists, an independent operator records bootstrap checks explicitly as operator verification; coding agents never mark VERIFIED.
