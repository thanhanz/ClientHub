# 005 — Event–Jira mapping and review

Status: DRAFT — pending milestone review; not execution authorization.

## Goal

Discover fake Jira candidates and provide reviewable many-to-many event associations.

## Dependencies and requirements

- Dependency: 004 verified and owner-accepted; 005 design approved.
- Coverage: FR-03, FR-07; AC-03, AC-04, AC-06, AC-07.
- Authority: [Product Goal](../../../docs/product/goal.md), [roadmap](../../README.md), and [execution policy](../../policies/execution.md).

## Review and exit gate

Review the [checklist](checklist.md), resolve relevant decisions, and approve exact task scopes/checks at a Git revision before dispatch. Tasks may be prepared while BLOCKED; file existence is not authorization. A build alone does not establish completion.

Stop at this milestone boundary for owner review. 001/002 bootstrap uses explicitly assigned setup work until independent Runner verification exists.

## Exclusions

No Jira mutation, invented ticket dependencies, or automatic business approvals.

## Session and context rules

One task is one fresh session and one cohesive, independently testable outcome. Follow [execution policy](../../policies/execution.md#session-context-and-task-sizing). Starting context target: 10,000-30,000 tokens; ceiling: strictly below 100,000 tokens including supplied instructions, task, selected references and dependency handoffs. This is not a guaranteed total-session token cap. Split oversized work before dispatch. Update these canonical files directly; Git retains history.
