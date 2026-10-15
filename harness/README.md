# ClientHub milestone harness

Status: planning scaffold. No executable Runner or authoritative run state exists yet.

## Agreed MVP direction

Use scenario-backed fake communication sources and fake Jira behind separate backend interfaces. Real AI extraction, optional mapping adjudication, and investigation follow in later milestones. Start with Google Login, Sales Export deadline, and Discount scope change from [Product Goal §9.2](../docs/product/goal.md). Use API-based demonstrations; a custom UI is a separate scope decision.

The owner approved this roadmap direction on 2026-10-14. Individual milestone designs, technical choices, and execution gates remain subject to review. The Product Goal still has proposed status; this scaffold does not freeze it.

## Current layout

Each milestone keeps one current `goal.md`, one `checklist.md`, and a `tasks/` directory. Edit these files directly; Git preserves earlier versions. Do not create parallel proposed/design/review copies.

| Artifact | Responsibility |
| --- | --- |
| `goal.md` | Outcome, scope, decisions, prerequisite contracts and acceptance criteria |
| `checklist.md` | Task index, unresolved decisions, acceptance evidence and owner approval record |
| `tasks/<NN-step>.md` | One session: objective, dependencies/context, allowed changes, implementation, exact checks, stop conditions and handoff |
| `docs/architecture/`, `docs/contracts/`, `docs/scenarios/` | Shared product specifications; link selected sections rather than copy them |
| `runs/<run-id>/` | Runner-generated local handoffs, logs, check results and commit checkpoints; ignored by Git |

Use the [task template](task-template.md) and [execution policy](policies/execution.md). Prepared tasks can be BLOCKED; dispatch requires explicit approval and satisfied prerequisites. The Runner uses the approved finite task list, never checklist order alone. Agents do not mark verification or edit Runner records. Checked document-review items in 001 retain their original limited meaning.

Starting context targets 10,000-30,000 tokens and must remain below 100,000. Supply the assigned task, selected contract sections, code entry points and verified dependency handoffs. This planning ceiling is not automatic total-session usage enforcement. Split oversized tasks before dispatch.

## Roadmap

Milestone directories use `NNN_Name`: a three-digit, one-based ID followed by a descriptive PascalCase name. Use the same ID in headings, dependencies, and review records. Numeric ordering defines the review sequence; execution still requires explicit milestone approval.

| Milestone | Goal | Dependency | Principal acceptance coverage |
|---|---|---|---|
| 001 | [Design and scenario baseline](milestones/001_DesignFoundation/goal.md) | None | Design coverage for AC-01–12 |
| 002 | [Minimal harness](milestones/002_HarnessFoundation/goal.md) | 001 reviewed and accepted | Scope, verification failure, interruption, resume, milestone stop |
| 003 | [Backend and fake ingestion](milestones/003_BackendFoundation/goal.md) | 002 verified and accepted | Isolation, repeatable imports, adapter contracts |
| 004 | [Extraction and review](milestones/004_EventExtraction/goal.md) | 003 verified and accepted | AC-01, AC-02, AC-08, AC-09 |
| 005 | [Mapping and review](milestones/005_EventMapping/goal.md) | 004 verified and accepted | AC-03, AC-04, AC-06, AC-07 |
| 006 | [Evidence-backed investigation](milestones/006_Investigation/goal.md) | 005 verified and accepted | AC-05, AC-10, AC-11, AC-12 |
| 007 | [Demo and regression](milestones/007_MvpValidation/goal.md) | 006 verified and accepted | All twelve cases and all three demos |

Review each milestone's goal and checklist, settle its decisions, then approve its exact task scopes and checks at a Git revision. Run only that milestone. Review its evidence before authorizing the next. Earlier checks remain regression gates.

001 is a documentation/review milestone. 002 is bootstrapped through explicitly assigned setup tasks until its Runner exists; neither requires invented Runner checkpoints. See [execution policy](policies/execution.md) and [scenario baseline](../docs/scenarios/README.md).

## Current limits

System design, ERD, workflows, and draft contracts now exist. The owner-approved revision scope is recorded in docs/architecture/decisions.md; unrelated technology choices and milestone gates still require their own review. The handoff referenced by the Product Goal is unavailable. The Runner is not implemented. Three 002 tasks and eight 003 tasks are prepared but BLOCKED pending approvals/prerequisites; 003 also has unresolved product decisions and check commands. Later milestones retain feature/acceptance checklists and empty task directories until their task contracts can be defined without inventing decisions. Existing build CI and the empty starter test do not establish product readiness.

## Next preparation step

Review 001's open findings and resolve or explicitly defer only the prerequisites appropriate to 002 bootstrap. Approve the 002 task scopes at the actual Git revision, then issue HF-002-01 as a separate session. No bootstrap deferral or milestone acceptance is granted by this restructure. Complete and independently check 002 before dispatching 003. Resolve 003 G1-G7 in canonical product contracts before approving affected tasks.
