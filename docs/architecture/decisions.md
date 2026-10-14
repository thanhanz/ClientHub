# Technical decisions and open questions

> Status: **PROPOSED BASELINE / OWNER REVIEW REQUIRED**. Values below must not be represented as previously finalized where the Product Goal calls them deferred.

| ID | Topic | Baseline for design | Status | Why / boundary |
| --- | --- | --- | --- | --- |
| ADR-001 | Data and authority | ASP.NET Core owns durable business data, access control, orchestration, bounded retrieval, output verification, audit | USER-DIRECTED | Python may not bypass backend authorization or own business decisions |
| ADR-002 | AI boundary | Stateless Python/FastAPI inference service receiving backend-prepared inputs and returning structured output | USER-DIRECTED | No DB or Jira credentials in AI service |
| ADR-003 | External integration | Mock-first provider adapters; deterministic scenarios; later replace adapters with real sources | USER-DIRECTED | Mock behavior must not be mistaken for verified real integration |
| ADR-004 | Backend runtime | ASP.NET Core modular monolith, C#; feature-oriented modules | PROPOSED | Simple deploy, strong internal contracts; avoid premature microservices |
| ADR-005 | Persistence | PostgreSQL + EF Core migrations | PROPOSED | Relational integrity for project/source/event/mapping/audit; explicit migrations |
| ADR-006 | Jira access | `IJiraIssueReader` read-only port, seeded provider first, later Jira REST adapter; optional MCP/hybrid evaluated separately | PROPOSED | Jira stays authoritative; no speculative local mirror requirement |
| ADR-007 | LLM orchestration | Backend-controlled code paths; Python extraction/mapping/synthesis requests; no multi-agent framework requirement | PROPOSED | Narrow, testable, bounded workflows |
| ADR-008 | Jobs | Backend Foundation may execute seeded/manual use cases synchronously; idempotent job processing designed before live asynchronous ingestion | PROPOSED | Avoid implementing a fragile in-memory queue as durable delivery |
| ADR-009 | Identity | Authentication pluggable; test identity scheme ONLY in Test/Development; project membership enforced by backend | PROPOSED | Never trust client-supplied user/role headers in production |
| ADR-010 | Search | Deterministic normalized keyword/key search for seeded MVP; evaluate full-text/vector only with measured need | PROPOSED | No mandatory vector DB or LLM retrieval |
| ADR-011 | Deployment | Docker Compose for local/demo; migration + seed commands explicit | PROPOSED | Reproducible backend milestone |
| ADR-012 | Source retention | Meeting-level references and approved notes acceptable; raw transcript not mandatory; retention controlled per source | AGREED PRODUCT DIRECTION | No fictional verbatim/minute-level evidence |

## Open implementation design questions

- Which production identity provider and organization provisioning process will be used?
- Which exact Jira workspace(s), REST permissions, rate limits, and field mappings apply?
- Are actual email/chat message bodies allowed to be durably retained, and for how long?
- Which AI provider/model, schema-constrained output mode, timeout and budget are accepted?
- Is background processing backed by a database jobs table, an outbox, or an external queue after the backend foundation?
- What operational latency, cost and evaluation thresholds can be established with real measurements?

## Decision protocol

To approve: owner changes `Status` in this file to `APPROVED` with date and records any trade-off. A coding agent may only propose edits. Scope-affecting decisions require updates to product goal first. Any new optional technology needs an evidence-based reason (specific acceptance failure, operational limitation or measurable benefit).
