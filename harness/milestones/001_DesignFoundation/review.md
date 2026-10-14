# 001 DesignFoundation review — DF-001-R2

Date: 2026-10-15. Status: REVIEW CANDIDATE; no owner approval or independent verification recorded. Authorized scope: complete scenario specifications and review remaining design gaps; milestone 001 and supporting documentation only. No milestone 002 implementation or executable task authorization.

## Revision and delivered evidence

Base commit: `08777edd056cf17c0ba3bad56f550720efc5a8ab`. Proposed working-tree revision: **DF-001-R2**. The adjacent [revision manifest](revision-manifest.json) binds the review candidate to SHA-256 hashes of the complete milestone-001/scenario/architecture/contract/product/policy/roadmap documentation set and existing contract-check script. Its manifest hash is presented in the handoff. The manifest is an optional review aid, not a policy requirement. Approval may identify this candidate by manifest hash or an exact committed revision; any subsequent specification edit requires renewed review of the affected revision. This manifest is documentation, not Runner state or a verified checkpoint.

Deliverables: [concrete runtime inputs](../../../docs/scenarios/fixture-inputs.md), [separate outcomes and AC-01–12 allocation](../../../docs/scenarios/expected-outcomes.md), and updated [scenario index](../../../docs/scenarios/README.md). Scenarios specify source text, verified actor metadata, timestamps/precision, memberships, Jira fields/excerpts/directed links, questions, and isolated negative variants. Future test doubles and annotation rubrics are distinct from runtime provider input.

The design checklist now records an agent document review: 14 of 25 items checked with section evidence and open findings. Five of six deliverable inventory items are checked. Owner approval, incomplete definitions, runtime confirmation, passing validation, and resolution of blocking findings remain unchecked. Existing owner-approved 2026-10-14 rules are preserved; product goals, schemas, architecture decisions, and Runner state are unchanged.

## Remaining decisions for owner review

These are findings/proposals, not contract amendments. Approving scenarios alone does not resolve them. Each decision needs a recorded choice and updated canonical contract before dependent executable tasks.

| ID | Evidence / gap | Proposed resolution for review | Blocks / deferral |
| --- | --- | --- | --- |
| DF-01 | Product Goal remains proposed and references an unavailable architecture handoff | Approve the current Product Goal explicitly and formally supersede the missing handoff, or supply it and reconcile differences | 001 sign-off; all dependent milestone approvals |
| DF-02 | ADR-004–011 and technology baseline remain proposed, despite approved semantic revision rules | Approve/revise each separately: .NET modular monolith, PostgreSQL/EF, mock Jira port, code-controlled orchestration, synchronous demo operations, guarded test identity, deterministic search, Compose | Persistence/auth/provider choices before 003; no silent framework adoption |
| DF-03 | Source schema permits but does not require occurred_at_precision; provider required fields and source ERD omit it, so date-only precision can be lost before extraction | Require/preserve source occurrence precision in normalized input and persistence, including DATE UTC normalization; explicitly define UNKNOWN occurrence handling before freezing v1 | 003 source contract freeze and 004 extraction; D-03 exposes this gap |
| DF-04 | Provider contracts describe freshness, partial results and errors, but return signatures do not define complete page/coverage/error envelopes; duplicate §6 headings are ambiguous | Define DTOs, cursor/snapshot semantics, field availability and timeout/error envelopes; distinguish not-found from denied and absent fields from empty collections; renumber sections when canonical contract edits are authorized | 003 provider contract freeze; 006 partial-context policy |
| DF-05 | ERD calls for same-project constraints “where feasible” and nonempty provenance; exact relational enforcement and retention cleanup are not fixed | Specify composite keys/FKs and transaction checks; reject approved-event edits initially; define cleanup of derived summaries and stored investigations when evidence access/content changes | 003 DB design, 004 provenance/history, 006 persisted result access; organization retention durations may remain deferred to real integration |
| DF-06 | Investigation snapshots/results and audit are described, but persistence entity, retained payload, access revalidation and failure transaction boundaries are incomplete | Approve minimal result/audit persistence schema, permitted retention, request/result association, and revalidation on later reads; never retain forbidden evidence via audit | 006; not needed to implement 003 source intake |
| DF-07 | Backend budgets are proposed; traversal relevance/ranking, retries and partial-vs-error behavior are not exact | Approve demo defaults 2/10/12; count every provider attempt/page; use visited locators; approve deterministic ranking and stable pagination; choose no automatic demo retries or an explicit bounded policy and safe partial-result rules | 005 candidate discovery; 006 bounded retrieval; V-BOUNDS intentionally does not dictate a call sequence |
| DF-08 | Freshness timestamps exist, but stale thresholds/conflict handling and semantic claim rejection/repair authority remain unspecified | Attribute historical Jira observations without labeling them current; disclose discrepancies; define thresholds and reject unsupported high-risk FACT claims rather than publish; decide validation failure response without unbounded AI repair | 006, real synthesis evaluation |
| DF-09 | API inventory lacks an exact synthesis endpoint request/response entry and event manual-review policy is less strict than the extraction default | Complete synthesis route contract and request schemas; explicitly choose whether manual creation can atomically approve with authorized audit or must always enter PENDING_REVIEW | 004 manual event creation; 006 synthesis |
| DF-10 | No quantitative real-AI gate or frozen annotation rubric; scenario statements can support multiple atomic representations | Approve allowed enum/annotation alternatives, model/configuration, repetitions, dataset, precision/support thresholds and failure criteria; require no critical isolation/false-commitment cases in this selected suite | 004/005/006 AI gates; these three synthetic demos alone do not establish production quality |
| DF-11 | Service authentication, token/time limits and safe prompt diagnostics are still TBD | Specify private backend-to-Python credentials, cancellation/timeout/token budgets and logging policy before inference; production identity, real Jira credentials/visibility and connectors require later sandbox decisions | 004 inference security; production provisioning/connector details deferred to real integration |

