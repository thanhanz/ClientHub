# Technology Baseline — ClientHub

> Status: **PROPOSED implementation baseline**, subject to owner approval in `decisions.md`. This design targets the project already visible as `ClientHub.slnx`, `src/Hub.Api`, `tests/Hub.Tests` and a .NET 10 build tree. It does not assert the repository has these dependencies installed yet.

## Stack for Backend Foundation M1

| Concern | Proposed choice | Implementation note |
| --- | --- | --- |
| Application API | ASP.NET Core on .NET 10 | Keep a single deployable backend; feature folders rather than multiple prematurely separated projects |
| Language | C# | Nullable reference types, async APIs, cancellation tokens |
| ORM and migrations | EF Core with Npgsql provider | Use compatible major versions with pinned tested packages; explicit migrations |
| Primary relational storage | PostgreSQL | Test against a real isolated PostgreSQL instance, not only EF InMemory |
| Integration tests | xUnit + `WebApplicationFactory` + isolated PostgreSQL | Enforce auth, persistence, state transitions and seed idempotency |
| Development environment | Docker Compose for DB/API | Use pinned, reviewable container tags and environment-specific secrets |
| Jira mock | `IJiraIssueReader` + versioned JSON fixtures | Explicit Jira links, realistic pagination and failure behavior |
| Source mocks | `IExternalSourceReader` + approved notes/communications fixtures | No external email/chat/meeting credentials in M1 |
| Structured API errors | RFC 7807 ProblemDetails | Stable machine-readable errors and correlation ID |
| Observability | .NET structured logging and correlation IDs | Never log raw secrets/transcript bodies indiscriminately |
| Verification | `dotnet build`, `dotnet test`, schema validation, DB migration + API smoke tests | CI/harness records actual exit codes and verified Git commit |

## Post-M1, not required for backend foundation

- Python + FastAPI for isolated structured LLM inference.
- Provider-specific Jira REST/source adapter implementations after mock and sandbox contract tests.
- A **durable** job mechanism selected based on measured workflow need, not an untracked fire-and-forget Task.
- Frontend UI for PO/PM review and investigation.

No mandatory LangGraph, Kafka, Redis, graph DB, vector DB or ticket mirror for the baseline.

## Suggested feature layout (not a required refactor of existing code)

```text
src/Hub.Api/
  Features/
    Projects/
    Sources/
    Events/
    Mappings/
    Investigations/
  Infrastructure/
    Persistence/
    Security/
    Jira/
    ExternalSources/
    Audit/
  Contracts/
tests/Hub.Tests/
  Unit/
  Integration/
  Acceptance/
```

Before creating implementations, inspect actual project files (`Hub.Api.csproj`, `Hub.Tests.csproj`, `global.json`, Dockerfile, compose.yaml). Do not guess installed EF/provider versions or silently overwrite configured infrastructure.

## Early quality gate

Backend Foundation cannot be declared complete without startup/migration on clean PostgreSQL, isolated API integration tests enforcing project/source access, and a deterministic context bundle contract test executed without Python.
