# 003 — Implementation checklist

Status: DRAFT deliverable inventory; not an executable task queue. Detailed task files, allowed paths, and exact commands follow approved milestone design. Check items only with implementation/artifact references and independent verification or documented review evidence (001). Execution state belongs exclusively to the Runner.

- [ ] Implement persistence, project membership checks, and normalized source ingestion behind an interface.
- [ ] Implement scenario source provider and read-only fake Jira provider through dependency injection.
- [ ] Test repeat imports, unauthorized project access, provenance, timestamps, and failed imports.
- [ ] Add reusable adapter contract tests for search, details, explicit links, and freshness.
- [ ] Record required focused checks and applicable earlier regression gates with actual results.
- [ ] Present milestone evidence to the owner and stop before the next milestone.

## Approved MVP revision checks

- [ ] Fresh isolated persistence setup and repeatable fixture loading pass; repeated composite source IDs return the existing stored record unchanged.
- [ ] PO_PM can ingest; MEMBER cannot mutate or investigate. Source visibility denies inaccessible project/source reads.
- [ ] Reusable source/Jira adapter tests check canonical identity, explicit link direction, missing/forbidden/timeout fixtures, and no provider writes.
