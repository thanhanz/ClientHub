# 002 — Minimal harness

Status: DRAFT — pending milestone review; not execution authorization.

## Goal

Build the smallest external Runner that can execute and independently verify tasks within one approved milestone.

## Dependencies and requirements

- Dependency: 001 reviewed and accepted.
- Coverage: Execution scope, verification, interruption, resume, and milestone boundary.
- Authority: [Product Goal](../../../docs/product/goal.md), [roadmap](../../README.md), and [execution policy](../../policies/execution.md).

## Review and exit gate

Review the [design checklist](design-checklist.md), then approve the [implementation checklist](implementation-checklist.md) and task-specific gates. Record owner approval against a specification revision before issuing executable tasks. All required deliverables need evidence; no successful build or checked box alone establishes completion.

Stop at this milestone boundary for owner review. 001/002 bootstrap uses explicitly assigned setup work until independent Runner verification exists.

## Exclusions

No general workflow platform, distributed scheduler, or product feature work. Bootstrap with explicitly assigned setup tasks.
