# 006 — Evidence-backed investigation

Status: DRAFT — pending milestone review; not execution authorization.

## Goal

Generate validated investigations using authorized events, bounded fake Jira retrieval, and real AI synthesis.

## Dependencies and requirements

- Dependency: 005 verified and owner-accepted; 006 design approved.
- Coverage: FR-04–07; AC-05, AC-10, AC-11, AC-12.
- Authority: [Product Goal](../../../docs/product/goal.md), [roadmap](../../README.md), and [execution policy](../../policies/execution.md).

## Review and exit gate

Review the [checklist](checklist.md), resolve relevant decisions, and approve exact task scopes/checks at a Git revision before dispatch. Tasks may be prepared while BLOCKED; file existence is not authorization. A build alone does not establish completion.

Stop at this milestone boundary for owner review. 001/002 bootstrap uses explicitly assigned setup work until independent Runner verification exists.

## Exclusions

No live Jira integration, unrestricted AI retrieval, or autonomous approval.

## Session and context rules

One task is one fresh session and one cohesive, independently testable outcome. Follow [execution policy](../../policies/execution.md#session-context-and-task-sizing). Starting context target: 10,000-30,000 tokens; ceiling: strictly below 100,000 tokens including supplied instructions, task, selected references and dependency handoffs. This is not a guaranteed total-session token cap. Split oversized work before dispatch. Update these canonical files directly; Git retains history.
