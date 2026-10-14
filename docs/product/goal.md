# PO–Client Communication Hub — Product Goal (MVP)

> **Document type:** Master Product Goal and Scope  
> **Status:** Proposed MVP baseline — review before freezing  
> **Updated:** 2026-10-14  
> **Primary reference:** `PO_Client_Hub_Architecture_Handoff_v2.md` (2026-10-13)  
> **Purpose:** Define what the product must achieve and the boundaries future architecture, plans, and implementation must respect.

## 1. Product Identity

**Product name:** PO–Client Communication Hub  
**Core capability:** Evidence-backed Project Investigation (practical **AI Project Memory**)  
**Primary users:** Product Owners and Project Managers (PO/PM)  
**MVP delivery strategy:** Build a verifiable backend foundation first, then connect the AI capabilities and complete end-to-end evaluations.

## 2. Problem Statement

Customer requests and project decisions are spread across email, chat, meetings, approved notes, and Jira. A PO/PM may struggle to reconstruct:

- What the client originally requested or reported.
- Whether a request was discussed, rejected, awaiting an estimate, or explicitly committed.
- Which Jira items relate to a business event, including issues created before the client report.
- What Jira currently records about ownership, progress, blockers, dependencies, and history.
- Which explanations are supported by evidence versus merely plausible.

The product must reconstruct project context **without inventing agreements, ticket links, root causes, or activity that the sources do not establish**.

## 3. Product Goal

Enable an authorized PO/PM to ask a natural-language question about a customer issue, feature, scope change, or deadline and receive a concise, chronological, evidence-backed investigation connecting business events to relevant Jira records.

The investigation must distinguish:

1. **FACT:** A supported business fact or an accurately attributed Jira-recorded fact.
2. **HYPOTHESIS:** A plausible but unverified explanation, clearly qualified.
3. **UNKNOWN:** An unresolved, stale, conflicting, or unsupported conclusion.

**Success is measured by reliable, traceable answers — not by producing an answer to every question.**

## 4. Users, Inputs, and Outputs

### 4.1 Users

- **PO/PM:** Reviews extracted events, verifies mappings, and requests investigations.
- **Authorized project members:** May access project data only according to assigned roles and permissions.
- **Client access:** Not part of the baseline MVP; any future client-facing access requires separate authorization rules.

### 4.2 Inputs

- Email or chat content with source identifiers, timestamps, and reliable sender metadata.
- Meeting transcription when its processing is permitted, or approved meeting notes.
- Jira issues and their recorded details, history, hierarchy, and explicit issue links.
- A natural-language investigation question, with or without a Jira issue key.

### 4.3 Outputs

- Structured, atomic business events with source provenance.
- Proposed or confirmed event-to-ticket associations with review status.
- A timeline of relevant events and Jira records ordered primarily by occurrence time.
- An investigation containing supported findings, qualified hypotheses, unknowns, and accessible evidence references.
- An auditable record of relevant review and investigation actions.

## 5. Functional Requirements

### FR-01 — Source Intake and Normalization

- Support the ingestion of permitted email, chat, meeting notes, or temporarily processed transcription data.
- Associate each source with the correct project, source identifier, source type, and available time/actor metadata.
- Preserve meeting-level metadata and approved business summaries; retaining raw transcripts, audio, and segments is **optional and policy-dependent**, not required for the MVP.
- Do not invent speaker identity or minute-level citations when those details are unavailable.

### FR-02 — Atomic Business Event Extraction

- Extract multiple distinct events from a single source where appropriate.
- Represent client requests, bug reports, feature requests, proposals, commitments, rejections, scope exclusions, and pending estimates distinctly.
- Preserve the difference between **requested** and **committed** deadlines.
- Record source provenance, `occurred_at`, and event review/business status without conflating these concepts.
- Support PO/PM review of important or ambiguous extracted events.

### FR-03 — Event–Jira Mapping

- Model business events as first-class entities.
- Support many-to-many event–ticket associations, including events without tickets and tickets without events.
- Search for existing Jira tickets even when no event-to-ticket mapping exists.
- Use explicit identifiers and deterministic candidate signals before semantic/LLM adjudication where relevant.
- Keep AI-inferred links `PROPOSED` until an authorized reviewer confirms or rejects them.
- Record mapping origin, relationship type, status, and reviewer/provenance.
- Treat mapping confirmation as **association approval only**, never as approval of a deadline, scope, or commitment.
- Use Jira's **explicit** issue links and hierarchy for ticket-to-ticket relationships; do not manufacture these relationships.

### FR-04 — Project Timeline and Search

- Support ticket-centric, feature-centric, and project-related lookup, including questions without a Jira key.
- Show source-backed events alongside related Jira records.
- Order the timeline primarily by `occurred_at`, with stable tie-breakers, rather than database insertion time.
- Preserve historical changes; do not silently overwrite earlier business requests or commitments.

### FR-05 — Bounded Jira Investigation

