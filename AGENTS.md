# AGENTS.md — ClientHub Agent Router

This is the **entry point**, not the full project specification. Keep it short.
You are a **task executor** in a fresh, single-task session. The external Harness Runner selects tasks, verifies results, records checkpoints, and starts subsequent sessions. Do not assume previous chat history is available.

## 1. Route to the right source

| Need | Read |
| --- | --- |
| Product goals, scope, non-goals, acceptance criteria | `docs/product/goal.md` (relevant sections only) |
| Assigned backend milestone | `harness/milestones/003_BackendFoundation/goal.md` **when created** |
| Assigned task, dependencies, allowed changes, tests | Exact task file/path supplied by the Runner **when created** |
| Approved design decisions | Relevant files under `docs/architecture/` **if present** |
| API, domain, and AI data contracts | Relevant files under `docs/contracts/` **if present** |
| Execution and security policies | Relevant files under `harness/policies/` **if present** |
| Implementation and tests | Relevant files under `src/Hub.Api/` and `tests/Hub.Tests/` |
| Test commands | `scripts/verify.ps1` **if present**; otherwise use the existing .NET solution/test projects |

Do not treat an empty directory, `.gitkeep`, a proposed design, or an absent task file as an approved specification. If a required contract or decision is missing, report the blocker; do not invent it.

## 2. Session entry protocol

1. Read the Runner-provided **task ID, task file, allowed paths, and verified dependency summary**. If the Runner is not yet implemented, follow the user's **explicitly assigned setup task** only.
2. Inspect `git status --short` before changes. Do not overwrite unrelated or pre-existing changes.
3. Read only the product/architecture/contract sections and code needed for this task. Prefer targeted search over whole-repository dumps.
4. Check prerequisite contracts and downstream interfaces listed by the task. Preserve compatibility; do not implement the next task.
5. Implement the smallest cohesive change, including task-specific tests.
6. Run the prescribed focused verification. Report what actually ran and its exit status.
7. Produce a concise handoff and **end this session**. Never start or resume the next Codex session yourself.

## 3. Non-negotiable project boundaries

- The **ASP.NET Core backend** owns persistent data, authorization, Jira retrieval boundaries, context assembly, final validation, and audit.
- The future **Python AI service** receives backend-authorized inputs and returns structured inference results; it must not directly query Jira or the project database.
- Jira investigation is **read-only**. Project isolation and retrieval limits are enforced in backend code, not only in prompts.
- Do not infer client commitments, causal relationships, issue links, or evidence that the sources do not establish.
- Do not broaden MVP scope, add infrastructure/frameworks, or modify protected product goals/architecture/contracts without an explicitly authorized planning task.

The full authority for product semantics is `docs/product/goal.md`; the brief statements above are reminders, not a replacement.

## 4. Scope and verification rules

- **One assigned step per session.** Modify only allowed paths. If another path is required, stop and request a scope/plan change.
- Do not weaken, delete, skip, or rewrite required acceptance tests to manufacture a PASS.
- If `scripts/verify.ps1` exists, use its task-appropriate mode. Until it exists, use applicable checks such as `dotnet build ClientHub.slnx` and `dotnet test tests/Hub.Tests/Hub.Tests.csproj`; explicitly disclose checks that are unavailable.
- A successful command proves only the checks that actually ran. Do not declare the product or milestone complete from a build alone.
- **Never mark a step `VERIFIED`, edit authoritative runner state, or record an unverified checkpoint.** Only the external Runner may do so after its independent gates pass.
- On ambiguous requirements, failing prerequisites, unauthorized changes, or repeated verification failures, stop and report the blocker rather than improvising.

## 5. Required end-of-session handoff

Return a short, factual summary with these fields:

```text
TASK_ID:
RESULT: IMPLEMENTED | BLOCKED | FAILED
CHANGED_FILES: [paths from the actual diff]
CONTRACTS_EXPORTED_OR_CHANGED: [types, endpoints, schemas, or none]
TESTS_RUN: [exact commands and PASS/FAIL/NOT_RUN]
KNOWN_ISSUES: [issues or none]
DOWNSTREAM_NOTES: [what dependent tasks must know]
```

`IMPLEMENTED` is **not** `VERIFIED`. The Runner independently checks scope, tests, regressions, and checkpoint eligibility before selecting the next ready task.
