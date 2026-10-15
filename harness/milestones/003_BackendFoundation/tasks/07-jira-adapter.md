# 003-P07 — Read-only fake Jira reader and reusable contract suite

Status: BLOCKED - prepared scope; milestone approvals, listed decisions and exact checks pending. One session.

Task ID: 003-P07

Milestone: 003

Depends on: 003-P01, 003-P03

## Objective

Implement the separate Jira port using versioned runtime fixtures and capability-aware adapter tests.

## Dependencies

P01, P03; G5–G6 closed. P05 is not a dependency; shared runtime wiring remains serialized by the Runner.

## Allowed changes

`src/Hub.Api/Infrastructure/Jira/**`, `src/Hub.Api/Fixtures/Jira/**`, `src/Hub.Api/Program.cs`, `tests/Hub.Tests/ContractTests/Jira/**`, `tests/Hub.Tests/Fixtures/JiraExpectations/**`.

## Implementation and acceptance

PR-01–05/08/09 pass for lookup, search, paging, explicit direction and unknown optional fields; applicable PR-10 suite is reusable, but real-adapter runs are NOT_RUN/deferred. AUTH-101 is discoverable without Hub mappings and is explicitly BLOCKED_BY AUTH-102; AUTH-103 sharing an assignee creates no dependency. Composite instance/project filtering, unauthorized project/link targets, missing/forbidden/timeout, stale/partial observations and cyclic-link fixtures preserve approved semantics. No writes, Jira mirror, graph traversal orchestration or LLM. Freshness is preserved, not relabeled current; authorized optional evidence remains available for later 006 without implementing bundles.

## Tests

proposed filter `FullyQualifiedName~JiraAdapterContract`. Stop on missing page/failure/direction/search policy; do not choose a traversal budget for 006.

Candidate checks are NOT_RUN. Filters name planned tests, not existing evidence. Approval must bind all required migration/schema/fixture/smoke commands after gaps close; this task is not dispatchable yet.

```json
[
  {
    "executable": "dotnet",
    "args": [
      "test",
      "tests/Hub.Tests/Hub.Tests.csproj",
      "--filter",
      "FullyQualifiedName~JiraAdapterContract"
    ],
    "expected_exit": 0,
    "required_result": "Positive test discovery; every task acceptance case passing",
    "id": "003-P07-check-1",
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

Use [milestone reference paths](../goal.md#contracts-and-readiness), reading only: Jira reader, directed links and failures; scenario Jira records; P01/P03 handoffs.

## Context and handoff

Read AGENTS.md, relevant sections of [milestone goal](../goal.md), [execution policy](../../../policies/execution.md), and verified prerequisite handoffs. Target 10,000-30,000 starting tokens; strictly below 100,000. Stop and propose a split if scope/context is too large. This does not guarantee a total-session token limit.

Return all seven AGENTS.md handoff fields, exact test exits, exported interfaces and downstream notes. End the session. Only the operator/Runner verifies and commits. Never write real run records or launch the next task.