- Retrieve relevant Jira issue fields, status, assignee, history, comments where available, and explicit blockers/dependencies.
- Expand to related issues only when relevant to the question and permitted by the user's project access.
- Allow relevant same-assignee workload as context, **never as proof of delay causation**.
- Enforce traversal depth, ticket count, tool-call, and authorization limits outside LLM prompts.
- Report truncated or unavailable context instead of pretending retrieval was complete.

### FR-06 — Evidence-backed Investigation Output

- Answer questions using reviewed events and authorized Jira context.
- Provide traceable references for significant factual claims.
- Separate facts from hypotheses and unknowns.
- Do not assert a root cause, a person's actual work activity, a commitment, or an approval without sufficient evidence.
- Attribute Jira status as **what Jira records**, not independently verified real-world activity.
- Expose source freshness or uncertainty when it affects the conclusion.

### FR-07 — Review, Validation, and Audit

- Validate structured output schemas and referenced entity existence.
- Verify project permissions and provenance before displaying or persisting results.
- Apply server-side checks to evidence references and retrieved Jira fields; semantic claims may additionally require evaluation or human review.
- Keep review decisions and investigation activity auditable.
- Do not treat schema validity alone as proof of semantic correctness.

## 6. Architectural and Security Invariants

These are **MVP implementation boundaries**, not an invitation to add unnecessary infrastructure.

1. **Backend ownership:** The .NET backend owns durable data, authorization, retrieval policies, context-bundle construction, orchestration decisions, result validation, persistence, and audit.
2. **AI service boundary:** The Python AI service receives only backend-prepared, authorized input; it runs model inference and structured-output/schema validation; it returns JSON. It has **no direct Jira credentials, database connection, or independent source-retrieval authority**.
3. **Backend-enforced access:** Every source, event, ticket context, and evidence reference is filtered by project authorization before being placed in an AI request or response.
4. **Backend-enforced budgets:** Retrieval limits are enforced in code. Initial configurable MVP defaults may use **2 Jira-link hops**, **10 tickets**, and **12 external tool calls** per investigation; these are tuning defaults, not guaranteed final limits.
5. **Read-only Jira access:** Investigation does not mutate Jira tickets, issue statuses, assignments, scope, or deadlines.
6. **Human authority:** AI does not approve customer commitments, proposed mappings, or scope changes on behalf of the PO/PM.
7. **Evidence integrity:** Missing, contradictory, stale, or inaccessible evidence must be surfaced as a limitation, not filled with an invented claim.
8. **Source retention:** Retain only content permitted by organizational policy. Approved notes and meeting-level references are valid when transcripts cannot be stored.
9. **System of record:** Jira remains authoritative for Jira-managed fields. The Hub must not become a second Jira.
10. **AI is advisory:** Model suggestions cannot override deterministic validation, access control, or business approvals.

## 7. MVP Scope

### 7.1 In Scope

- A minimal backend API for projects, permitted sources, structured events, and event–ticket links.
- Project membership and access enforcement in backend APIs and investigation retrieval.
- Reproducible seeded email/chat/meeting-note examples and Jira mock fixtures.
- Extraction from permitted normalized inputs, with human review for important/ambiguous events.
- A hybrid candidate-mapping workflow with reviewable `PROPOSED` links.
- Timeline and lookup for mapped and unmapped events/issues.
- Read-only, bounded Jira investigation against the MVP adapter/data source.
- An authorized **context bundle** with stable evidence reference identifiers.
- AI-generated structured findings validated by the backend.
- At least the agreed demonstration and acceptance scenarios in Section 9.
- Automated tests, reproducible local startup, and a demonstrable deployment configuration.

### 7.2 Out of Scope for MVP

- Autonomous code changes, Jira issue mutation, or ticket assignment decisions.
- Automatic approval of customer scope, commercial commitments, or deadlines.
- Assigning blame or presenting speculative causal explanations as verified root causes.
- A mandatory event-to-event graph or AI-generated ticket-to-ticket dependency graph.
- Mandatory persistent raw meeting transcripts, audio, utterance-level segments, or forensic transcription archives.
- A multi-agent swarm or graph database required solely for the sake of architecture complexity.
- Full production integrations for all communication channels, enterprise-grade retention administration, or a complete replacement for Jira.
- Uncontrolled cross-project investigation or client access without a separate access-control design.

### 7.3 Deferred / Not Yet Decided

- The production Jira integration mode: REST, MCP, mirror, or hybrid. **Mock/seeded Jira is acceptable for the initial MVP build.**
- Specific database engine, indexes, search technology, and schema details.
- Background queue/worker design, retry implementation, and production deployment topology.
- Specific LLM model and orchestration library; additional frameworks require demonstrated need.
- Final UI scope beyond what is needed to demonstrate reviews and investigation results.

These choices belong in the architecture/technology decisions document and must not be silently invented by an implementation agent.

## 8. Core Data and State Concepts

The system must represent, at minimum, these conceptual records (exact tables are an architecture decision):

