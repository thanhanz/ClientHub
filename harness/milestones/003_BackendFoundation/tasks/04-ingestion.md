# 003-P04 — Authorized source ingestion service

Status: BLOCKED - prepared scope; milestone approvals, listed decisions and exact checks pending. One session.

Task ID: 003-P04

Milestone: 003

Depends on: 003-P01, 003-P02, 003-P03

## Objective

Implement normalized intake behind an application interface, including immutable duplicate behavior and retention validation.

## Dependencies

P01–P03; G4 closed.

## Allowed changes

`src/Hub.Api/Features/Sources/Ingestion/**`, `src/Hub.Api/Infrastructure/Persistence/SourceRepository.cs`, `tests/Hub.Tests/Integration/BackendFoundation/Ingestion/**`.

## Implementation and acceptance

PO_PM intake persists required provenance and available actor/time metadata; stable composite identity is mandatory; repeat and changed-content imports return the existing ID/content/metadata/timestamps unchanged; concurrent duplicates return one stored record. Unauthorized, malformed, invalid-project, invalid-time and prohibited-retention imports leave no new record. METADATA_ONLY stores no body; APPROVED_NOTES stores only approved notes; meeting evidence never gains fabricated transcript/speaker detail. Transaction boundaries and duplicate validation order follow the approved decision. No extraction, jobs, ID-less intake or general idempotency-key store.

## Tests

proposed filter `FullyQualifiedName~BackendFoundationIngestion`, including DB-01 and V-DUPLICATE. Stop if rejection/deduplication ordering or content handling is unresolved.

Candidate checks are NOT_RUN. Filters name planned tests, not existing evidence. Approval must bind all required migration/schema/fixture/smoke commands after gaps close; this task is not dispatchable yet.

```json
[
  {
    "executable": "dotnet",
    "args": [
      "test",
      "tests/Hub.Tests/Hub.Tests.csproj",
      "--filter",
      "FullyQualifiedName~BackendFoundationIngestion"
    ],
    "expected_exit": 0,
    "required_result": "Positive test discovery; every task acceptance case passing",
    "id": "003-P04-check-1",
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

Use [milestone reference paths](../goal.md#contracts-and-readiness), reading only: source identity/retention; intake contract; P01-P03 handoffs.

## Context and handoff

Read AGENTS.md, relevant sections of [milestone goal](../goal.md), [execution policy](../../../policies/execution.md), and verified prerequisite handoffs. Target 10,000-30,000 starting tokens; strictly below 100,000. Stop and propose a split if scope/context is too large. This does not guarantee a total-session token limit.

Return all seven AGENTS.md handoff fields, exact test exits, exported interfaces and downstream notes. End the session. Only the operator/Runner verifies and commits. Never write real run records or launch the next task.
