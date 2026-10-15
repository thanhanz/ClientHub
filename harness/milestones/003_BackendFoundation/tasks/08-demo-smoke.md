# 003-P08 — Reproducible startup and milestone evidence

Status: BLOCKED - prepared scope; milestone approvals, listed decisions and exact checks pending. One session.

Task ID: 003-P08

Milestone: 003

Depends on: 003-P01, 003-P02, 003-P03, 003-P04, 003-P05, 003-P06, 003-P07

## Objective

Assemble the already implemented components into a clean-store smoke/regression gate and document evidence for owner review.

## Dependencies

P01–P07 independently verified; G6–G7 closed; 002's harness check interface available; exact product commands approved.

## Allowed changes

`scripts/verify.ps1`, `scripts/backend-foundation-smoke.ps1`, `tests/Hub.Tests/Acceptance/BackendFoundation/**`. If approved provisioning requires Compose, config, Dockerfile or CI edits, name those exact files in the executable task before issuance; none is implicitly allowed here.

## Implementation and acceptance

Fresh isolated store migrates and starts; runtime fixture loading twice yields unchanged existing sources; HTTP role/source isolation and provider contract suites pass together; readiness failure is observable; runtime fixtures remain separate from expectations. Verification discovers and runs all required tests, includes earlier applicable regression gates, records actual commands/exit codes and tested revision, and fails rather than silently skipping unavailable checks. The final handoff distinguishes implementation, local checks, independent Runner evidence and pending owner acceptance. Do not create Runner evidence/checkpoints or record owner approval on the owner's behalf.

## Tests

full build/test, schema validator, approved migration/fixture/API smoke and 002 regression modes. Stop after evidence handoff for owner review; no 004 execution.

Candidate checks are NOT_RUN. Filters name planned tests, not existing evidence. Approval must bind all required migration/schema/fixture/smoke commands after gaps close; this task is not dispatchable yet.

```json
[
  {
    "executable": "dotnet",
    "args": [
      "build",
      "ClientHub.slnx"
    ],
    "expected_exit": 0,
    "id": "003-P08-check-1",
    "cwd": ".",
    "timeout_seconds": 600
  },
  {
    "executable": "dotnet",
    "args": [
      "test",
      "tests/Hub.Tests/Hub.Tests.csproj"
    ],
    "expected_exit": 0,
    "required_result": "Positive test discovery; every task acceptance case passing",
    "id": "003-P08-check-2",
    "cwd": ".",
    "timeout_seconds": 600
  },
  {
    "executable": "python",
    "args": [
      "scripts/validate-contracts.py"
    ],
    "expected_exit": 0,
    "id": "003-P08-check-3",
    "cwd": ".",
    "timeout_seconds": 600
  }
]
```

## Limits and generated outputs

Agent timeout: 1800 seconds. Each check: 600 seconds. No automatic retries. Starting context target: 10,000-30,000 tokens; below 100,000.

Permitted build/test outputs: `src/Hub.Api/bin/`, `src/Hub.Api/obj/`, `tests/Hub.Tests/bin/`, `tests/Hub.Tests/obj/`, `TestResults/`, `tests/Hub.Tests/TestResults/`. Additional provisioning/output paths require approval before dispatch. None may contain hidden source inputs.

## Stop conditions

Unresolved task-specific G1-G7 decisions, missing approval/dependency evidence, incompatible contracts, out-of-scope changes or oversized context block work. Do not invent missing behavior or weaken tests.

## Selected references

Use [milestone reference paths](../goal.md#contracts-and-readiness), reading only: milestone acceptance; dependency handoffs/check commands; startup/fixture lifecycle.

## Context and handoff

Read AGENTS.md, relevant sections of [milestone goal](../goal.md), [execution policy](../../../policies/execution.md), and verified prerequisite handoffs. Target 10,000-30,000 starting tokens; strictly below 100,000. Stop and propose a split if scope/context is too large. This does not guarantee a total-session token limit.

Return all seven AGENTS.md handoff fields, exact test exits, exported interfaces and downstream notes. End the session. Only the operator/Runner verifies and commits. Never write real run records or launch the next task.
