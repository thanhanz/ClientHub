# Milestone review and execution policy

## Approval and specifications

The owner approves one milestone at a time. Approval evidence must identify the milestone, specification revision, approved task scope and gates, approver, and date. Store the review record with the milestone after approval; do not prepopulate an approval. Changes to approved requirements or gates require renewed review before dependent execution.

Implementation checklists are deliverable inventories until tasks are approved. Each future task must specify its ID, goal, dependencies, allowed paths, prerequisite contract versions, exact verification commands and expected assertions, and required handoff. A missing prerequisite blocks that task.

## Runner ownership

Only the external Runner creates or updates `harness/runs/<run-id>/state.json`, attempt records, verification evidence, and checkpoints. These generated records are ignored by Git and retained locally across restarts. This policy is not an implemented state schema.

Each run must bind to the approved specification revision and verified code revision. Each attempt must identify the task, input revision, execution result, changed paths, check commands and exit codes, evidence locations, and failure reason where applicable. Verification must identify the actual tested tree; later edits invalidate that evidence.

The coding agent returns the AGENTS.md handoff and ends its session. It cannot verify itself, start the next session, or edit authoritative Runner state. The Runner checks actual changes against allowed paths, executes required gates itself, and records a verified checkpoint only when all gates pass.

## Failure and resume requirements for 002

- Failed gates, missing checks, or out-of-scope changes prevent verification and advancement. Preserve evidence; never weaken tests to obtain success.
- An interrupted task is not a successful task. Reconcile its working tree and attempt evidence before retrying; do not overwrite unrelated changes.
- Resume only against compatible approved specifications and code. Do not reuse stale verification after either changes.
- Permit only one active writer for a run/workspace. Publish checkpoint state atomically so interruption cannot produce a false completed checkpoint.
- Bound retries and execution duration using limits approved in 002. Repeated failure or ambiguity stops for review; no unbounded retry loop.
- Stop after the approved milestone. Verification does not authorize the next milestone.

002 must choose and document the concrete state schema, execution mechanism, retry/time budgets, process interruption handling, and dirty-worktree policy before implementation. No queue, scheduler service, or additional framework is implied.

## Evidence and security

Do not record credentials or unnecessary source content in logs. Keep expected scenario answers outside runtime input bundles. Separate deterministic application checks from real AI evaluations; skipped AI evaluations cannot count as passed evaluations. A build alone cannot verify a milestone.
