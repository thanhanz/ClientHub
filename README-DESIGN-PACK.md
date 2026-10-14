# ClientHub Design Pack

This is a **copy-ready repository subtree**, not a modification to your local PC folder. Merge the files into the matching paths in your own `ClientHub/` repository.

## What is included

- Existing `AGENTS.md` and `docs/product/goal.md`, copied unchanged as context.
- Architecture review candidate: `docs/architecture/{README,system-design,erd,workflows,decisions,tech-stack,traceability}.md`.
- Contracts review candidate: `docs/contracts/{README,domain-contracts,provider-contracts,api-contracts,ai-contracts}.md`.
- Versioned JSON schemas in `docs/contracts/schemas/` and valid synthetic examples in `docs/contracts/examples/`.
- D0 design checklist and bounded M1 backend goal.

## Recommended use

1. Read `docs/architecture/README.md` and `decisions.md`; approve or adjust **proposed** technology choices.
2. Have an independent reviewer challenge system design, ERD, workflows, contracts and the design checklist.
3. Run JSON schema checks on examples; add your own negative tests and product acceptance fixtures.
4. Sign off D0, then derive milestone steps from `harness/milestones/backend-foundation/goal.md`.
5. Allow the coding harness to change only files listed by its task contracts; architecture documents require an authorized change request.

## Important limitation

These are **draft source-of-truth candidates**: the content is consistent with the supplied product goal and handoff in its principal invariants, but unapproved implementation defaults do not become final merely because they are written. Real Jira/Email/Chat/Meeting integration behavior must still be verified against actual provider environments before production use.
