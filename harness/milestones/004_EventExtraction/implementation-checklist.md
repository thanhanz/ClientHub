# 004 — Implementation checklist

Status: DRAFT deliverable inventory; not an executable task queue. Detailed task files, allowed paths, and exact commands follow approved milestone design. Check items only with implementation/artifact references and independent verification or documented review evidence (001). Execution state belongs exclusively to the Runner.

- [ ] Implement stateless Python extraction receiving only backend-authorized context.
- [ ] Validate and persist events with source provenance and separate review/business state.
- [ ] Implement authorized review and occurrence-ordered timeline preserving history.
- [ ] Test multiple events, requested versus committed dates, late arrivals, and absent transcript details.
- [ ] Test invalid AI payloads/references, denied review, duplicate retries, and service failure; run real extraction evaluations.
- [ ] Record required focused checks and applicable earlier regression gates with actual results.
- [ ] Present milestone evidence to the owner and stop before the next milestone.

## Approved MVP revision checks

- [ ] Require at least one source per persisted event; commit event/provenance atomically and deny cross-project links.
- [ ] Hide events when any supporting source is inaccessible; MEMBER sees APPROVED events only.
- [ ] Round-trip requested/committed deadlines and occurrence precision; manual and extracted events cannot bypass authorized review.
