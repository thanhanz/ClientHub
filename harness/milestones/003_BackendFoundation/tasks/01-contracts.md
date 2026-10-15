# 003-P01 — Backend source/provider contract types

Status: BLOCKED - prepared scope; milestone approvals, listed decisions and exact checks pending. One session.

Task ID: 003-P01

Milestone: 003

Depends on: none (milestone prerequisites still apply)

## Objective

Translate approved 003 contracts into C# types and read-only ports, without storage, endpoints or providers.

## Dependencies

milestone entry gates; G3–G5 closed. Bind domain/API/provider/source-schema revisions and approved DTO decisions in the eventual task.

## Allowed changes

`src/Hub.Api/Contracts/Sources/**`, `src/Hub.Api/Contracts/Providers/**`, `tests/Hub.Tests/Contracts/BackendFoundation/**`.

## Implementation and acceptance

Required composite source/Jira locators preserve project and instance identity; canonical enum spellings and snake_case/UUID/UTC/version semantics match approved contracts; source precision and actor provenance survive serialization; failure/page/coverage types match approved envelopes; Jira ports expose no write operations. Source and problem response compatibility checks pass. No events/mappings/AI or new packages unless separately scoped.

## Tests

proposed filter `FullyQualifiedName~BackendFoundationContracts`; exact serialization/schema command and nonzero discovered tests must be approved. Stop if translating a contract requires choosing missing behavior.

Candidate checks are NOT_RUN. Filters name planned tests, not existing evidence. Approval must bind all required migration/schema/fixture/smoke commands after gaps close; this task is not dispatchable yet.

```json
[
  {
    "executable": "dotnet",
    "args": [
      "test",
      "tests/Hub.Tests/Hub.Tests.csproj",
      "--filter",
      "FullyQualifiedName~BackendFoundationContracts"
    ],
    "expected_exit": 0,
    "required_result": "Positive test discovery; every task acceptance case passing",
    "id": "003-P01-check-1",
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

Use [milestone reference paths](../goal.md#contracts-and-readiness), reading only: domain-contracts sections 1, 2, 5-7; provider-contracts sections 1-5; source schema.

## Context and handoff

Read AGENTS.md, relevant sections of [milestone goal](../goal.md), [execution policy](../../../policies/execution.md), and verified prerequisite handoffs. Target 10,000-30,000 starting tokens; strictly below 100,000. Stop and propose a split if scope/context is too large. This does not guarantee a total-session token limit.

Return all seven AGENTS.md handoff fields, exact test exits, exported interfaces and downstream notes. End the session. Only the operator/Runner verifies and commits. Never write real run records or launch the next task.
