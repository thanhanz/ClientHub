# TASK-ID - One cohesive outcome

Status: BLOCKED - replace with the actual readiness and prerequisites. File existence does not authorize execution. One session per task.

Task ID: TASK-ID

Milestone: NNN

Depends on: TASK-IDS or none (milestone prerequisites still apply)

## Objective

State the observable outcome, demo value and exclusions.

## Dependencies

Name prerequisite task IDs and acceptance evidence. The Runner supplies their verified commit IDs and relevant handoffs. Missing/unapproved interfaces block execution.

## Allowed changes

List exact repository-relative files or directory boundaries. Include implementation and task-specific tests. Do not allow Runner records, approval inputs or unrelated product specifications.

## Implementation and acceptance

Describe required behavior, constraints and interfaces. List independently observable success criteria and negative cases. Leave routine implementation choices to the agent. Split unrelated or oversized outcomes into separate task files before dispatch.

## Tests

Use one fenced JSON array of executable/argument objects, expected exit codes and required assertions/test counts. Approve actual commands before dispatch; placeholders make the task BLOCKED. New suites must be implemented in this task, fail when assertions are absent, and report positive test discovery. List focused and explicitly applicable regression checks.

```json
[
  {
    "id": "TASK-ID-check-1",
    "executable": "REPLACE_WITH_ACTUAL_EXECUTABLE",
    "args": [],
    "cwd": ".",
    "timeout_seconds": 600,
    "expected_exit": 0,
    "required_result": "REPLACE_WITH_OBSERVABLE_ASSERTIONS"
  }
]
```

## Limits and generated outputs

Declare allowed generated-output directories and timeouts (002 defaults: 30 minutes agent, 10 minutes per check); source-changing commands cannot be acceptance gates.

## Stop conditions

Stop on missing approval/contracts, out-of-scope requirements, failed prerequisites, ambiguous behavior or oversized scope/context. Return BLOCKED with a concrete suggested split when appropriate. Never weaken tests, retry indefinitely or start another session.

## Selected references

List specific contract sections and code entry points. Read the milestone goal selectively. Include no unrelated history, full-repository dump or expected answers in runtime fixtures.

## Context and handoff

Target 10,000-30,000 starting-context tokens; strictly below 100,000 including supplied instructions and selected references. Record the estimate/method if available; exact total-session usage enforcement is not implemented. Trim optional context or split before dispatch when uncertain near the ceiling.

Return TASK_ID, RESULT (IMPLEMENTED/BLOCKED/FAILED), CHANGED_FILES, CONTRACTS_EXPORTED_OR_CHANGED, TESTS_RUN (exact commands/exits), KNOWN_ISSUES and DOWNSTREAM_NOTES. Identify interface details the next task needs. End the session; the Runner independently verifies, commits and records completion before dispatching the next task.
