# 003-P06 — Source HTTP API and health endpoints

Status: BLOCKED - prepared scope; milestone approvals, listed decisions and exact checks pending. One session.

Task ID: 003-P06

Milestone: 003

Depends on: 003-P02, 003-P03, 003-P04, 003-P05

## Objective

Expose only the approved source list/intake and liveness/readiness routes with dependency injection.

## Dependencies

P02–P05; G4, G7 closed.

## Allowed changes

`src/Hub.Api/Features/Sources/Endpoints/**`, `src/Hub.Api/Features/Health/**`, `src/Hub.Api/Program.cs`, `tests/Hub.Tests/Integration/BackendFoundation/SourceApi/**`.

## Implementation and acceptance

New intake returns 201 and duplicate returns 200 with approved deduplication response; list filters source ACLs before disclosure/paging and respects approved numeric bounds/order/cursor. API-01–03 pass; UUID, source refs, UTC, schema_version and safe ProblemDetails match contracts; 401/404/403 and 400/422 behavior follows API §4. Forged caller identity or project payload cannot bypass URL/principal checks. Health routes follow approved readiness policy and return 503 for specified dependency failures without sensitive details. No later-milestone routes.

## Tests

proposed filter `FullyQualifiedName~BackendFoundationSourceApi`, with response schema validation. Stop if intake/page wire shapes or readiness policy are incomplete.

Candidate checks are NOT_RUN. Filters name planned tests, not existing evidence. Approval must bind all required migration/schema/fixture/smoke commands after gaps close; this task is not dispatchable yet.

```json
[
  {
    "executable": "dotnet",
    "args": [
      "test",
      "tests/Hub.Tests/Hub.Tests.csproj",
      "--filter",
      "FullyQualifiedName~BackendFoundationSourceApi"
    ],
    "expected_exit": 0,
    "required_result": "Positive test discovery; every task acceptance case passing",
    "id": "003-P06-check-1",
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

Use [milestone reference paths](../goal.md#contracts-and-readiness), reading only: source/health API routes; API section 4; P02-P05 handoffs.

## Context and handoff

Read AGENTS.md, relevant sections of [milestone goal](../goal.md), [execution policy](../../../policies/execution.md), and verified prerequisite handoffs. Target 10,000-30,000 starting tokens; strictly below 100,000. Stop and propose a split if scope/context is too large. This does not guarantee a total-session token limit.

Return all seven AGENTS.md handoff fields, exact test exits, exported interfaces and downstream notes. End the session. Only the operator/Runner verifies and commits. Never write real run records or launch the next task.
