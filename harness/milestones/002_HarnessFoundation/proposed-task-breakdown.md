# Proposed task breakdown — HF-002-R1

Status: PROPOSED; deliberately outside `tasks/`. None of these entries is an executable assignment. Owner must settle [design](proposed-design.md), [contracts](proposed-contracts.md), [prerequisites](review.md), then approve exact task files and their hashes/gates. Paths and commands below are proposed for that approval, not permission to write them in this session.

## Common prerequisites, gates and stopping rules

All tasks require explicit 001 acceptance, owner approval of 002 revision and exact task scope/gates, clean approved baseline or explicit isolated-worktree authorization, PowerShell 7/Git capability evidence, and an independently checked dependency summary. Actual versions/hashes replace descriptive revision names in executable tasks. Never infer approval from this draft. Each task is one fresh explicitly assigned bootstrap session; later Runner availability does not permit self-dispatch.

Common handoff: TASK_ID, RESULT (IMPLEMENTED/BLOCKED/FAILED), CHANGED_FILES from actual inventory, CONTRACTS_EXPORTED_OR_CHANGED, TESTS_RUN with exact commands/exit codes, KNOWN_ISSUES, DOWNSTREAM_NOTES. Include approved revision, dependency evidence and test tree inventory references in downstream notes. Independent operator reruns the prescribed gates and records exact tree/exits outside the agent session; coding-agent PASS is not VERIFIED. No agent writes `harness/runs/`.

All tasks stop after their handoff. Stop earlier on missing approval/contracts, out-of-scope requirement/change, incompatible dependency evidence, failed prerequisites, ambiguous decisions or repeated gate failure. Do not weaken checks, alter state, issue approvals, launch another task/session, accept 002 or execute 003. Any additional path requires a scope amendment before edits. Test drivers use disposable repositories and fake children; fixtures are synthetic, never real approval or authoritative state. All commands below must exit 0 and satisfy assertions, not merely finish. Test drivers must fail nonzero on any missing scenario, skipped assertion or unexpected result.

Proposed future independent gate entry point is `tests/Harness.Tests/verify.ps1 -Suite <name>`; until created, it is NOT_RUN, not an existing repository gate. It must support `Contracts`, `Preflight`, `Sessions`, `Recovery`, `All`, and emit counts/results. No mandatory dependency on product build restoration for harness unit tests. Existing earlier applicable gates must be retained in task approval; recorded 001 failures require resolution or explicit owner disposition, never silently dropped.

## HF-002-01 — Strict contracts and test foundation

Goal: implement strict v1 JSON validation/serialization and a dependency-free PowerShell assertion driver. Dependencies: accepted 001 (review evidence, not an invented task ID). Prerequisite contracts: approved proposed-contracts.md v1; manifest canonicalization and tree identity from approved design; exact task/gate approval.

Allowed paths (only these directory prefixes): `scripts/harness/contracts/`, `tests/Harness.Tests/contracts/`; exact files `tests/Harness.Tests/verify.ps1`, `tests/Harness.Tests/TestSupport.ps1`. Do not create approved inputs or state.

Acceptance: all task/handoff/approval/attempt/state/checkpoint/verification/acceptance/reconciliation shapes validate strictly; malformed/duplicate keys, unknown fields/version, traversal, unsupported states, inconsistent PASS exits and incomplete checks fail; canonical digests stable across property/input ordering and sensitive to bytes; agent handoffs cannot express VERIFIED. Test driver deliberately exercises a failing assertion and observes nonzero child exit. Valid and invalid synthetic fixtures are labeled as such.

Verification commands:
- `pwsh -NoProfile -File tests/Harness.Tests/verify.ps1 -Suite Contracts`
- `git diff --check`

Handoff: common fields plus exported validator functions, contract version and rejected-shape coverage. Stop: common rules; no dispatcher or state mutation implemented in this task.

## HF-002-02 — Approval, readiness, tree and scope preflight

Goal: fail closed on unapproved/stale/unready work and identify exact source bytes with scope reconciliation. Dependencies: HF-002-01 independently checked on compatible approved baseline. Prerequisite contracts: strict v1 contracts, approved inventory/output-root rules and owner approval/001 acceptance inputs.

