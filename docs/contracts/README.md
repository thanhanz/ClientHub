# Contracts — ClientHub

> Status: REVIEW CANDIDATE · 2026-10-14. Exact formats are **versioned baselines**, to be owner-reviewed and tested before code generation.

## Index

| File | Authority |
| --- | --- |
| `domain-contracts.md` | Identifiers, state machines, domain invariants, refs, time semantics |
| `api-contracts.md` | External ASP.NET HTTP routes, authorization, errors, idempotency, concurrency |
| `provider-contracts.md` | Mock/real normalized source and Jira read ports, behavior, failures, contract tests |
| `ai-contracts.md` | Future ASP.NET ↔ Python inference routes, input/output and trust boundary |
| `schemas/*.schema.json` | Draft 2020-12 machine-checkable wire objects; implementation must validate fixtures against schemas |

## Ownership and compatibility

- ASP.NET Core contracts, domain state and EF Core persistence belong to the backend.
- Provider adapters and Python service return **data/suggestions**, never decisions with authority over project permissions or business approvals.
- `schema_version` **must** be `1.0` in version-1 top-level wire objects. Any breaking change needs a revised version, migration strategy and contract test update.
- Client IDs and timestamp fields use string IDs and ISO-8601 UTC timestamps on the wire. Numeric IDs from providers are normalized to strings; never infer actor identity from a name in message text.
- Authorization **always** precedes context construction. A matching `ref_id` string does not automatically prove access or the truth of a claim.
- Schemas are structural checks. Business invariants and authorization rules are additional application/test checks.

## Phase gate

003 uses source/access API and provider contracts without Python. 004 adds event/extraction contracts, 005 mapping contracts, and 006 context/synthesis contracts. The API inventory describes all milestones, not just backend foundation. Draft 1.0 schemas are revised before initial freeze; deployed compatibility is not claimed.

## Compatibility examples

Machine-readable example fixtures are under `examples/`. They are illustrative synthetic data and are not Jira production records. Each sample must parse and pass the referenced schema; acceptance tests must separately check semantic requirements.

## Local contract validation

Use a workspace-local environment to avoid global Python dependency conflicts:

```powershell
py -m venv artifacts/contract-review-venv
.\artifacts\contract-review-venv\Scripts\python.exe -m pip install -r scripts/requirements-contracts.txt
.\artifacts\contract-review-venv\Scripts\python.exe scripts/validate-contracts.py
```

The validator checks all positive schemas/examples, bundle/result reference invariants, and negative mutations. It does not execute backend duplicate-import/mapping behavior, role authorization, or real AI evaluations; those gates remain in 003–006.
