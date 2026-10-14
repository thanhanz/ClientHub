# 003 — Proposed task breakdown

Status: PROPOSAL FOR REVIEW, 2026-10-15. Documentation only; no execution authorization, task verification, or approval is recorded here. The user explicitly requested this proposal before milestone approval. This file is outside `tasks/`, which the [roadmap](../../README.md) reserves for approved executable scopes.

## Authority and entry gates

Read the [goal](goal.md), [design checklist](design-checklist.md), [implementation checklist](implementation-checklist.md), and [execution policy](../../policies/execution.md) together. Scope is FR-01, authorized persistent sources, and separate scenario-source/read-only Jira adapters. AC-01–12 receive prerequisites here, not complete acceptance implementation.

Relevant specifications:

- [Product Goal](../../../docs/product/goal.md) §§5 FR-01, 6–9, 12.
- [Domain contracts](../../../docs/contracts/domain-contracts.md) §§1, 2, 5–7: composite identity, enums, UTC, roles, retention and isolation.
- [API contracts](../../../docs/contracts/api-contracts.md) §§1–4: only health and source endpoints belong to 003; §5 API-01–03 are applicable source gates.
- [Provider contracts](../../../docs/contracts/provider-contracts.md) §§1–5: source/Jira ports, explicit links, failure signals and PR-01–10; bounded excerpts in the final §6 protect downstream compatibility but do not authorize 006 context assembly.
- [Source schema](../../../docs/contracts/schemas/source.schema.json): wire version 1.0; it is a response object, not a complete intake/page schema.
- [ERD](../../../docs/architecture/erd.md) §§1, 3, milestone allocation: projects, memberships and sources only; no Jira mirror.
- [Decisions](../../../docs/architecture/decisions.md), [technology baseline](../../../docs/architecture/tech-stack.md), [workflows](../../../docs/architecture/workflows.md) WF-01 and milestone allocation.
- [Scenario inputs](../../../docs/scenarios/fixture-inputs.md), [scenario index](../../../docs/scenarios/README.md), and separate [expected outcomes](../../../docs/scenarios/expected-outcomes.md).
- [001 review](../001_DesignFoundation/review.md): DF-001-R2 is a pending candidate, including unresolved DF-01–11 and previously failed environment checks. Preserve existing working-tree changes; they are not approval evidence.

Every executable task requires 002 independently verified and owner-accepted, 003 goal/design/task scope and gates approved, and prerequisite contracts frozen against an exact revision. No such evidence was supplied for this proposal. Wire `schema_version=1.0` alone does not identify an approved specification revision. The Runner must supply the approved revision and verified dependency summary for each session; missing or incompatible evidence stops execution.

## Decisions required before executable task issuance

These are gaps, not choices made by this proposal. Resolve them in separately authorized canonical-document planning work; this file does not grant permission to edit those documents.

| Gap | Required decision/evidence | Affected tasks |
| --- | --- | --- |
| G1 — approval and harness prerequisites | Resolve DF-01; obtain 001 acceptance, 002 verification/owner acceptance, and revision-bound 003 review. Select actual Runner task format, verification modes, retry/time limits and dirty-tree policy from completed 002. | All |
| G2 — persistence/runtime | Approve or replace proposed ADR-004/005/011: runtime, database, ORM, pinned compatible dependencies, migration/startup and isolated-test provisioning. Define minimal project/membership/source columns, lengths, keys, indexes and transactions. Do not assume PostgreSQL/EF/Compose is approved. | P02–P08 |
| G3 — identity and provisioning | Approve guarded fixture identity and trusted actor/role resolution, project/membership provisioning, source ACL policy and Production rejection of test identity. Production identity provider can remain deferred only with an explicit demo boundary. API §4 already fixes inaccessible-project 404 and forbidden-operation 403. | P01, P03–P08 |
| G4 — source contracts | Resolve DF-03: preserve DATE/UNKNOWN precision end to end and define normalization. Specify intake, duplicate response, list page/cursor DTOs, numeric limits, order, timestamp ownership (fixture ingestion vs actual import), ID encoding, verified actor metadata and content-policy rejection vs stripping. Schema does not structurally enforce all retention combinations. | P01–P06, P08 |
| G5 — provider envelopes | Resolve DF-04: exact ports/types, missing/forbidden/transient/invalid signals, stale/partial/coverage representation, deterministic cursor/snapshot and search semantics, field visibility and link-direction interpretation. Avoid ambiguous duplicate §6 references. Decide timeout/cancellation behavior; do not add retries without policy. | P01, P05, P07–P08 |
| G6 — fixture lifecycle | Approve scenario revision, runtime fixture location/format, actor/project alias-to-UUID mapping, loading/reset mechanism, environment guard, clock handling, negative variants and test-only expectations. Reset must be restricted to a named isolated demo/test store. | P05–P08 |
| G7 — health and verification | Define readiness authorization and DB/provider criteria, failure disclosure, exact focused check commands, discovery counts, migration/fixture smoke commands, dependency prerequisites and earlier regression gates. Fix or explicitly resolve previously reported Python validator/.NET restore failures before relying on checks. | P02–P08 |

