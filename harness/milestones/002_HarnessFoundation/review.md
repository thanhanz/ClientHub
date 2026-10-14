# Owner review packet — HF-002-R1

Date: 2026-10-15. Status: REVIEW CANDIDATE; approval pending. This is explicitly assigned documentation bootstrap work, not Runner implementation. Read [proposed design](proposed-design.md), [proposed contracts](proposed-contracts.md), and [proposed task breakdown](proposed-task-breakdown.md). Existing goal/checklists remain draft/unreviewed; no boxes or execution state changed.

## Evidence and prerequisites

Read milestone 002 goal and both checklists, execution policy, roadmap, milestone 001 goal/review/manifest, and relevant owner-approved rules in docs/architecture/decisions.md. Milestone 001 [review](../001_DesignFoundation/review.md) records DF-001-R2 as REVIEW CANDIDATE, approval pending, unresolved DF-01–11 and no independent verification. Its manifest has `approval: null`. Recorded contract validation, build and test commands failed before validation/compilation/tests; these are historical results, not commands rerun here. Its candidate manifest is an optional review aid, not acceptance.

2026-10-14 owner approval recorded in architecture decisions covers specific product rules and roadmap direction; it explicitly excludes blanket technology approval, milestone completion and Runner verification. No evidence inspected authorizes acceptance of 001 or implementation of 002. Documentation preparation is authorized by this session; implementation readiness remains blocked.

Missing prerequisites:
- Explicit 001 acceptance bound to the actual reviewed revision, including disposition of DF-01–11 and recorded failed gates. Any deferral must say which dependent work remains blocked; 002 cannot silently waive its 001 dependency.
- 002 owner approval of goal/resolved design, exact tasks/scopes/gates, concrete budgets and contract version, with approver/date and revision binding.
- Capability evidence for PowerShell 7, local NTFS, Git, installed Codex CLI fresh sessions, final-output transport, isolated permissions and Windows child-tree termination. Proposed adapter must not be implemented by guessing flags or accepting prompt-only isolation.
- Exact executable task files issued after approval and independent bootstrap dependency evidence. No `tasks/` files are created now.
- Applicable earlier regression-gate disposition and a working independent bootstrap verification environment. `scripts/verify.ps1` is currently absent; future harness test commands are proposals, not existing successful gates.

Product technology/provider/AI gaps in DF-02–11 are not resolved by this harness design. No product implementation or contract amendment is proposed here. Any 001 acceptance with bounded deferrals must retain explicit downstream blocks before 003/004/005/006 work.

## Review questions (no approval prefilled)

Owner should resolve: PowerShell/CLI adapter and isolation capability; strict local JSON contracts and manifest binding; isolated clean worktree policy; current-tree cumulative regression evidence; NTFS lock/atomic publication; two-attempt and 30/10/60-minute budgets; manual reconciliation/retry; independent bootstrap verification; exact five-task scopes/gates. Approve/revise the specification as a whole with a content manifest or exact clean commit, not the label alone. If any choice changes, update proposal and rebind approval before executable tasks.

Coverage for design checklist: execution mechanism/contracts in design §Authority and contracts; authority/readiness/scope in design §§Approval and Scope; atomicity/dirt/staleness in §§Scope, Exclusive execution and Interruption; budgets/bootstrap gates in design and task breakdown. Approval remains pending. Implementation checklist coverage is planned by tasks 01–05 and matrix, not demonstrated implementation evidence.

## Session scope and checks

Initial status contained only unrelated untracked `harness/milestones/003_BackendFoundation/proposed-task-breakdown.md`; preserve it byte-for-byte. Created four documentation files in milestone 002 only. No Runner, test driver, workflow platform, product code, approval record, authoritative state or executable task was created. Local documentation checks validate relative links, whitespace/conflict markers and actual scope. Product/runtime acceptance tests and proposed harness commands are NOT_RUN because this session implements no runtime and those commands do not yet exist.

Stop for owner review. This packet does not accept 001/002, authorize implementation, or launch 003.

## Actual documentation verification

The following inline PowerShell command ran from repository root and exited 0 (four documents, 14 relative links). It covers new untracked files, which `git diff --check` alone does not inspect:

```powershell
$docs = @('proposed-design.md','proposed-contracts.md','proposed-task-breakdown.md','review.md'); $root = Join-Path (Get-Location) 'harness/milestones/002_HarnessFoundation'; $links = 0; foreach ($name in $docs) { $path = Join-Path $root $name; $content = Get-Content -LiteralPath $path -Raw; if ($content -match '(?m)[ \t]+$|^(<<<<<<<|=======|>>>>>>>)') { throw "Whitespace/conflict marker: $name" }; foreach ($match in [regex]::Matches($content, '\]\(([^)]+)\)')) { $target = $match.Groups[1].Value.Split('#')[0]; if ($target -and $target -notmatch '^https?://') { if (-not (Test-Path -LiteralPath (Join-Path $root $target))) { throw "Missing link in ${name}: $target" }; $links++ } } }; Write-Output "PASS: 4 documents; $links relative links; whitespace/conflict checks"
```

`git diff --check`: PASS, exit 0 (tracked whitespace only). `git status --short`: PASS, exit 0, shows only the four new 002 documents plus the pre-existing untracked 003 draft. Repeat documentation check after this evidence appendix uses the same command; no product/runtime check is implied.
