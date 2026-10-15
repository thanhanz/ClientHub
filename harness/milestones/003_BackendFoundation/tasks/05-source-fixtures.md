# 003-P05 — Scenario source reader and fixture intake

Status: BLOCKED - prepared scope; milestone approvals, listed decisions and exact checks pending. One session.

Task ID: 003-P05

Milestone: 003

Depends on: 003-P01, 003-P03, 003-P04

## Objective

Provide deterministic runtime source fixtures through the approved source-reader port and existing authorized ingestion service.

## Dependencies

P01, P03, P04; G5–G6 closed.

## Allowed changes

`src/Hub.Api/Infrastructure/ExternalSources/**`, `src/Hub.Api/Fixtures/Sources/**`, `src/Hub.Api/Program.cs`, `tests/Hub.Tests/ContractTests/ExternalSources/**`, `tests/Hub.Tests/Fixtures/SourceExpectations/**`.

## Implementation and acceptance

Google Login, Sales Export and Discount inputs preserve external IDs, project, actor metadata, occurrence/import conventions, approved meeting notes and D-03 DATE precision. Loading twice is repeatable through P04; adapters neither write persistent entities directly nor bypass authorization. Deterministic paging yields no missing/duplicate items in a snapshot. Missing/forbidden/invalid/timeout behavior uses approved signals. Runtime assets never contain expected extracted events, mapping decisions or findings. Reusable source contract suite covers PR-04/06/07/08/09 where applicable.

## Tests

proposed filter `FullyQualifiedName~ExternalSourceContract`; expectation assets remain test-only. Stop if scenario input revision or loading/reset entry point is unapproved.

Candidate checks are NOT_RUN. Filters name planned tests, not existing evidence. Approval must bind all required migration/schema/fixture/smoke commands after gaps close; this task is not dispatchable yet.

```json
[
  {
    "executable": "dotnet",
    "args": [
      "test",
      "tests/Hub.Tests/Hub.Tests.csproj",
      "--filter",
      "FullyQualifiedName~ExternalSourceContract"
    ],
    "expected_exit": 0,
    "required_result": "Positive test discovery; every task acceptance case passing",
    "id": "003-P05-check-1",
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

Use [milestone reference paths](../goal.md#contracts-and-readiness), reading only: source reader contract; selected scenario source inputs; test-only expectations.

## Context and handoff

Read AGENTS.md, relevant sections of [milestone goal](../goal.md), [execution policy](../../../policies/execution.md), and verified prerequisite handoffs. Target 10,000-30,000 starting tokens; strictly below 100,000. Stop and propose a split if scope/context is too large. This does not guarantee a total-session token limit.

Return all seven AGENTS.md handoff fields, exact test exits, exported interfaces and downstream notes. End the session. Only the operator/Runner verifies and commits. Never write real run records or launch the next task.
