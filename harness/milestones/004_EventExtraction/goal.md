# 004 — Event extraction and review

Status: DRAFT — pending milestone review; not execution authorization.

## Goal

Extract atomic events from fixture source content through real Python inference, with backend validation and human review.

## Dependencies and requirements

- Dependency: 003 verified and owner-accepted; 004 design approved.
- Coverage: FR-02, FR-04, FR-07; AC-01, AC-02, AC-08, AC-09.
- Authority: [Product Goal](../../../docs/product/goal.md), [roadmap](../../README.md), and [execution policy](../../policies/execution.md).

## Review and exit gate

Review the [checklist](checklist.md), resolve relevant decisions, and approve exact task scopes/checks at a Git revision before dispatch. Tasks may be prepared while BLOCKED; file existence is not authorization. A build alone does not establish completion.

Stop at this milestone boundary for owner review. 001/002 bootstrap uses explicitly assigned setup work until independent Runner verification exists.

## Exclusions

Python has no database/Jira credentials; no mapping approval or investigation synthesis yet.

## Session and context rules

One task is one fresh session and one cohesive, independently testable outcome. Follow [execution policy](../../policies/execution.md#session-context-and-task-sizing). Starting context target: 10,000-30,000 tokens; ceiling: strictly below 100,000 tokens including supplied instructions, task, selected references and dependency handoffs. This is not a guaranteed total-session token cap. Split oversized work before dispatch. Update these canonical files directly; Git retains history.
