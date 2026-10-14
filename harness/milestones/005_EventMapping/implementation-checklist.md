# 005 — Implementation checklist

Status: DRAFT deliverable inventory; not an executable task queue. Detailed task files, allowed paths, and exact commands follow approved milestone design. Check items only with implementation/artifact references and independent verification or documented review evidence (001). Execution state belongs exclusively to the Runner.

- [ ] Implement discovery of existing Jira issues even without prior event mappings.
- [ ] Implement deterministic matching and approved optional AI adjudication.
- [ ] Persist link type, origin, provenance, and authorized human review decisions.
- [ ] Test pre-existing QA issues, Google/Apple distinction, many-to-many/unmapped states, and review concurrency.
- [ ] Verify mapping confirmation cannot approve business commitments; test candidate-provider failures.
- [ ] Record required focused checks and applicable earlier regression gates with actual results.
- [ ] Present milestone evidence to the owner and stop before the next milestone.

## Approved MVP revision checks

- [ ] MEMBER reads only CONFIRMED mappings of accessible APPROVED events; PO_PM alone proposes/reviews.
- [ ] Duplicate proposals return the existing mapping unchanged even after rejection; review version and audit changes commit atomically.
- [ ] Verify many-to-many/unmapped cases and association confirmation never changes commitment status.