| Concept | Minimum responsibility |
|---|---|
| Project / project membership | Isolation, actor role, and authorized access |
| Source document/reference | Source identity, type, project, timestamps, retention metadata |
| Business event | Atomic event, summary, business status, occurrence time, review state |
| Event source link | Traceability from an event to one or more permitted sources |
| Event–ticket link | Many-to-many association, link type, origin, review state |
| Jira issue context | Jira-recorded facts and explicit issue links, from an adapter or optional mirror |
| Investigation result | Question, referenced findings, hypotheses, unknowns, freshness, audit metadata |

**Required distinctions:**

- `occurred_at` is not the same as ingestion/creation time.
- `business_status` is not the same as `review_status`.
- `mapping_status` is not the same as client commitment approval.
- A reported correlation is not an established cause.

## 9. Acceptance Criteria and Demonstrations

All cases below require deterministic fixtures and explicit test assertions; AI-dependent behavior additionally needs a repeatable evaluation set.

### 9.1 Acceptance Criteria

- **AC-01:** One meeting can yield multiple distinct events without mandatory segment retention.
- **AC-02:** A client-requested date followed by PO deferral remains `REQUESTED_NOT_COMMITTED`.
- **AC-03:** A Jira bug created by QA before the client report remains discoverable and mappable.
- **AC-04:** Google Login is not incorrectly matched with Apple Login merely because both involve authentication or an assignee.
- **AC-05:** A Jira-recorded blocking issue can be included; same-assignee workload cannot become an invented dependency.
- **AC-06:** Unmapped events and unmapped tickets are valid states.
- **AC-07:** Mapping review is enforced and remains separate from business approval.
- **AC-08:** Timeline ordering uses occurrence time even if records arrive later.
- **AC-09:** The system does not invent verbatim/minute-level meeting evidence when it was not retained.
- **AC-10:** Investigations explicitly acknowledge missing evidence and unresolved causes.
- **AC-11:** Retrieval stays within configured depth, ticket/tool, and authorization limits.
- **AC-12:** Factual references resolve to accessible sources, with relevant freshness disclosed.

### 9.2 Required Demo Narratives

1. **Google Login:** A client bug report and a pre-existing QA issue with explicit blocker links, plus a parallel Apple Login assignment; no invented workload-based explanation.
2. **Sales Export deadline:** Client-requested date versus an actual PO commitment versus an internal Jira due date.
3. **Discount scope change:** The initial first-order discount is agreed and delivered; a later request to include returning customers is not automatically approved by the old ticket's `Done` status.

Example issue identifiers, actors, and dates are **synthetic test data**, not real Jira records.

## 10. Quality Attributes and Success Measures

**Correctness and trust**

- Extraction precision/recall and commitment-classification accuracy.
- Event–ticket mapping precision/recall, prioritizing **precision** over excessive linking.
- Valid evidence-reference rate and proportion of significant factual claims supported by evidence.
- No critical project-isolation or unauthorized-data disclosure in acceptance tests.

**Operational quality**

- Measured investigation latency, model tokens, and cost.
- Repeatable seeded tests and explicit regression gates.
- Recoverable errors and visible partial/truncated results rather than silent incorrect success.
- Reduced PO/PM time spent reconstructing customer conversations and Jira context (measured in demos when practical).

Numeric quality thresholds should be established with a representative test dataset; do not claim specific production SLAs before measurement.

## 11. MVP Definition of Done

The MVP can be declared complete only when:

- [ ] The three core workflows (extraction, mapping/review, investigation) operate end-to-end on permitted, reproducible examples.
- [ ] All twelve acceptance cases are implemented and pass their applicable checks/evaluations.
- [ ] The backend enforces project access, retrieval budgets, and read-only Jira boundaries.
- [ ] Review decisions preserve the distinction between association and business commitment.
- [ ] Significant factual output is tied to valid evidence references, or the result explicitly states uncertainty.
- [ ] The application can be launched in a reproducible local/demo environment.
- [ ] Regression test results and any known limitations are recorded.
- [ ] Final changes to product scope and architecture have been reviewed rather than silently introduced by an agent.

## 12. Planning and Change-Control Rules

- This document defines **product goals, requirements, scope, and non-negotiable invariants**.
- An architecture decision record defines **how** requirements will be implemented; it may not contradict this document without explicit review.
- A milestone goal defines a smaller delivery target, such as **Backend Foundation**; its steps cannot silently expand the master product scope.
- A coding agent may propose requirement or scope changes but **must not make them unilaterally**.
- Test failures, missing evidence, unresolved architecture decisions, and incomplete work must be reported explicitly.
- A checkbox marked complete in a planning document is not verification evidence. Completion requires the corresponding tests, evaluations, or review records.

---

**Next document to create:** `harness/milestones/003_BackendFoundation/goal.md`, a bounded Day-1 objective derived from this master goal. Do not generate implementation steps until that milestone goal and its verification gates are approved.
