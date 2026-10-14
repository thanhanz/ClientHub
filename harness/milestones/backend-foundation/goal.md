# M1 — Backend Foundation Goal

> Status: PROPOSED / AWAITING D0 DESIGN REVIEW · Target: deterministic mock-first ASP.NET Core vertical slice. This milestone is a subset of `docs/product/goal.md` and does not redefine full MVP completion.

## Objective

Implement a reproducible, authorized backend that can persist project source metadata and business events, record/review many-to-many event–ticket mappings, read seeded Jira issues and **explicit** links, and return a bounded evidence context bundle with valid source refs. **No real AI service or real providers are required for this milestone.**

## In scope

1. ASP.NET Core modular backend, PostgreSQL/EF Core migrations and deterministic isolated seeds (if architecture baseline approved).
2. Verified actor identity via test-only scheme in guarded environments and project membership authorization.
3. Core entity persistence: projects, memberships, source metadata, events, source links, mapping links, review audit/history.
4. Manual/seeded structured events with correct occurrence date and approved source-level provenance.
5. Create/review mapping proposals with optimistic concurrency, audited authorization and separate business status.
6. Read-only `IJiraIssueReader` mock; issue-key/search/explicit links; bounded cycle-safe retrieval.
7. `POST /api/v1/projects/{project_id}/investigations/context` building `ContextBundle v1.0` without AI.
8. Unit and PostgreSQL-backed API integration tests, contract fixtures, Docker local/demo start and verification commands.

## Out of scope

LLM extraction, AI adjudication/synthesis, Python service calls, live Jira REST/MCP, Gmail/Slack/meeting integrations, OCR, full dashboard, graph DB/vector search, production identity provider, open-ended multi-agent orchestration.

## Non-negotiable acceptance gates

- **M1-AC01** Fresh DB migrations + idempotent seed on isolated PostgreSQL succeed.
- **M1-AC02** Project B resources cannot be read, mapped or linked by a Project A-only principal; source-level visibility enforced.
- **M1-AC03** Meeting metadata/approved notes work without stored transcript segments; no minute-level citation is fabricated.
- **M1-AC04** Unmapped events and Jira issues remain valid. Mapping relation is many-to-many.
- **M1-AC05** Proposal begins `PROPOSED`; authorized `CONFIRMED`/`REJECTED` review recorded with actor/time/version/audit; review does not alter business commitments.
- **M1-AC06** Google Login fixture retrieves explicitly linked OAuth blocker; Apple Login same-assignee context does not become a dependency.
- **M1-AC07** Event timeline is ordered by `occurred_at`, even after a late import.
- **M1-AC08** Investigation retrieval stops at configured depth/ticket/call limits; cycles and cross-project links terminate safely.
- **M1-AC09** Every context bundle evidence ref resolves within that same authorized bundle, with observed/freshness metadata and honest truncation.
- **M1-AC10** All relevant domain/API/provider/schema tests, integration tests and a fresh Docker smoke test pass; verifier records commands and actual results.

## Required design dependencies (before implementation)

- `docs/architecture/system-design.md`, `erd.md`, `workflows.md`, `decisions.md` reviewed for M1 scope.
- `docs/contracts/domain-contracts.md`, `provider-contracts.md`, `api-contracts.md`, `schemas/context-bundle.schema.json` accepted.
- `harness/milestones/design-foundation/checklist.md` signed or explicit approved conditions recorded.

## Completion evidence

Only a trusted external harness/CI can mark M1 VERIFIED using test output, no unauthorized file changes, stable migrations, contract validation and Git checkpoint. A coding session ending with exit code 0 is not sufficient evidence of correctness.
