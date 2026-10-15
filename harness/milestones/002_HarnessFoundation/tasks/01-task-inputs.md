# HF-002-01 - Task loading and context packet

Status: BLOCKED - prepared scope; prerequisite acceptance and exact task/revision approval pending. One session.

Task ID: HF-002-01

Milestone: 002

Depends on: none (milestone prerequisites still apply)

## Objective

Load one finite approved milestone, validate compact task inputs and build context from references and verified dependency handoffs.

## Dependencies

accepted 001 or an explicitly approved bounded bootstrap deferral; approved current task scope. A deferral must retain product blocks.

## Allowed changes

`scripts/harness/runner.ps1`, `scripts/harness/inputs.ps1`, `tests/Harness.Tests/verify.ps1`, `tests/Harness.Tests/fixtures/`.

## Implementation and acceptance

Missing approval/reference/dependency, wrong revision, duplicate IDs, invalid paths and dependency cycles/order reject before dispatch. Packets include baseline commit and relevant dependency interfaces/limitations. Dirty starts reject without altering files. No session dispatch, commits or real checkpoint records yet.

## Tests

`pwsh -NoProfile -File tests/Harness.Tests/verify.ps1 -Suite Inputs`; `git diff --check`.

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
      "Inputs"
    ],
    "expected_exit": 0,
    "required_result": "All scenarios exercised; positive assertion count; no skipped required scenario",
    "id": "HF-002-01-check-1",
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
    "id": "HF-002-01-check-2",
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

Read these sections of [goal](../goal.md): Execution model, Inputs and context, Task input format, Run input and approval, Session context and handoff.

## Context and handoff

Read AGENTS.md, relevant sections of [milestone goal](../goal.md), [execution policy](../../../policies/execution.md), and verified prerequisite handoffs. Target 10,000-30,000 starting tokens; strictly below 100,000. Stop and propose a split if scope/context is too large. This does not guarantee a total-session token limit.

Return all seven AGENTS.md handoff fields, exact test exits, exported interfaces and downstream notes. End the session. Only the operator/Runner verifies and commits. Never write real run records or launch the next task.