Production connectors, real Jira sandbox proof, jobs/outbox, production retention administration and AI decisions are deferred. DF-06–11 investigation/AI decisions do not authorize work in 003. Only their source/provider compatibility implications must be settled here.

## Session and path rules

Each proposed ID below represents exactly one future session. Dependencies mean independently verified outputs at the approved revision, never an agent's `IMPLEMENTED` report. IDs and layouts are proposals; the Runner must materialize one approved task file with exact commands after decisions close.

Allowed paths below are narrow proposed write allowlists, relative to repository root. Reads may inspect relevant prerequisites. `**` means descendants only; it does not authorize neighboring features. Shared files are enumerated explicitly. Final layout must be approved before execution; needing another file triggers a scope change, not an improvised expansion. Never write `harness/runs/**`, protected specifications, or another task's files.

For every session: read the assigned task/revision/dependency evidence; inspect `git status --short`; preserve unrelated changes; validate prerequisites; implement only that task and its focused tests; run prescribed gates and record exit codes; return the AGENTS.md handoff and end. Stop on missing decisions, incompatible interfaces, unauthorized paths, failed prerequisites, or repeated verification failures under 002 policy. Never weaken tests, mark tasks VERIFIED, start the next session, or advance milestones.

## Proposed sessions

### 003-P01 — Backend source/provider contract types

Goal: translate approved 003 contracts into C# types and read-only ports, without storage, endpoints or providers.

Dependencies: global entry gates; G3–G5 closed. Bind domain/API/provider/source-schema revisions and approved DTO decisions in the eventual task.

Allowed paths: `src/Hub.Api/Contracts/Sources/**`, `src/Hub.Api/Contracts/Providers/**`, `tests/Hub.Tests/Contracts/BackendFoundation/**`.

Acceptance: required composite source/Jira locators preserve project and instance identity; canonical enum spellings and snake_case/UUID/UTC/version semantics match approved contracts; source precision and actor provenance survive serialization; failure/page/coverage types match approved envelopes; Jira ports expose no write operations. Source and problem response compatibility checks pass. No events/mappings/AI or new packages unless separately scoped.

Focused gate: proposed filter `FullyQualifiedName~BackendFoundationContracts`; exact serialization/schema command and nonzero discovered tests must be approved. Stop if translating a contract requires choosing missing behavior.

### 003-P02 — Minimal isolated persistence

Goal: add project, membership and source storage plus explicit migrations against the chosen database.

Dependencies: P01; G2, G4, G7 closed. Bind approved minimal schema and test-database lifecycle.

Allowed paths: `src/Hub.Api/Infrastructure/Persistence/**`, `src/Hub.Api/Features/Projects/Models/**`, `src/Hub.Api/Features/Sources/Models/**`, `src/Hub.Api/Hub.Api.csproj`, `tests/Hub.Tests/Hub.Tests.csproj`, `tests/Hub.Tests/Integration/BackendFoundation/Persistence/**`.

Acceptance: clean isolated database can migrate; repeat migration is safe; data survives a fresh application/database connection; membership uniqueness, ownership FK and composite source uniqueness are enforced; occurrence/import/observation times and permitted precision/content persist; independent projects can use otherwise identical provider IDs. Concurrent duplicate insert cannot produce two records. No event, mapping, review-audit or Jira-mirror tables.

Focused gate: proposed filter `FullyQualifiedName~BackendFoundationPersistence`, using the approved real database rather than an in-memory substitute; migration command is pending G2/G7. Stop if schema or provisioning needs an unapproved infrastructure path.

### 003-P03 — Guarded identity and project/source authorization

Goal: implement trusted fixture principal resolution and reusable backend membership/role/source access services.

Dependencies: P01, P02; G3 closed.

Allowed paths: `src/Hub.Api/Infrastructure/Security/**`, `src/Hub.Api/Features/Projects/Authorization/**`, `src/Hub.Api/Features/Sources/Authorization/**`, `src/Hub.Api/Program.cs`, `tests/Hub.Tests/Integration/BackendFoundation/Authorization/**`.

Acceptance: Test/Development fixture identity works only under approved guards; Production cannot activate it; caller headers/body cannot grant actor identity, role or membership. Nonmember access is denied before protected reads; MEMBER may read accessible PROJECT_MEMBERS sources but cannot mutate; PO_PM_ONLY reads are denied to MEMBER. Cross-project locators fail safely. Test principals cover PO_PM, MEMBER, outsider and unauthenticated access. Future investigation permission can reuse this service; do not create investigation endpoints.

