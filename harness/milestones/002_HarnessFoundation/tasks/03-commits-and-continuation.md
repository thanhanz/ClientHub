# HF-002-03 - Verified commits, records and milestone stop

Status: BLOCKED - prepared scope; prerequisite acceptance and exact task/revision approval pending. One session.

Task ID: HF-002-03

Milestone: 002

Depends on: HF-002-01, HF-002-02

## Objective

Finish the loop with exclusive workspace ownership, one verified commit per task, simple records and explicit continuation checks.

## Dependencies

HF-002-01?02 independently checked on compatible code.

## Allowed changes

`scripts/harness/runner.ps1`, `scripts/harness/records.ps1`, `tests/Harness.Tests/verify.ps1`, `tests/Harness.Tests/fixtures/`.

## Implementation and acceptance

Stage only task changes; two successful synthetic tasks produce two commits, complete records and two fresh sessions. No automatic push. Failures prevent commit/advancement; commit failure or changed hook output prevents a completed checkpoint. Dirty workspace, concurrent Runner, incomplete/corrupt record, unrecorded commit, changed specification or mismatched HEAD stops for manual review. A checkpoint is written only after commit validation. No automatic retries, cleanup or inferred recovery. Completion stops at the approved milestone with AWAITING_OWNER_REVIEW.

## Tests

`pwsh -NoProfile -File tests/Harness.Tests/verify.ps1 -Suite All`; `pwsh -NoProfile -File tests/Harness.Tests/cli-smoke.ps1`; `git diff --check`.

Return evidence in the final handoff; operator/Runner records are linked from the checklist. No automatic dispatch of 003 during this bootstrap task.

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
      "All"
    ],
    "expected_exit": 0,
    "required_result": "All scenarios exercised; positive assertion count; no skipped required scenario",
    "id": "HF-002-03-check-1",
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
    "id": "HF-002-03-check-2",
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
    "id": "HF-002-03-check-3",
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

Read these sections of [goal](../goal.md): Commits and records, Failure/interruption/continuation, Runner-owned local records; HF-002-01/02 exports.

## Context and handoff

Read AGENTS.md, relevant sections of [milestone goal](../goal.md), [execution policy](../../../policies/execution.md), and verified prerequisite handoffs. Target 10,000-30,000 starting tokens; strictly below 100,000. Stop and propose a split if scope/context is too large. This does not guarantee a total-session token limit.

Return all seven AGENTS.md handoff fields, exact test exits, exported interfaces and downstream notes. End the session. Only the operator/Runner verifies and commits. Never write real run records or launch the next task.
