# HF-002-02 - Fresh sessions and independent checks

Status: BLOCKED - prepared scope; prerequisite acceptance and exact task/revision approval pending. One session.

Task ID: HF-002-02

Milestone: 002

Depends on: HF-002-01

## Objective

Implement the task execution loop, scope comparison, handoff capture, focused checks and normal timeout/cancellation handling.

## Dependencies

HF-002-01 independently checked; installed Codex CLI capability evidence for actual invocation and output capture.

## Allowed changes

`scripts/harness/runner.ps1`, `scripts/harness/execution.ps1`, `tests/Harness.Tests/verify.ps1`, `tests/Harness.Tests/fixtures/`, `tests/Harness.Tests/cli-smoke.ps1`.

## Implementation and acceptance

Separate invocation per task, correct context, no session reuse; missing/mismatched handoff, agent commit/index edits, out-of-scope change and failed/missing/zero-test gates stop. Source changes during verification invalidate results. Check both rename paths, deletions, untracked and ignored source. Approved task/check definitions remain protected. Timeout/Ctrl+C stop descendants in normal operation; abrupt Runner loss requires manual reconciliation. No commit or next-task advancement until 03 supplies that boundary.

## Tests

`pwsh -NoProfile -File tests/Harness.Tests/verify.ps1 -Suite Execution` (includes Inputs); `pwsh -NoProfile -File tests/Harness.Tests/cli-smoke.ps1`; `git diff --check`.

Checks to implement and approve, currently NOT_RUN/unavailable:

```json
[
  {
    "executable": "pwsh",
    "args": [
      "-NoProfile",
      "-File",
      "tests/Harness.Tests/verify.ps1",
      "-Suite",
      "Execution"
    ],
    "expected_exit": 0,
    "required_result": "All scenarios exercised; positive assertion count; no skipped required scenario",
    "id": "HF-002-02-check-1",
    "cwd": ".",
    "timeout_seconds": 600
  },
  {
    "executable": "pwsh",
    "args": [
      "-NoProfile",
      "-File",
      "tests/Harness.Tests/cli-smoke.ps1"
    ],
    "expected_exit": 0,
    "required_result": "Fresh invocation, handoff capture and normal cancellation",
    "id": "HF-002-02-check-2",
    "cwd": ".",
    "timeout_seconds": 600
  },
  {
    "executable": "git",
    "args": [
      "diff",
      "--check"
    ],
    "expected_exit": 0,
    "id": "HF-002-02-check-3",
    "cwd": ".",
    "timeout_seconds": 600
  }
]
```

## Limits and generated outputs

Agent timeout: 1800 seconds. Each check: 600 seconds. No automatic retries. Starting context target: 10,000-30,000 tokens; below 100,000.

Test fixtures use disposable temporary repositories outside product source; delete only the test-owned fixtures. Generated check logs may use `artifacts/harness-tests/`. Runner records for real runs remain forbidden to the coding agent.

## Stop conditions

Missing prerequisites/approval, incompatible CLI capability, out-of-scope requirements or oversized work block execution. Never weaken gates.

## Selected references

Read these sections of [goal](../goal.md): Task loop and independent checks, Failure/interruption/continuation, Verification scope; HF-002-01 exports.

## Context and handoff

Read AGENTS.md, relevant sections of [milestone goal](../goal.md), [execution policy](../../../policies/execution.md), and verified prerequisite handoffs. Target 10,000-30,000 starting tokens; strictly below 100,000. Stop and propose a split if scope/context is too large. This does not guarantee a total-session token limit.

Return all seven AGENTS.md handoff fields, exact test exits, exported interfaces and downstream notes. End the session. Only the operator/Runner verifies and commits. Never write real run records or launch the next task.
