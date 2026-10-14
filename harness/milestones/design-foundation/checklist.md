# D0 — Design Foundation Review Checklist

> Status: NOT VERIFIED. All boxes intentionally start unchecked. An approved artifact requires owner review and documented evidence, not merely a file existing.

## Product and decision authority

- [ ] Product Goal reviewed and MVP boundaries explicitly approved.
- [ ] All `USER-DIRECTED` and `PROPOSED` design decisions in `docs/architecture/decisions.md` are reviewed.
- [ ] No architecture or contract rule contradicts `docs/product/goal.md` or the v2 handoff.
- [ ] Unresolved production integration and security choices are captured as open decisions.

## System design

- [ ] Backend owns identity/project access, persistence, Jira retrieval, context assembly, verification and audit.
- [ ] Python AI service has no DB/Jira/source provider credentials or domain authorization authority.
- [ ] Mock and real provider adapters share normalized contracts.
- [ ] All trust boundaries and cross-project access paths are reviewed.
- [ ] Backend M1 can run with Python and real providers disabled.

## Database / ERD

- [ ] Event, source, membership, mapping and audit relationships are reviewed.
- [ ] Same-project relationship invariants are database/test enforceable.
- [ ] Jira external identity is composite and Jira remains authoritative.
- [ ] Event business/review status and mapping review status are independent.
- [ ] Occurrence/import/observation timestamps and retention are consistent.
- [ ] Event history and mapping optimistic concurrency have a concrete implementation plan.

## Workflows and contracts

- [ ] WF-01 / WF-02 / WF-03 happy and failure paths are reviewed.
- [ ] API endpoints, authorization, error and idempotency conventions are accepted.
- [ ] Jira link direction and bounded retrieval policies have tests.
- [ ] Context bundle and evidence registry have stable ref conventions.
- [ ] AI inference output is independently validated by backend with explicit uncertainty.
- [ ] Existing JSON Schema example fixtures validate successfully.
- [ ] API/domain/provider/AI documents agree on enums, IDs, timestamps and lifecycle.

## Testability / integration readiness

- [ ] AC-01..AC-12 traced to intended tests (`docs/architecture/traceability.md`).
- [ ] Synthetic scenarios have independent expected results and negative cases.
- [ ] Backend Foundation Definition of Done and out-of-scope rules are approved.
- [ ] Known mock-vs-real integration risks are listed and sandbox contract spike planned.
- [ ] Design reviewer records `READY FOR BACKEND IMPLEMENTATION` or explicit conditions.

## Review sign-off (human / trusted workflow)

- Review date:
- Reviewer:
- Approved document versions / commit:
- Blocking findings:
- Decision: `NOT READY` / `READY WITH CONDITIONS` / `READY`:
