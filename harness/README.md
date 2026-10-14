# ClientHub milestone harness

Status: planning scaffold. No executable Runner or authoritative run state exists yet.

## Agreed MVP direction

Use scenario-backed fake communication sources and fake Jira behind separate backend interfaces. Real AI extraction, optional mapping adjudication, and investigation follow in later milestones. Start with Google Login, Sales Export deadline, and Discount scope change from [Product Goal §9.2](../docs/product/goal.md). Use API-based demonstrations; a custom UI is a separate scope decision.

The owner approved this roadmap direction on 2026-10-14. Individual milestone designs, technical choices, and execution gates remain subject to review. The Product Goal still has proposed status; this scaffold does not freeze it.

## Separate sources of truth

| Artifact | Responsibility | Authority |
|---|---|---|
| `docs/architecture/`, `docs/contracts/`, `docs/scenarios/` | Product design, interfaces, scenario inputs and expectations | Reviewed specifications; approval must be explicit |
| `milestones/<NNN_Name>/design-checklist.md` | Independently verifiable design review questions | Completed items cite document sections and review evidence |
| `milestones/<NNN_Name>/implementation-checklist.md` | Deliverables and acceptance evidence | Checked items cite implementation and independent verification; never schedule work |
| `milestones/<NNN_Name>/tasks/` | Approved executable task scope, dependencies, exact checks | Created only after milestone goal and design gates are approved |
| `runs/<run-id>/` | Attempts, verification evidence, resumable checkpoints | Generated and owned exclusively by the external Runner |

No checkbox is an execution authorization. An agent's `IMPLEMENTED` result is not Runner verification. Do not put task attempt statuses in design documents or use Markdown checklists as a work queue.

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

Review each milestone's goal and design checklist, settle its decisions, then approve its implementation checklist and executable tasks. Run only that milestone. Review its evidence before authorizing the next. Earlier checks remain regression gates.

001 is a documentation/review milestone. 002 is bootstrapped through explicitly assigned setup tasks until its Runner exists; neither requires invented Runner checkpoints. See [execution policy](policies/execution.md) and [scenario baseline](../docs/scenarios/README.md).

## Current limits

System design, ERD, workflows, and draft contracts now exist. The owner-approved revision scope is recorded in docs/architecture/decisions.md; unrelated technology choices and milestone gates still require their own review. The handoff referenced by the Product Goal is unavailable. The Runner, task files, exact verification commands, and run-state schema are not implemented. Existing build CI and the empty starter test do not establish product readiness.
