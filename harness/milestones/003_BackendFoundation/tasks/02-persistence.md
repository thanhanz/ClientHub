# 003-P02 — Minimal isolated persistence

Status: BLOCKED - prepared scope; milestone approvals, listed decisions and exact checks pending. One session.

Task ID: 003-P02

Milestone: 003

Depends on: 003-P01

## Objective

Add project, membership and source storage plus explicit migrations against the chosen database.

## Dependencies

P01; G2, G4, G7 closed. Bind approved minimal schema and test-database lifecycle.

## Allowed changes

`src/Hub.Api/Infrastructure/Persistence/**`, `src/Hub.Api/Features/Projects/Models/**`, `src/Hub.Api/Features/Sources/Models/**`, `src/Hub.Api/Hub.Api.csproj`, `tests/Hub.Tests/Hub.Tests.csproj`, `tests/Hub.Tests/Integration/BackendFoundation/Persistence/**`.

## Implementation and acceptance

Clean isolated database can migrate; repeat migration is safe; data survives a fresh application/database connection; membership uniqueness, ownership FK and composite source uniqueness are enforced; occurrence/import/observation times and permitted precision/content persist; independent projects can use otherwise identical provider IDs. Concurrent duplicate insert cannot produce two records. No event, mapping, review-audit or Jira-mirror tables.

## Tests

proposed filter `FullyQualifiedName~BackendFoundationPersistence`, using the approved real database rather than an in-memory substitute; migration command is pending G2/G7. Stop if schema or provisioning needs an unapproved infrastructure path.

Candidate checks are NOT_RUN. Filters name planned tests, not existing evidence. Approval must bind all required migration/schema/fixture/smoke commands after gaps close; this task is not dispatchable yet.

```json
[
  {
    "executable": "dotnet",
    "args": [
      "test",
      "tests/Hub.Tests/Hub.Tests.csproj",
      "--filter",
      "FullyQualifiedName~BackendFoundationPersistence"
    ],
    "expected_exit": 0,
    "required_result": "Positive test discovery; every task acceptance case passing",
    "id": "003-P02-check-1",
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

Use [milestone reference paths](../goal.md#contracts-and-readiness), reading only: ERD project/membership/source tables; approved database decision; P01 handoff.

## Context and handoff

Read AGENTS.md, relevant sections of [milestone goal](../goal.md), [execution policy](../../../policies/execution.md), and verified prerequisite handoffs. Target 10,000-30,000 starting tokens; strictly below 100,000. Stop and propose a split if scope/context is too large. This does not guarantee a total-session token limit.

Return all seven AGENTS.md handoff fields, exact test exits, exported interfaces and downstream notes. End the session. Only the operator/Runner verifies and commits. Never write real run records or launch the next task.