Focused gate: proposed filter `FullyQualifiedName~BackendFoundationAuthorization`. Stop on unspecified identity provisioning or ACL behavior.

### 003-P04 — Authorized source ingestion service

Goal: implement normalized intake behind an application interface, including immutable duplicate behavior and retention validation.

Dependencies: P01–P03; G4 closed.

Allowed paths: `src/Hub.Api/Features/Sources/Ingestion/**`, `src/Hub.Api/Infrastructure/Persistence/SourceRepository.cs`, `tests/Hub.Tests/Integration/BackendFoundation/Ingestion/**`.

Acceptance: PO_PM intake persists required provenance and available actor/time metadata; stable composite identity is mandatory; repeat and changed-content imports return the existing ID/content/metadata/timestamps unchanged; concurrent duplicates return one stored record. Unauthorized, malformed, invalid-project, invalid-time and prohibited-retention imports leave no new record. METADATA_ONLY stores no body; APPROVED_NOTES stores only approved notes; meeting evidence never gains fabricated transcript/speaker detail. Transaction boundaries and duplicate validation order follow the approved decision. No extraction, jobs, ID-less intake or general idempotency-key store.

Focused gate: proposed filter `FullyQualifiedName~BackendFoundationIngestion`, including DB-01 and V-DUPLICATE. Stop if rejection/deduplication ordering or content handling is unresolved.

### 003-P05 — Scenario source reader and fixture intake

Goal: provide deterministic runtime source fixtures through the approved source-reader port and existing authorized ingestion service.

Dependencies: P01, P03, P04; G5–G6 closed.

Allowed paths: `src/Hub.Api/Infrastructure/ExternalSources/**`, `src/Hub.Api/Fixtures/Sources/**`, `src/Hub.Api/Program.cs`, `tests/Hub.Tests/ContractTests/ExternalSources/**`, `tests/Hub.Tests/Fixtures/SourceExpectations/**`.

Acceptance: Google Login, Sales Export and Discount inputs preserve external IDs, project, actor metadata, occurrence/import conventions, approved meeting notes and D-03 DATE precision. Loading twice is repeatable through P04; adapters neither write persistent entities directly nor bypass authorization. Deterministic paging yields no missing/duplicate items in a snapshot. Missing/forbidden/invalid/timeout behavior uses approved signals. Runtime assets never contain expected extracted events, mapping decisions or findings. Reusable source contract suite covers PR-04/06/07/08/09 where applicable.

Focused gate: proposed filter `FullyQualifiedName~ExternalSourceContract`; expectation assets remain test-only. Stop if scenario input revision or loading/reset entry point is unapproved.

### 003-P06 — Source HTTP API and health endpoints

Goal: expose only the approved source list/intake and liveness/readiness routes with dependency injection.

Dependencies: P02–P05; G4, G7 closed.

Allowed paths: `src/Hub.Api/Features/Sources/Endpoints/**`, `src/Hub.Api/Features/Health/**`, `src/Hub.Api/Program.cs`, `tests/Hub.Tests/Integration/BackendFoundation/SourceApi/**`.

Acceptance: new intake returns 201 and duplicate returns 200 with approved deduplication response; list filters source ACLs before disclosure/paging and respects approved numeric bounds/order/cursor. API-01–03 pass; UUID, source refs, UTC, schema_version and safe ProblemDetails match contracts; 401/404/403 and 400/422 behavior follows API §4. Forged caller identity or project payload cannot bypass URL/principal checks. Health routes follow approved readiness policy and return 503 for specified dependency failures without sensitive details. No later-milestone routes.

Focused gate: proposed filter `FullyQualifiedName~BackendFoundationSourceApi`, with response schema validation. Stop if intake/page wire shapes or readiness policy are incomplete.

### 003-P07 — Read-only fake Jira reader and reusable contract suite

Goal: implement the separate Jira port using versioned runtime fixtures and capability-aware adapter tests.

Dependencies: P01, P03; G5–G6 closed. P05 is not a dependency; shared runtime wiring remains serialized by the Runner.

Allowed paths: `src/Hub.Api/Infrastructure/Jira/**`, `src/Hub.Api/Fixtures/Jira/**`, `src/Hub.Api/Program.cs`, `tests/Hub.Tests/ContractTests/Jira/**`, `tests/Hub.Tests/Fixtures/JiraExpectations/**`.

