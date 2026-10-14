# Architecture documentation — ClientHub

> Status: **REVIEW CANDIDATE** (2026-10-14). This package is written as a coherent implementation baseline; the project owner must approve the technical choices and `design-foundation/checklist.md` before a coding runner treats them as frozen.

## Authority and change control

1. `../product/goal.md` owns **product requirements, scope, non-goals and acceptance criteria**. The handoff v2 is historical decision evidence; the Product Goal deliberately remains marked proposed until owner review.
2. `decisions.md` records technical choices, rationale, status and explicitly open questions; `tech-stack.md` describes proposed baseline versions and code layout.
3. `system-design.md` owns component **responsibilities, trust boundaries and runtime topology**.
4. `workflows.md` owns process/state transitions, triggering and failure handling.
5. `erd.md` owns proposed persisted data model, integrity constraints and history semantics.
6. `../contracts/` owns **exact interoperable payloads, statuses, endpoint semantics and versioning**. If text examples and machine-readable schemas disagree, implementation is blocked pending correction; neither silently overrides the other.
7. Harness milestones/tasks are downstream implementation plans; they cannot override (1)–(6).

All draft technical decisions are **PROPOSED**, not automatically approved. An agent must not resolve contradictions by inventing product requirements. Any material change requires an architecture decision record, updating impacted contracts/workflows/ERD and regression cases before implementation.

## Reading routes

| Work item | Minimum reading set |
| --- | --- |
| Database migration | `erd.md`, `../contracts/domain-contracts.md`, relevant product invariants |
| API endpoint | `../contracts/api-contracts.md`, `domain-contracts.md`, `workflows.md` section |
| Mock Jira adapter | `../contracts/provider-contracts.md`, `system-design.md` trust boundaries |
| Investigator bundle | `../contracts/ai-contracts.md`, `../contracts/schemas/context-bundle.schema.json`, `workflows.md` |
| Authorization | `system-design.md`, `../contracts/api-contracts.md`, `erd.md` |
| Coding agent | Assigned task + relevant sources above; do not load the entire design by default |

## Backend foundation target

The **first implementation milestone** is a deterministic, mock-first vertical slice:

`seeded permitted sources/events -> stored source provenance -> reviewed mapping -> authorized mock Jira retrieval -> bounded evidence context bundle`.

It does **not** require a Python service, real provider credentials, live Jira, vector search, or a frontend. `backend-foundation/goal.md` defines the narrower completion gate.

## Design review flags

- Explicitly confirm whether authenticated test identities are sufficient for the first milestone and when production identity integration begins.
- Explicitly approve PostgreSQL + EF Core as the initial persistence baseline.
- Confirm configurable retrieval limits and their failure semantics before performance/production claims.
- Validate wire contracts against mock scenarios; later validate provider interfaces against Jira sandbox behavior (not only mocks).