Allowed directory prefixes: `scripts/harness/preflight/`, `tests/Harness.Tests/preflight/`. Exact files: `tests/Harness.Tests/verify.ps1`, `tests/Harness.Tests/TestSupport.ps1` (only suite registration/support additions).

Acceptance: valid same-milestone task ready only with bound approval and dependencies; missing contracts, cycles, changed task/gates/approval/spec bytes and invalid evidence reject before dispatch. Inventory catches tracked/staged/unstaged/untracked/ignored source changes, deletions and both rename paths; rejects case alias, traversal, junction and output-root evasion. A dirty original workspace is unchanged and blocks default start; explicit clean isolated baseline excludes dirt. Changed cumulative tree requires current regression evidence. Gate commands are approved argv, not shell strings. Protected verifier/state paths cannot be allowed. Tests compare byte hashes of unrelated dirty files before/after all paths.

Verification commands:
- `pwsh -NoProfile -File tests/Harness.Tests/verify.ps1 -Suite Contracts`
- `pwsh -NoProfile -File tests/Harness.Tests/verify.ps1 -Suite Preflight`
- `git diff --check`

Handoff: common fields plus inventory format/digest and rejection assertions. Stop: common rules; no session launch or verified checkpoint.

## HF-002-03 — Fresh session supervisor and independent checks

Goal: implement one-task dispatch, structured handoff collection and trusted independent gates with deadlines/cancellation. Dependencies: HF-002-01 and HF-002-02 independently checked. Prerequisite contracts: v1 task/handoff/attempt; approved CLI capability record specifying actual fresh-session flags, writable scope, final-output transport and Job Object/process-tree behavior. Missing capability record blocks this task.

Allowed directory prefixes: `scripts/harness/execution/`, `tests/Harness.Tests/execution/`. Exact files: `tests/Harness.Tests/verify.ps1`, `tests/Harness.Tests/TestSupport.ps1` (registration/support additions).

Acceptance: fake adapter counts one invocation per attempt with no history reuse; exact task/revision/dependency bundle; malformed/missing/mismatched handoffs stop. Agent success plus failing/missing checks never passes. Runner uses trusted gates and captures actual exit/assertions; agent-modified gate source is rejected. Source edits during verification invalidate results. Timeouts, cancellation and Runner death kill descendants before releasing writer ownership; output capped/redacted; no credentials in bundle/logs. Actual installed CLI smoke test demonstrates separate fresh sessions, denial of protected writes and cancellation in a disposable repository without product edits; no fake test substitutes for capability evidence.

Verification commands:
- `pwsh -NoProfile -File tests/Harness.Tests/verify.ps1 -Suite Contracts`
- `pwsh -NoProfile -File tests/Harness.Tests/verify.ps1 -Suite Preflight`
- `pwsh -NoProfile -File tests/Harness.Tests/verify.ps1 -Suite Sessions`
- `pwsh -NoProfile -File tests/Harness.Tests/execution/cli-smoke.ps1`
- `git diff --check`

Handoff: common fields plus CLI version/flags, isolation and termination evidence, actual smoke-test outcomes. Stop: common rules; no authoritative checkpoint generation. Missing CLI/authentication/permission capability is BLOCKED, not skipped PASS.

## HF-002-04 — Exclusive state publication and safe recovery

Goal: implement exclusive workspace ownership, immutable attempts, atomic checkpoints, reconciliation and bounded resume. Dependencies: HF-002-01–03 independently checked. Prerequisite contracts: v1 state/checkpoint/verification/reconciliation, approved NTFS and Job Object constraints, budgets, snapshot restore policy.

Allowed directory prefixes: `scripts/harness/persistence/`, `tests/Harness.Tests/persistence/`. Exact files: `tests/Harness.Tests/verify.ps1`, `tests/Harness.Tests/TestSupport.ps1` (registration/support additions). Tests write only into disposable synthetic run roots, not repository `harness/runs/`.

Acceptance: simultaneous runs for same common Git workspace yield exactly one writer; loser leaves no state mutation. Crash injection before/after evidence, snapshot and state replace never yields false VERIFIED; committed state validates all refs/generation. Truncated/corrupt/missing records stop. Interrupted work is preserved and reconciled before retry; no reset over dirt; stale specification/tree/environment/check/dependency invalidates evidence transitively. Attempt/time budgets survive restarts; two total attempts maximum, no automatic unsafe retries. Child remains running after supervisor crash is impossible or recovery blocks. Cancelled run cannot silently resume. Restored snapshot hashes exactly match checkpoint in empty isolated worktree.