Acceptance: PR-01–05/08/09 pass for lookup, search, paging, explicit direction and unknown optional fields; applicable PR-10 suite is reusable, but real-adapter runs are NOT_RUN/deferred. AUTH-101 is discoverable without Hub mappings and is explicitly BLOCKED_BY AUTH-102; AUTH-103 sharing an assignee creates no dependency. Composite instance/project filtering, unauthorized project/link targets, missing/forbidden/timeout, stale/partial observations and cyclic-link fixtures preserve approved semantics. No writes, Jira mirror, graph traversal orchestration or LLM. Freshness is preserved, not relabeled current; authorized optional evidence remains available for later 006 without implementing bundles.

Focused gate: proposed filter `FullyQualifiedName~JiraAdapterContract`. Stop on missing page/failure/direction/search policy; do not choose a traversal budget for 006.

### 003-P08 — Reproducible startup and milestone evidence

Goal: assemble the already implemented components into a clean-store smoke/regression gate and document evidence for owner review.

Dependencies: P01–P07 independently verified; G6–G7 closed; 002's actual verify interface available.

Allowed paths: `scripts/verify.ps1`, `scripts/backend-foundation-smoke.ps1`, `tests/Hub.Tests/Acceptance/BackendFoundation/**`, `harness/milestones/003_BackendFoundation/evidence-summary.md`. If approved provisioning requires Compose, config, Dockerfile or CI edits, name those exact files in the executable task before issuance; none is implicitly allowed here.

Acceptance: fresh isolated store migrates and starts; runtime fixture loading twice yields unchanged existing sources; HTTP role/source isolation and provider contract suites pass together; readiness failure is observable; runtime fixtures remain separate from expectations. Verification discovers and runs all required tests, includes earlier applicable regression gates, records actual commands/exit codes and tested revision, and fails rather than silently skipping unavailable checks. Evidence summary distinguishes implementation, local checks, independent Runner evidence and pending owner acceptance. Do not create Runner evidence/checkpoints or record owner approval on the owner's behalf.

Focused gate: full build/test, schema validator, approved migration/fixture/API smoke and 002 regression modes. Stop after evidence handoff for owner review; no 004 execution.

## Verification command proposals and release conditions

Existing fallback commands to bind into future tasks where applicable:

```powershell
dotnet build ClientHub.slnx
dotnet test tests/Hub.Tests/Hub.Tests.csproj --filter "FullyQualifiedName~BackendFoundationContracts"
dotnet test tests/Hub.Tests/Hub.Tests.csproj --filter "FullyQualifiedName~BackendFoundationPersistence"
dotnet test tests/Hub.Tests/Hub.Tests.csproj --filter "FullyQualifiedName~BackendFoundationAuthorization"
dotnet test tests/Hub.Tests/Hub.Tests.csproj --filter "FullyQualifiedName~BackendFoundationIngestion"
dotnet test tests/Hub.Tests/Hub.Tests.csproj --filter "FullyQualifiedName~ExternalSourceContract"
dotnet test tests/Hub.Tests/Hub.Tests.csproj --filter "FullyQualifiedName~BackendFoundationSourceApi"
dotnet test tests/Hub.Tests/Hub.Tests.csproj --filter "FullyQualifiedName~JiraAdapterContract"
dotnet test tests/Hub.Tests/Hub.Tests.csproj
python scripts/validate-contracts.py
```

These filters are proposed names, not existing runnable acceptance suites. Before release, approve real test names and positive discovery counts; exit 0 with zero tests does not pass. `scripts/verify.ps1` is currently absent; use its task-appropriate modes once 002 supplies them. Exact database lifecycle, fixture load/reset, startup/API smoke and earlier regression commands remain BLOCKED on G1/G2/G6/G7; do not invent switches or claim this proposal is executable. Schema checks supplement semantic authorization/retention checks, not replace them. Previously reported environment failures are historical, not fresh results from this planning session.

Dependency graph: entry gates → P01 → P02 → P03 → P04 → P05 → P06; P01 + P03 → P07; P01–P07 → P08. This graph is planning only, not a schedule or Runner state.

Before any executable session, the Runner/owner must replace pending decisions with revision-bound approvals, finalize allowed paths and exact checks, then issue one task. No checkbox or proposal ID authorizes execution.

## Required handoff for every future session

```text
TASK_ID:
RESULT: IMPLEMENTED | BLOCKED | FAILED
CHANGED_FILES: [paths from the actual diff for this task; distinguish pre-existing changes]
CONTRACTS_EXPORTED_OR_CHANGED: [types, endpoints, schemas, or none]
TESTS_RUN: [exact commands, exit codes, and PASS/FAIL/NOT_RUN]
KNOWN_ISSUES: [issues or none]
DOWNSTREAM_NOTES: [interfaces, prerequisites, deferred work]
```

End the session after this handoff. IMPLEMENTED is not VERIFIED. Only the external Runner may independently verify the tested tree and update authoritative state; owner review is still required at the milestone boundary.
