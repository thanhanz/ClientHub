# DesignFoundation expected outcomes and acceptance allocation

Status: REVIEW CANDIDATE, DF-001-R1. Evaluation/test-only specification. Never load this file into source/Jira providers, extraction prompts, or synthesis context. Inputs are in [fixture-inputs.md](fixture-inputs.md).

## Semantic expectations

Extraction must preserve the following distinct facts. Atomic wording/event count may vary where equivalent coverage is retained; additional invented commitments, identities, dates, or dependencies fail evaluation. Proposed events initially have PENDING_REVIEW; an authorized PO_PM reviews before synthesis. Approval of an extracted event means the representation was reviewed, not a new client commitment.

| Test aliases / sources | Required content and state |
| --- | --- |
| G-report / G-01 | BUG_REPORTED, REPORTED: Google callback error; source occurrence 2026-10-06T09:00:00Z |
| G-qa / G-02 | Earlier QA report with explicit AUTH-101 reference; occurrence 2026-10-04T08:00:00Z despite later ingestion |
| G-dark / G-03 | FEATURE_REQUESTED, REQUESTED_NOT_COMMITTED; valid unmapped event |
| S-request / S-01 | DEADLINE_REQUESTED, REQUESTED_NOT_COMMITTED; requested date 2026-10-15, no committed date |
| S-deferral / S-02 | Pending estimate/deferral; no commitment to October 15; do not rewrite S-request |
| S-csv, S-commit, S-nightly / S-03 | Separate CSV request, COMMITMENT_MADE with COMMITTED and committed date 2026-10-20, and nightly-delivery proposal/pending estimate with no committed date; all share the approved-note source |
| D-request, D-agreement, D-exclusion / D-01 | Distinguish first-order request, explicit first-order commitment, and returning-customer scope exclusion; no commitment date invented |
| D-extension / D-02 | SCOPE_CHANGE_REQUESTED, REQUESTED_NOT_COMMITTED for returning customers; no approved scope expansion |
| D-estimate / D-03 | PENDING_ESTIMATE for the extension; DATE precision and normalized occurrence retained; no time-of-day claim |

Some source statements permit more than one proposed enum representation (for example proposal plus pending estimate). Before 004 evaluation freeze, approve the annotation rubric and allowed alternatives; use semantic requirements above rather than a brittle one-word summary match.

## Mapping, review, and investigation assertions

| ID | Action / expected assertion |
| --- | --- |
| G-MAP | Search before creating mappings finds AUTH-101, although its creation predates G-01. Propose ADDRESSES_REPORTED_ISSUE for G-report -> AUTH-101. AUTH-103 is not a valid match for the Google bug. G-dark and AUTH-104 can remain unmapped. |
| S-MAP | Propose S-request -> SALES-201 as HAS_REQUESTED_DEADLINE_FOR and S-commit -> SALES-201 as COMMITMENT_COVERS_WORK. Many events may reference one ticket; all proposals require review. |
| D-MAP | The initial first-order agreement can associate with DISC-301 as COMMITMENT_COVERS_WORK. Leave D-extension unmapped, or propose RELATED_TO only with an explicit rationale that the old ticket covers earlier scope; never assert IMPLEMENTS_REQUEST for the extension from Done alone. |
| REVIEW | PO_PM confirms/rejects with expected version and audit; MEMBER cannot mutate. Duplicate proposal preserves original status/version/metadata, including rejected status. Competing reviews from one version allow one terminal transition; the stale reviewer receives 409. Confirming S-request's mapping leaves its business state/date unchanged. |
| G-ANSWER | Jira records AUTH-101 In Progress and explicitly BLOCKED_BY AUTH-102. Blocker FACT uses `jira-link:demo-jira:AUTH-101:BLOCKED_BY:AUTH-102`. AUTH-103 is parallel same-assignee context only when relevant; no invented dependency, actual-work claim, blame, or proven delay causation. |
| S-ANSWER | Distinguish requested October 15 (S-01), deferred agreement (S-02), later committed October 20 (S-03), and internal Jira due date October 18 (SALES-201). Each factual claim references its own evidence. |
| D-ANSWER | Earlier first-order scope remains visible; Jira records Done and a release comment for that scope. Returning-customer extension remains uncommitted/pending estimate. Old Done status does not approve or prove delivery of expanded scope. |
| ELIGIBILITY | Pending/rejected events and proposed/rejected associations do not enter synthesis; proposed mappings may guide backend discovery only. Only approved events with every source accessible are included. A valid unmapped approved event may appear. |

