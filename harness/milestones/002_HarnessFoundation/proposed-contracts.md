# Proposed v1 machine-readable contracts

Status: PROPOSED, not approved schemas or executable inputs. All objects reject unknown fields, duplicate JSON keys, invalid enum values, missing required fields, malformed IDs/hashes and unsupported `schema_version`; paths are canonical repository-relative slash paths. UTC times use ISO 8601; durations are positive integer seconds; SHA-256 uses lowercase 64 hex digits. No secrets or full prompts/source content in evidence. Lists below specify required fields; `?` means nullable/optional. Implement strict serialization/validation in task HF-002-01 after approval.

## Shared bindings

`revision`: `{label, manifest_path, manifest_sha256}`. `tree`: `{head_commit, index_sha256, inventory_path, inventory_sha256}`; inventory entries sorted by canonical path: `{path, kind, mode, sha256}`. Missing/deleted files are represented by comparison, not empty hashes. Inventory also records explicitly excluded output roots. `evidence_ref`: `{path, sha256}`. Paths to local generated evidence are resolved only within the run root; prerequisite approvals/specifications are resolved only within the approved repository root.

`approval`: `{schema_version:1, milestone_id, revision, task_bindings:[{task_id, task_path, task_sha256, gates_sha256}], limits, prerequisite_acceptances:[evidence_ref], approver, approved_at, scope}`. This is an owner-authored record; validator checks structure and exact bindings, not whether a person is trustworthy. Approval is a local trust boundary: explicit operator selection of owner evidence and read-only isolation are required, no fabricated signature security.

## Task

`{schema_version:1, task_id, milestone_id, goal, revision, dependencies:[task_id], prerequisite_contracts:[{path, sha256, version}], allowed_paths:[{path, kind:FILE|DIRECTORY}], gates:[{id, executable, argv, cwd, timeout_seconds, expected_exit:0, assertions:[string], output_roots:[path], verifier_sha256}], required_regression_gate_ids:[string], limits:{max_attempts, agent_seconds, gate_seconds, task_seconds, termination_grace_seconds}, handoff_fields:[string], stop_instructions:[string]}`.

Commands are executable/argv arrays, never shell-evaluated strings. Executables/tool versions and environment identity are pinned in run configuration. Task and gates cannot authorize writes to state or protected inputs. Duplicate gate IDs, empty assertions/gates, cross-milestone dependencies without accepted evidence, cycles and broader budgets than approval are rejected.

## Agent handoff

`{schema_version:1, task_id, attempt_id, revision, result:IMPLEMENTED|BLOCKED|FAILED, changed_files:[path], contracts_exported_or_changed:[string], tests_run:[{executable, argv, exit_code?, result:PASS|FAIL|NOT_RUN, reason?}], known_issues:[string], downstream_notes:[string]}`.

Collect this JSON from the session's final output using the CLI adapter and render the seven AGENTS.md fields for the operator. NOT_RUN requires reason and null exit code; PASS requires zero. Missing/malformed/mismatched handoff blocks verification. Claims never set Runner status. Actual file inventory and Runner checks override handoff claims.

## Attempt (Runner only)

`{schema_version:1, run_id, attempt_id, task_id, revision, approval_ref, input_tree, candidate_tree?, dependency_evidence:[evidence_ref], started_at, ended_at?, consumed_seconds, session:{adapter_version, process_id?, invocation_digest, exit_code?, termination_reason?}, execution_result:STARTED|IMPLEMENTED|BLOCKED|FAILED|INTERRUPTED|CANCELLED, handoff_ref?, changed_paths:[{path, change_kind, old_path?}], scope_result:PENDING|PASS|FAIL, checks:[{gate_id, executable, argv, cwd, environment_digest, started_at, elapsed_seconds, exit_code?, assertions:[{id, passed}], stdout_ref?, stderr_ref?, result:PASS|FAIL|NOT_RUN|TIMEOUT|CANCELLED}], evidence_refs:[evidence_ref], failure_reason?}`.

STARTED records are immutable and separate from terminal completion records. Interrupted terminal records may have unknown candidate/check exit fields; uncertainty is a failure to verify. Logs are bounded (1 MiB per stream, truncation recorded); do not store credentials. Nonempty failure reason required for unsuccessful terminal results.

## Run state and checkpoint (Runner only)

`state`: `{schema_version:1, run_id, milestone_id, revision, approval_ref, baseline_tree, current_tree, generation, status:READY|RUNNING|VERIFYING|STOPPED_FAILED|STOPPED_SCOPE|INTERRUPTED|CANCELLED|BLOCKED|AWAITING_OWNER_REVIEW, active_attempt_id?, task_records:[{task_id, status:PENDING|VERIFIED|INVALIDATED, attempts_used, consumed_seconds, checkpoint_ref?}], last_checkpoint_ref?, reconciliation_ref?, updated_at}`.

`checkpoint`: `{schema_version:1, run_id, generation, task_id, revision, approval_ref, tested_tree, dependency_evidence:[evidence_ref], attempt_ref, verification_ref, cumulative_gate_ids:[string], snapshot_ref, created_at}`. `verification`: `{schema_version:1, tested_tree, before_tree, after_tree, approval_ref, task_ref, environment_digest, scope_result, checks, verdict:PASS|FAIL, invalidation_reason?}`. VERIFIED is emitted only by external Runner after all gates PASS, no omitted assertions, exact before/after match and atomic publication. Agents never write these records.

`reconciliation`: `{schema_version:1, run_id, attempt_id?, observed_tree, preserved_evidence:[evidence_ref], decision:PRESERVE_AND_RETRY_CLEAN|ADOPT_IN_SCOPE_BASELINE|STOP, operator, decided_at, reason, new_baseline_tree?}`. Adoption starts a new attempt; it cannot retroactively verify the old one.

`acceptance` prerequisite input: `{schema_version:1, milestone_id, revision, evidence_refs:[evidence_ref], resolved_findings:[{id, disposition, evidence_ref}], accepted_by, accepted_at, authorized_next_milestone?}`. Authorization of next milestone is still a distinct approved scope/gate binding; acceptance alone cannot launch it.

## Invariants and readiness

A run has one milestone and one bound approval. A VERIFIED task has exactly one valid checkpoint reachable through committed state generation, matching complete evidence hashes and current cumulative tree/regression evidence. Dependency evidence must be valid on current source bytes and approved contract digests; different manifest, changed inputs, failed regression, unknown environment or altered evidence blocks reuse and transitively invalidates dependents. Historical evidence remains immutable. Attempt counters and time consumed never decrease on resume. Cancellation/interruption never creates a verified checkpoint. No state enum denotes owner acceptance.
