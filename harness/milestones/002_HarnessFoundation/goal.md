# 002 — Minimal harness

Status: DRAFT — pending milestone review; not execution authorization.

## Goal

Build a small local PowerShell Runner that executes one fresh agent session per approved task, independently checks it, commits successful task changes and supplies durable context to the next session within the same milestone.

## Dependencies and requirements

- Dependency: 001 reviewed and accepted.
- Coverage: Execution scope, verification, interruption, resume, and milestone boundary.
- Authority: [Product Goal](../../../docs/product/goal.md), [roadmap](../../README.md), and [execution policy](../../policies/execution.md).

## Review and exit gate

Review the [checklist](checklist.md), resolve relevant decisions, and approve exact task scopes/checks at a Git revision before dispatch. Tasks may be prepared while BLOCKED; file existence is not authorization. A build alone does not establish completion.

Stop at this milestone boundary for owner review. 001/002 bootstrap uses explicitly assigned setup work until independent Runner verification exists.

## Exclusions

No general workflow platform, distributed scheduler, automatic worktree/snapshot management, automatic retries or product feature work. Use manual reconciliation after interruption. Bootstrap with explicitly assigned setup tasks.

## Session and context rules

One task is one fresh session and one cohesive, independently testable outcome. Follow [execution policy](../../policies/execution.md#session-context-and-task-sizing). Starting context target: 10,000-30,000 tokens; ceiling: strictly below 100,000 tokens including supplied instructions, task, selected references and dependency handoffs. This is not a guaranteed total-session token cap. Split oversized work before dispatch. Update these canonical files directly; Git retains history.

## Execution model

One PowerShell 7 script, `scripts/harness/runner.ps1`, runs a finite ordered list of approved tasks for one milestone. Use Git and the installed Codex CLI; no service, scheduler, framework, automatic worktree creation, or snapshot store. One dedicated clean workspace and one active Runner are required. An exclusive workspace lock rejects a second Runner; the operator must not edit the workspace during execution.

For each ready task, assemble a context packet and start a separate `codex exec` process. Never reuse a conversation ID. Check the installed CLI's arguments and final-output support before implementing the adapter. The coding agent implements one task, runs its focused checks, returns the AGENTS.md handoff, and exits. Only the Runner checks acceptance, commits, records verification, and dispatches another task.

## Inputs and context

Use the compact task and run records in the task input format below. Approval identifies one Git specification revision, the finite task list, scopes, checks, approver and date. References identify relevant contract sections and required dependencies. The approval record may follow the specification commit; it names that exact commit. Require the approved input files to match that revision before dispatch. A changed specification stops the run for review.

Each context packet contains AGENTS.md, the assigned task path, baseline commit, relevant reference paths, and Runner-verified prerequisite handoffs with commit IDs. Include exported interfaces, decisions, limitations and downstream notes. Durable source documents remain authoritative; a handoff cannot amend a contract. Do not include unrelated chat history or expected scenario answers in runtime inputs.

Existing milestone prerequisites remain in force. Missing contracts or acceptance evidence block dependent tasks. Bootstrap 002 through explicitly assigned sessions and independent operator checks until the Runner exists. No agent assigns itself the next task.

## Task loop and independent checks

1. Require a clean working tree, correct expected HEAD, unchanged approved inputs, and completed dependencies. Reject an unresolved previous attempt. Write an attempt-start record before launching the agent.
2. Run one fresh session. Default limits for task approval: 30 minutes for the agent and 10 minutes per check, with no automatic retry. Bind the final limits in task approval.
3. Require process success and a matching IMPLEMENTED handoff. Confirm the agent did not change HEAD or the index. Compare actual tracked/untracked changes with allowed paths, including both sides of renames and deletions. Protect approval/task inputs, Runner code, run records and existing acceptance tests. Any required change to those inputs needs a separate approved setup task.
4. Run the approved checks independently, as executable/argument arrays. Record actual commands, exit codes and required assertions/test counts. Zero discovered tests, skipped required checks and missing tools fail. Run the focused checks and explicitly listed regression checks; do not rerun every earlier gate by default.
5. Confirm source bytes did not change during checks, stage only the reviewed task changes, and commit. Confirm the committed source is the tested source and the worktree is clean. Write the completed checkpoint last, then select the next ready task.

Use a small temporary source hash inventory for the before/after comparison, not a durable snapshot system. Exclude only declared generated output directories; ignored source/configuration files are not exempt from scope checks. Validate repository-relative file/directory paths, reject traversal and links escaping the workspace, and match directory boundaries. This MVP catches accidental scope violations; it is not a hostile-agent security sandbox. Run records belong to the Runner; configure agent permissions to protect them where supported and document capability limits.

## Commits and records

The Runner creates one local commit per successful task, such as `003-P01: add source contract types`. Never use blanket staging, amend another commit, push automatically, or include unrelated files. Agent-created commits stop the attempt. A task with no changes stops for review rather than generating an empty success commit.

Store local logs, handoffs and Runner records under ignored `harness/runs/<run-id>/`. Records identify the approved specification, task, input/output commits, handoff, actual check results and downstream notes. Write each completed record through a temporary file and rename it into place only after checks and commit validation. A commit alone is not a verified checkpoint. No multi-file transaction protocol or generation graph is needed.

Git commit hooks can alter files: if committed content differs from the checked candidate, stop without recording verification. Commit failure also stops. Never reset or delete the candidate to recover automatically.

## Failure, interruption and continuation

On failure, ambiguity, out-of-scope edits, timeout or cancellation, stop without committing or advancing. Preserve edits and available logs. If a commit was already created but checkpoint writing failed, preserve it and stop; do not repeat or amend it automatically.

On timeout/Ctrl+C, terminate the launched process tree and exit nonzero. If the Runner itself crashes, assume a child may survive. Before restarting, the operator confirms child termination and reconciles the workspace. Automatic orphan recovery, Windows Job Object guarantees, persisted retry budgets and crash fault-injection infrastructure are deferred.

Continuation is explicit and conservative: the operator supplies the last completed task/checkpoint after reviewing any incomplete attempt. Require a clean tree, matching recorded commit, unchanged approved inputs, and complete check evidence. An incomplete or corrupt record, unrecorded commit or mismatched HEAD blocks continuation. The operator independently rechecks uncertain work or authorizes a fresh attempt; the script never infers success from a commit message. No reset, stash, cleanup or snapshot restore.

When the approved task list finishes, report AWAITING_OWNER_REVIEW and exit. Never enter another milestone automatically. Verification does not constitute owner acceptance.

## Verification scope

Use a small PowerShell test driver with temporary Git repositories and fake sessions. Cover success with two fresh sessions and two commits; failed/missing checks; scope violations; malformed handoffs; agent commits; commit failure; interrupted or incomplete records; stale inputs; dirty start; concurrent Runner rejection; and milestone stop. A real CLI smoke test separately demonstrates fresh invocation, handoff capture and normal cancellation. Keep product acceptance gates intact. Defer exhaustive crash-boundary testing and generalized recovery.

## Task input format

Canonical Markdown tasks follow the [task template](../../task-template.md). They use Task ID, Milestone and Depends on fields plus the fixed template headings. Their content declares:

- `task_id`, `milestone_id`, `goal`.
- `dependencies`: task IDs in the approved set; external milestone acceptance is a prerequisite input.
- `allowed_paths`: repository-relative files or directory prefixes, with explicit kind.
- `references`: relevant specification/contract paths and sections.
- `checks`: IDs, executable, argument array, working directory, timeout and required assertions or positive test-count expectations. Include applicable regression checks explicitly.
- `output_paths`: generated directories that checks may write, never source directories.
- `agent_timeout_seconds` and required AGENTS.md handoff fields.

Parse fixed headings and the fenced JSON check block. Validate required fields, unique IDs, dependency order, path boundaries and nonempty checks before dispatch. Commands are executable/argument arrays, never shell expressions. Generate JSON execution inputs if needed; never maintain a second editable task definition. No generic schema engine or canonical digest is required.

## Run input and approval

A small run configuration records `format_version: 1`, `run_id`, `milestone_id`, `specification_commit`, `baseline_commit`, ordered `task_paths`, and `approval_path`. The approval section of checklist.md names the specification commit, approved task list/scopes/checks/limits, prerequisite acceptance evidence, approver and date. Approval is never generated by the coding agent or inferred from checklist marks.

Tasks, goal.md, AGENTS.md, applicable policies, references and trusted check definitions must match the approved specification commit. Bind the approval section separately at run start; Runner-added completion links do not change the approved task specification. Reject any other checklist edits during the run. Git is the revision binding; no separate manifest format. Changes require review before dependent execution. The run config may live locally; approved task definitions are committed before use.

## Session context and handoff

The Runner supplies task/reference paths, expected HEAD and prerequisite summaries: task ID, verified commit, exported interfaces, known issues and downstream notes. Missing dependency evidence blocks dispatch. A context packet is a convenience, not a new source of authority.

The final agent output contains the existing seven fields: TASK_ID, RESULT (IMPLEMENTED/BLOCKED/FAILED), CHANGED_FILES, CONTRACTS_EXPORTED_OR_CHANGED, TESTS_RUN, KNOWN_ISSUES, DOWNSTREAM_NOTES. Prefer a JSON object carrying these fields if the installed CLI supports structured final output. Otherwise capture and validate a documented fixed text format. Missing/mismatched fields stop the run. The agent cannot report VERIFIED. Runner checks override agent claims.

## Runner-owned local records

Under `harness/runs/<run-id>/`, keep one attempt-start record, the captured handoff and logs, and a completed record per task. Each attempt identifies the task, specification commit, input commit, start time and session outcome. Each completed checkpoint adds:

- Output commit and actual changed paths.
- Check commands, exit codes, required assertion/test-count results and log paths.
- Handoff path and dependency commit references.
- Runner verification result and completion time.

A completion record is published last through temporary-file rename. Missing or malformed evidence blocks continuation. A small summary may list completed tasks and AWAITING_OWNER_REVIEW; it is derived from completed records, not an independent authority. Do not add snapshot bundles, generation counters, transitive invalidation graphs or automatic reconciliation records.

Store no credentials or unnecessary source content in logs. These records are local and ignored by Git; preserve them if continuation is needed. If lost, stop and independently recheck rather than treating commit history as verification. Only the external Runner writes real records; tests use disposable synthetic directories.

## Current readiness

Runner code and harness test driver remain absent. Prerequisite acceptance and task approvals remain pending. The earlier readiness review identified these same gaps; its R1 snapshot, retry and whole-run-budget additions were superseded by the lightweight design. Use exact task commands: 002 does not promise a product-wide scripts/verify.ps1 wrapper. Completion links in checklist.md are a Runner-owned projection, separate from task commits and agent write scope. To keep the execution workspace clean, publish that projection only at the milestone stop; local run records carry per-task progress during execution. Reconcile and commit any checklist-only update explicitly before starting a later run. It cannot masquerade as a task commit or change task approval.
