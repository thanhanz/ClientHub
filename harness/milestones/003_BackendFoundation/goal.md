# 003 — Backend foundation and fake ingestion

Status: DRAFT — pending milestone review; not execution authorization.

## Goal

Persist authorized project sources using scenario-backed source ingestion and expose a read-only fake Jira adapter.

## Dependencies and requirements

- Dependency: 002 verified and owner-accepted; 003 design approved.
- Coverage: FR-01; project isolation and adapter prerequisites for AC-01–12.
- Authority: [Product Goal](../../../docs/product/goal.md), [roadmap](../../README.md), and [execution policy](../../policies/execution.md).

## Review and exit gate

Review the [checklist](checklist.md), resolve relevant decisions, and approve exact task scopes/checks at a Git revision before dispatch. Tasks may be prepared while BLOCKED; file existence is not authorization. A build alone does not establish completion.

Stop at this milestone boundary for owner review. 001/002 bootstrap uses explicitly assigned setup work until independent Runner verification exists.

## Exclusions

No live email/chat/Jira connectors, real AI integration, polling, or custom UI.

## Session and context rules

One task is one fresh session and one cohesive, independently testable outcome. Follow [execution policy](../../policies/execution.md#session-context-and-task-sizing). Starting context target: 10,000-30,000 tokens; ceiling: strictly below 100,000 tokens including supplied instructions, task, selected references and dependency handoffs. This is not a guaranteed total-session token cap. Split oversized work before dispatch. Update these canonical files directly; Git retains history.

## Contracts and readiness

Read the [checklist](checklist.md) and [execution policy](../../policies/execution.md) with the assigned task. Scope is FR-01, authorized persistent sources, and separate scenario-source/read-only Jira adapters. AC-01–12 receive prerequisites here, not complete acceptance implementation.

Relevant specifications:

- [Product Goal](../../../docs/product/goal.md) §§5 FR-01, 6–9, 12.
- [Domain contracts](../../../docs/contracts/domain-contracts.md) §§1, 2, 5–7: composite identity, enums, UTC, roles, retention and isolation.
- [API contracts](../../../docs/contracts/api-contracts.md) §§1–4: only health and source endpoints belong to 003; §5 API-01–03 are applicable source gates.
- [Provider contracts](../../../docs/contracts/provider-contracts.md) §§1–5: source/Jira ports, explicit links, failure signals and PR-01–10; bounded excerpts in the final §6 protect downstream compatibility but do not authorize 006 context assembly.
- [Source schema](../../../docs/contracts/schemas/source.schema.json): wire version 1.0; it is a response object, not a complete intake/page schema.
- [ERD](../../../docs/architecture/erd.md) §§1, 3, milestone allocation: projects, memberships and sources only; no Jira mirror.
- [Decisions](../../../docs/architecture/decisions.md), [technology baseline](../../../docs/architecture/tech-stack.md), [workflows](../../../docs/architecture/workflows.md) WF-01 and milestone allocation.
- [Scenario inputs](../../../docs/scenarios/fixture-inputs.md), [scenario index](../../../docs/scenarios/README.md), and separate [expected outcomes](../../../docs/scenarios/expected-outcomes.md).
- [001 review](../001_DesignFoundation/goal.md): DF-001-R2 is a pending candidate, including unresolved DF-01–11 and previously failed environment checks. Preserve existing working-tree changes; they are not approval evidence.

Every executable task requires 002 independently verified and owner-accepted, 003 goal/design/task scope and gates approved, and prerequisite contracts frozen against an exact revision. Approval and prerequisite evidence remain pending. Wire `schema_version=1.0` alone does not identify an approved specification revision. The Runner must supply the approved revision and verified dependency summary for each session; missing or incompatible evidence stops execution.

## Decisions required before executable task issuance

These are unresolved decisions, not implementation choices. Resolve them in separately authorized canonical-document planning work; this file does not grant permission to edit those documents.

| Gap | Required decision/evidence | Affected tasks |
| --- | --- | --- |
| G1 — approval and harness prerequisites | Resolve DF-01; obtain 001 acceptance, 002 verification/owner acceptance, and revision-bound 003 review. Use canonical Markdown tasks, approved check commands, no automatic retries, and the clean-workspace/manual-continuation policy from completed 002. | All |
| G2 — persistence/runtime | Approve or replace proposed ADR-004/005/011: runtime, database, ORM, pinned compatible dependencies, migration/startup and isolated-test provisioning. Define minimal project/membership/source columns, lengths, keys, indexes and transactions. Do not assume PostgreSQL/EF/Compose is approved. | P02–P08 |
| G3 — identity and provisioning | Approve guarded fixture identity and trusted actor/role resolution, project/membership provisioning, source ACL policy and Production rejection of test identity. Production identity provider can remain deferred only with an explicit demo boundary. API §4 already fixes inaccessible-project 404 and forbidden-operation 403. | P01, P03–P08 |
| G4 — source contracts | Resolve DF-03: preserve DATE/UNKNOWN precision end to end and define normalization. Specify intake, duplicate response, list page/cursor DTOs, numeric limits, order, timestamp ownership (fixture ingestion vs actual import), ID encoding, verified actor metadata and content-policy rejection vs stripping. Schema does not structurally enforce all retention combinations. | P01–P06, P08 |
| G5 — provider envelopes | Resolve DF-04: exact ports/types, missing/forbidden/transient/invalid signals, stale/partial/coverage representation, deterministic cursor/snapshot and search semantics, field visibility and link-direction interpretation. Avoid ambiguous duplicate §6 references. Decide timeout/cancellation behavior; do not add retries without policy. | P01, P05, P07–P08 |
| G6 — fixture lifecycle | Approve scenario revision, runtime fixture location/format, actor/project alias-to-UUID mapping, loading/reset mechanism, environment guard, clock handling, negative variants and test-only expectations. Reset must be restricted to a named isolated demo/test store. | P05–P08 |
| G7 — health and verification | Define readiness authorization and DB/provider criteria, failure disclosure, exact focused check commands, discovery counts, migration/fixture smoke commands, dependency prerequisites and earlier regression gates. Fix or explicitly resolve previously reported Python validator/.NET restore failures before relying on checks. | P02–P08 |

Production connectors, real Jira sandbox proof, jobs/outbox, production retention administration and AI decisions are deferred. DF-06–11 investigation/AI decisions do not authorize work in 003. Only their source/provider compatibility implications must be settled here.
