# Milestone review and execution policy

## Approval and specifications

The owner approves one milestone at a time. Approval evidence must identify the milestone, specification revision, approved task scope and gates, approver, and date. Store the approval record in the milestone checklist after approval; do not prepopulate an approval. Changes to approved requirements or gates require renewed review before dependent execution.

Each milestone has only goal.md, checklist.md and tasks/. The checklist indexes tasks and evidence; it is not the execution queue. Prepared BLOCKED tasks may exist before approval. Each future task must specify its ID, goal, dependencies, allowed paths, prerequisite contract versions, exact verification commands and expected assertions, and required handoff. A missing prerequisite blocks that task.

## Runner ownership

Only the external Runner creates or updates `harness/runs/<run-id>/state.json`, attempt records, verification evidence, and checkpoints. These generated records are ignored by Git and retained locally across restarts. The MVP format may use per-task completion records and a derived summary instead of a separate state.json. This policy does not imply an implemented Runner.

Each run must bind to the approved specification revision and verified code revision. Each attempt must identify the task, input revision, execution result, changed paths, check commands and exit codes, evidence locations, and failure reason where applicable. Verification must identify the actual tested tree; later edits invalidate that evidence.

The coding agent returns the AGENTS.md handoff and ends its session. It cannot verify itself, start the next session, or edit authoritative Runner state. The Runner checks actual changes against allowed paths, executes required gates itself, and records a verified checkpoint only when all gates pass. The current 002 design specifies Runner-owned local commits after verification; execution still requires approved task scopes/checks. Agents do not commit. A commit alone is not verification.

## Failure and resume requirements for 002

- Failed gates, missing checks, or out-of-scope changes prevent verification and advancement. Preserve evidence; never weaken tests to obtain success.
- An interrupted task is not a successful task. Reconcile its working tree and attempt evidence before retrying; do not overwrite unrelated changes.
- Resume only against compatible approved specifications and code. Do not reuse stale verification after either changes.
- Permit only one active writer for a run/workspace. Publish checkpoint state atomically so interruption cannot produce a false completed checkpoint.
- Bound execution duration using limits approved in 002. The MVP design has no automatic retries. Failure or ambiguity stops for review; a fresh attempt requires explicit operator reconciliation.
- Stop after the approved milestone. Verification does not authorize the next milestone.

002 must choose and document compact task/completion formats, execution mechanism, timeouts, commit behavior, process interruption handling and clean-workspace policy before implementation. Manual reconciliation is sufficient for interrupted work; automatic recovery, snapshot restoration and persisted retry machinery are not required. Keep one dedicated workspace and one active Runner. No queue, scheduler service or additional framework is implied.

## Evidence and security

Do not record credentials or unnecessary source content in logs. Keep expected scenario answers outside runtime input bundles. Separate deterministic application checks from real AI evaluations; skipped AI evaluations cannot count as passed evaluations. A build alone cannot verify a milestone.

## Session context and task sizing

One task is one fresh session, one independently testable feature/step and one successful task commit. Task files follow [the shared template](../task-template.md); the approved run selects a finite ordered list with dependencies. Do not split solely by file count or combine unrelated features to fill a context window.

Starting context target: 10,000-30,000 tokens. Ceiling: strictly below 100,000 tokens for the supplied instructions, task brief, selected reference content and dependency handoffs together. Include only relevant sections, code entry points, verified prerequisite commits, exported interfaces and known limitations. Do not paste the repository or entire prior conversations. Log the estimate and method when available; an estimate is not an exact guarantee. If required context is oversized or its size is uncertain near the ceiling, trim optional material or split the task before dispatch. Never remove required acceptance criteria to fit.

This MVP does not implement an automatic total-session token meter or guarantee a cap on accumulated tool responses/reasoning. Keep code reads and test output targeted. If investigation shows the task is too broad, stop with a proposed split and preserve the handoff; do not launch a second session yourself or silently exceed scope.

A task must name its objective/exclusions, prerequisites and selected references, allowed files/directories, implementation constraints, observable acceptance criteria, exact check commands with expected assertions, and stop conditions. Commands are executable/argument arrays in one fenced JSON block; use fixed Markdown headings for the rest. Pending commands/decisions mean BLOCKED, not READY. An implementation agent may add task tests but cannot weaken existing acceptance gates.

Successful handoffs identify actual changed files, exported interfaces, check commands/exits, known issues and downstream notes. Runner records bind these to the independently tested commit. The next task receives the relevant handoffs, not the chat transcript. Checklists may link completed records/commits only after independent checks; no agent-written VERIFIED entries.
