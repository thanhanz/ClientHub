# 003 — Backend foundation and fake ingestion

Status: DRAFT — pending milestone review; not execution authorization.

## Goal

Persist authorized project sources using scenario-backed source ingestion and expose a read-only fake Jira adapter.

## Dependencies and requirements

- Dependency: 002 verified and owner-accepted; 003 design approved.
- Coverage: FR-01; project isolation and adapter prerequisites for AC-01–12.
- Authority: [Product Goal](../../../docs/product/goal.md), [roadmap](../../README.md), and [execution policy](../../policies/execution.md).

## Review and exit gate

Review the [design checklist](design-checklist.md), then approve the [implementation checklist](implementation-checklist.md) and task-specific gates. Record owner approval against a specification revision before issuing executable tasks. All required deliverables need evidence; no successful build or checked box alone establishes completion.

Stop at this milestone boundary for owner review. 001/002 bootstrap uses explicitly assigned setup work until independent Runner verification exists.

## Exclusions

No live email/chat/Jira connectors, real AI integration, polling, or custom UI.
