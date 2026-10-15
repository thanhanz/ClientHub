# 003-P03 — Guarded identity and project/source authorization

Status: BLOCKED - prepared scope; milestone approvals, listed decisions and exact checks pending. One session.

Task ID: 003-P03

Milestone: 003

Depends on: 003-P01, 003-P02

## Objective

Implement trusted fixture principal resolution and reusable backend membership/role/source access services.

## Dependencies

P01, P02; G3 closed.

## Allowed changes

`src/Hub.Api/Infrastructure/Security/**`, `src/Hub.Api/Features/Projects/Authorization/**`, `src/Hub.Api/Features/Sources/Authorization/**`, `src/Hub.Api/Program.cs`, `tests/Hub.Tests/Integration/BackendFoundation/Authorization/**`.

## Implementation and acceptance

Test/Development fixture identity works only under approved guards; Production cannot activate it; caller headers/body cannot grant actor identity, role or membership. Nonmember access is denied before protected reads; MEMBER may read accessible PROJECT_MEMBERS sources but cannot mutate; PO_PM_ONLY reads are denied to MEMBER. Cross-project locators fail safely. Test principals cover PO_PM, MEMBER, outsider and unauthenticated access. Future investigation permission can reuse this service; do not create investigation endpoints.

## Tests

proposed filter `FullyQualifiedName~BackendFoundationAuthorization`. Stop on unspecified identity provisioning or ACL behavior.

Candidate checks are NOT_RUN. Filters name planned tests, not existing evidence. Approval must bind all required migration/schema/fixture/smoke commands after gaps close; this task is not dispatchable yet.

```json
[
  {
    "executable": "dotnet",
    "args": [
      "test",
      "tests/Hub.Tests/Hub.Tests.csproj",
      "--filter",
      "FullyQualifiedName~BackendFoundationAuthorization"
    ],
    "expected_exit": 0,
    "required_result": "Positive test discovery; every task acceptance case passing",
    "id": "003-P03-check-1",
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

Use [milestone reference paths](../goal.md#contracts-and-readiness), reading only: domain roles/source access; API section 4; trusted identity decision.

## Context and handoff

Read AGENTS.md, relevant sections of [milestone goal](../goal.md), [execution policy](../../../policies/execution.md), and verified prerequisite handoffs. Target 10,000-30,000 starting tokens; strictly below 100,000. Stop and propose a split if scope/context is too large. This does not guarantee a total-session token limit.

Return all seven AGENTS.md handoff fields, exact test exits, exported interfaces and downstream notes. End the session. Only the operator/Runner verifies and commits. Never write real run records or launch the next task.