Verification commands:
- `pwsh -NoProfile -File tests/Harness.Tests/verify.ps1 -Suite Contracts`
- `pwsh -NoProfile -File tests/Harness.Tests/verify.ps1 -Suite Preflight`
- `pwsh -NoProfile -File tests/Harness.Tests/verify.ps1 -Suite Sessions`
- `pwsh -NoProfile -File tests/Harness.Tests/verify.ps1 -Suite Recovery`
- `git diff --check`

Handoff: common fields plus publication ordering, injected crash boundaries and resume/budget evidence. Stop: common rules; do not write real run state or authorize another task.

## HF-002-05 — CLI integration and milestone evidence

Goal: connect approved components into minimal external Runner and demonstrate milestone hard stops. Dependencies: HF-002-01–04 independently checked with compatible current cumulative tree/regression evidence. Prerequisite contracts: all v1 contracts, actual CLI capability record, accepted 001, approved finite 002 task set, approved exact regression gates and budgets.

Allowed exact files: `scripts/harness/runner.ps1`, `tests/Harness.Tests/verify.ps1`, `tests/Harness.Tests/TestSupport.ps1`, `harness/milestones/002_HarnessFoundation/implementation-evidence.md`. Allowed directory prefix: `tests/Harness.Tests/integration/`. Cross-component fixes outside these paths require amended task scope, not opportunistic edits.

Acceptance: end-to-end synthetic approved finite milestone has one fresh invocation per task, independent checks and durable verified checkpoints in temporary fixtures; all required matrix scenarios below pass. Run ends AWAITING_OWNER_REVIEW and does not dispatch unapproved same-milestone task or 003 even with available files. Bootstrap operator—not coding agent—records independent actual evidence for real implementation; evidence document distinguishes implemented, independently checked and owner accepted. No auto-commit, workflow service or product behavior. Owner reviews milestone evidence before acceptance/003 authorization.

Verification commands:
- `pwsh -NoProfile -File tests/Harness.Tests/verify.ps1 -Suite All`
- `pwsh -NoProfile -File tests/Harness.Tests/execution/cli-smoke.ps1`
- `git diff --check`

Handoff: common fields plus full matrix counts, independent evidence gaps and milestone review packet location. Stop at 002 boundary; no acceptance declaration or next-session launch.

## Required integration matrix

| Scenario | Assertions / no false success | Primary task |
| --- | --- | --- |
| Success | Correct approval/dependencies; actual gates pass; exact before/after tree; one committed checkpoint; next ready task only within approved set | 05 |
| Failed or missing checks | Nonzero, absent assertion, omitted command and timeout each block checkpoint/advancement; handoff PASS has no authority | 03/05 |
| Out-of-scope edits | Tracked/untracked/ignored/deleted/renamed/protected-path changes preserved, rejected and never checkpointed | 02/05 |
| Interruption | Agent/check/Runner termination and every atomic-write boundary; no uncertain success; child killed; resume reconciles | 03/04/05 |
| Stale revisions | Change approval, task, gate, contract, source, dependency evidence or environment separately; reuse blocked and dependents invalidated | 02/04/05 |
| Concurrent execution | Same run and different run IDs/worktrees on same repository reject second writer without mutations | 04/05 |
| Unapproved task/boundary | Unknown task, extra same-milestone task and ready-looking 003 rejected before process creation; completed 002 stops for owner | 02/05 |
| Dirty reconciliation | Original dirt byte-identical; interrupted in-scope edits require recorded decision; unknown dirt blocks | 02/04/05 |
| Limits/cancellation | Retry exhaustion persists across restart; clock rollback cannot replenish time; Ctrl+C/cancel kills child tree and stops | 03/04/05 |

## Assignment template after approval

Use the user's supplied execution prompt once per task in a fresh session. Substitute the exact approved task ID/file, revision digest, owner approval path and independent verified dependency evidence; do not leave placeholders or use this draft as those inputs. External operator issues bootstrap sessions and reviews each result. Only after all approved tasks and independent milestone gates are evidenced does the owner review acceptance of 002 and separately authorize 003.
