# Requirements-to-Design Traceability — ClientHub

> Status: REVIEW CANDIDATE. Traceability is a design map, **not proof that tests have run**. Product Goal `AC-01`..`AC-12` is the authoritative acceptance list.

| Product acceptance | Primary design location | Contract / test obligation | Milestone |
| --- | --- | --- | --- |
| AC-01 Multiple events per meeting | `workflows.md` WF-01; `erd.md` source links | `extraction-output.schema.json`; multi-event evaluation | M2 |
| AC-02 Requested vs committed deadline | `domain-contracts.md` business state; WF-01 | negative commitment classification dataset | M2 |
| AC-03 Existing QA ticket before client | WF-02/03; provider search | `PR-01`, `API-12`; seeded earlier Jira fixture | M1/M3 |
| AC-04 Do not match Apple to Google | WF-02; mapping contract | mapping negative candidate regression | M3 |
| AC-05 Explicit blocker vs same-assignee | `system-design.md` retrieval; WF-03 | `PR-02`, `API-09`; exact Jira-link ref | M1/M4 |
| AC-06 Unmapped event and ticket | `erd.md` zero-to-many association; WF-02/03 | `DB-04`, `DB-05` and retrieval tests | M1 |
| AC-07 Mapping review ≠ approval | `domain-contracts.md` states; WF-02 | `API-05/06/07/08`; audit check | M1/M3 |
| AC-08 Chronology by occurrence | `erd.md` time model; WF-04 | `DB-07`, `API-04` | M1 |
| AC-09 No invented minute-level meeting source | `system-design.md` retention; WF-01 | `PR-07`; summarization evaluation | M2/M4 |
| AC-10 Missing evidence acknowledged | `system-design.md` limitations; WF-03 | investigation result schema + adversarial eval | M4 |
| AC-11 Bounded authorized retrieval | `system-design.md` retrieval; WF-03 | `API-01/02/10`; traversal/cross-project tests | M1 |
| AC-12 Resolvable, fresh evidence refs | `domain-contracts.md` refs; WF-03 | `API-11`; registry and freshness tests | M1/M4 |

## Mandatory negative/invariant tests

- Cross-project source/event joins are rejected in both application and persistence checks.
- Unauthenticated or non-member caller cannot obtain refs or existence of hidden data.
- Invalid, invented or unauthorized `ref_id` cannot pass the final claim validator.
- Review state transitions cannot be skipped by AI outputs; review version conflicts are rejected.
- Explicit `BLOCKED_BY` link stays distinct from a relevant ticket with same assignee.
- LLM inference service has no Jira/DB credentials; all Python outputs must be treated as untrusted proposals.
- Backend M1 context creation must run with Python service disconnected.

## Test evidence requirements

Each check needs: stable test ID, fixture, assertion, command, actual exit/result, commit SHA, runner verification record. Code presence or `[x]` in a Markdown list is not test evidence.