## All twelve acceptance cases

These are future tests/evaluations to implement in their assigned milestones, not tests claimed to have run in 001.

| Stable test ID / acceptance | Fixture and exact obligation | Gate |
| --- | --- | --- |
| SC-AC01 / AC-01 | S-03 yields at least the distinct CSV request, explicit commitment, and pending nightly proposal; same source provenance, no segment requirement | 004 deterministic persistence + real extraction evaluation |
| SC-AC02 / AC-02 | S-01/S-02 never produce an October 15 commitment; S-03 has separate October 20 commitment; D-02/D-03 never approve expanded scope | 004 real extraction + deterministic date/state preservation |
| SC-AC03 / AC-03 | G-MAP finds AUTH-101 without a pre-existing mapping and despite earlier Jira creation | 003 provider PR-01/03; 005 discovery/mapping + real mapping evaluation |
| SC-AC04 / AC-04 | AUTH-103 cannot become the Google report's approved answer/match merely from shared login vocabulary/assignee | 005 negative mapping evaluation; 006 synthesis evaluation |
| SC-AC05 / AC-05 | G-ANSWER uses directed explicit link ref; AUTH-103 never creates a Jira edge or causal FACT | 003 PR-02; 006 deterministic links + real synthesis evaluation |
| SC-AC06 / AC-06 | G-dark and AUTH-104 persist/retrieve with zero mappings; discovering Jira does not require a linked event | 005 association/search; 006 context |
| SC-AC07 / AC-07 | REVIEW and ELIGIBILITY; mapping confirmation does not change S-request, D-extension, or create a commitment | 005 review/access/concurrency/audit; 006 bundle filtering |
| SC-AC08 / AC-08 | G-qa sorts before G-report despite arriving later; S-03 occurrence remains October 9 after October 12 ingestion; ties use stable IDs | 004 timeline; 006 chronology |
| SC-AC09 / AC-09 | S-03/D-01 refs point to approved notes only; no fabricated quote, transcript segment, speaker minute, or D-03 precise time | 003 PR-07; 004 extraction and 006 synthesis evaluations |
| SC-AC10 / AC-10 | V-MISSING discloses unavailable blocker evidence without inventing contents; V-CONFLICT preserves discrepancy as unresolved; workload delay cause remains unknown | 006 partial-context tests + real adversarial synthesis evaluation |
| SC-AC11 / AC-11 | V-BOUNDS stops at each configured cap, counts provider calls/pagination, avoids cycle re-expansion; V-ACCESS excludes OTHER sources/issues/refs before AI; V-UNTRUSTED cannot alter budgets or access | 003 authorization/PR-03; 006 traversal/access/security tests |
| SC-AC12 / AC-12 | Every FACT ref resolves in its authorized request bundle to the exact source/issue/excerpt/link; V-STALE exposes observation time/limitation; invented refs fail validation | 006 registry/freshness/negative validation + real synthesis evaluation |

## Additional deterministic variants

V-SOURCE-ACL: member-leo cannot read the entire mixed-source event or any derived mapping, despite access to G-01. outsider-ada receives no SHOP content/refs/existence disclosure under the approved error policy. V-DUPLICATE returns original G-01 unchanged, with no duplicate source; changed fixture content requires a new ID/reset. These are 003/004/005 gates as applicable.

V-EXCERPTS: bundle respects at most ten history/comments each and 2000 characters per excerpt, sets truncated and warnings when omitting/clipping, and registers only included authorized evidence. V-MISSING timeout/forbidden must produce safe explicit failure/partial status; retries cannot bypass call caps. Policy choice between permitted partial output and total failure must be finalized before executable 006 tasks.

## Evaluation protocol to approve

Deterministic backend tests may use structured AI doubles to test persistence, permissions, review, references, and budgets; their outputs are test setup, never runtime source fixtures. Run context tests with Python disconnected. Separate real AI evaluations consume only permitted runtime inputs and compare results against this independently authored rubric. Record input revision, provider/model and configuration, repeats, result artifacts, and failures. Owner must approve annotation alternatives, repetition count, and numeric quality thresholds before 004/005/006 evaluation gates; no current claim of model quality is made.