Existing decisions already resolve PO_PM vs MEMBER permissions, nonempty event provenance, immutable duplicate imports, unique mappings across all states, terminal mapping review, and approved-event/confirmed-association synthesis eligibility. Do not reopen these as blank design questions. API §4 already chooses non-disclosing 404 for inaccessible projects and 403 for forbidden operations in accessible projects; workflows should refer to it rather than offer an independent policy choice.

## Available checks and actual results

Initial `git status --short`: exit 0, clean tree before edits. Repository inventory: `scripts/verify.ps1` absent; existing solution/test projects and `scripts/validate-contracts.py` available.

The primary shell tool stopped starting processes (`helper_unknown_error: setup refresh had errors`). Checks below were executed through the available Node execution tool. That process uses a different sandbox identity; Git required a per-command `-c safe.directory=D:/SelfProject/Dotnet/ClientHub` override, without changing global configuration.

| Exact command | Actual result |
| --- | --- |
| `python scripts/validate-contracts.py` | FAIL, exit 1 before validation: installed `referencing` calls `TypeVar(default=Any)` under Python 3.12; `TypeError: 'default' is an invalid keyword argument for typevar()` |
| `dotnet build ClientHub.slnx` | FAIL, exit 1 during NuGet restore: `Value cannot be null. (Parameter 'path1')` for both projects; no successful compilation |
| `dotnet test tests/Hub.Tests/Hub.Tests.csproj` | FAIL, exit 1 during the same restore error; no tests executed |
| `scripts/verify.ps1` | NOT_RUN: absent |
| `git -c safe.directory=D:/SelfProject/Dotnet/ClientHub diff --check` | PASS, exit 0; tracked diff whitespace only, not semantic/acceptance verification |

Supplementary Node filesystem checks inspect relative Markdown link targets in the six edited/new Markdown files (22 targets) and compare every manifest file's bytes with its recorded SHA-256. The first link scan identified the not-yet-created manifest; the final scan is performed after manifest generation. These are local documentation integrity checks, not Runner gates. Untracked new Markdown files are also inspected for trailing whitespace/conflict markers separately because `git diff --check` does not include them.

No dependencies, project configuration, acceptance tests, or infrastructure were altered to repair environment failures outside this documentation task. Future scenario tests and real AI evaluations are NOT_RUN: fixtures are specifications only. These failures leave verification pending; they are not evidence of defective scenario semantics or a passed milestone.

## Owner approval record (pending)

Required by [execution policy](../../policies/execution.md): approval must identify milestone, specification revision, scope/gates, approver and date. The user explicitly requested approval review at this boundary.

- Approver/date: pending.
- Approved revision (manifest SHA-256 or exact Git commit): pending.
- Scenario revision approved/revised: pending.
- DF-01–11 decisions and conditions: pending; do not treat silence as acceptance.
- Milestone readiness decision: pending; blocked dependencies above require resolution or explicit bounded deferral before affected tasks.

Stop here. Approval of this documentation revision does not authorize milestone 002 implementation, independently verify milestone 001, or allow a coding agent to update Runner checkpoints.

## Checklist review follow-up — 2026-10-15

The owner requested the agent to review and check the checklist for delivery. This authorizes recording completed document review, not inventing approvals or marking failed gates as passed. Reviewed scenario text and outcomes, domain states and permissions, architecture/ERD ownership and provenance, workflows, provider/AI interfaces, technology status, and acceptance traceability. Each checked design item cites exact sections; findings stay open even where document review is complete.

Delivery decision: suitable as a review candidate; milestone readiness BLOCKED by unresolved DF-01–11 and failed contract validation. Fake-provider application workflow execution, Python-free backend/context execution, and real AI evaluations are future gates with no runtime evidence here. The prior build/test failures remain unresolved; those commands were not rerun because this follow-up changes only review documentation.

Follow-up commands: `python scripts/validate-contracts.py` FAIL, exit 1, same Python TypeVar dependency error before validation; `git -c safe.directory=D:/SelfProject/Dotnet/ClientHub diff --check` and local documentation/hash checks are recorded in the final handoff. No application code, schemas, policies, milestone 002, or Runner state changed. Existing working-tree changes from the scenario-specification task were preserved.
