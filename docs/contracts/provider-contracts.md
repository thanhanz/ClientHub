# Provider Contracts — Mock-first adapters

> Status: REVIEW CANDIDATE. Ports are C#-style examples, not generated source. Authorization is *always* enforced by backend application services; providers are insufficient as the sole access control.

## 1. External source reader (mock now / permitted providers later)

```csharp
public interface IExternalSourceReader
{
    Task<NormalizedSource?> GetAsync(
        SourceLocator locator, CancellationToken cancellationToken);
    Task<SourcePage> ListAsync(
        SourceQuery query, CancellationToken cancellationToken);
}
```

`SourceLocator = { projectId, sourceType, providerInstanceKey, externalSourceId }`.

`NormalizedSource` must contain: `projectId`, `sourceType (EMAIL|CHAT|MEETING)`, `providerInstanceKey`, `externalSourceId`, `occurredAt`, `actorKind`, optional verified actor metadata, `retentionMode`, `visibilityClass (PROJECT_MEMBERS|PO_PM_ONLY)`, `permittedText` for policy-allowed message text or `approvedNotes` for meeting notes, source title, `observedAt`, permission/visibility metadata. A meeting may carry **only metadata + approved notes**, with no transcript segments.

Normalize provider-specific sender IDs, timestamps and content types at the adapter boundary. `actorKind` must come from verified membership/sender metadata or be `UNKNOWN` (not guessed by an LLM). Pagination returns an opaque cursor and deterministic ordering. Providers must not return sources from another project as though authorized.

## 2. Jira issue reader

```csharp
public interface IJiraIssueReader
{
    Task<NormalizedJiraIssue?> GetIssueAsync(
        JiraIssueLocator locator, CancellationToken cancellationToken);

    Task<JiraIssuePage> SearchIssuesAsync(
        JiraIssueSearchQuery query, CancellationToken cancellationToken);

    Task<IReadOnlyList<NormalizedJiraIssueLink>> GetIssueLinksAsync(
        JiraIssueLocator locator, CancellationToken cancellationToken);
}
```

`JiraIssueLocator = { projectId, jiraInstanceKey, issueKey }`.

`NormalizedJiraIssue` required: `jiraInstanceKey`, `issueKey`, associated Hub `projectId` (validated mapping), `summary`, `status`, `observedAt`; optional `assigneeId`, `descriptionExcerpt`, `parentKey`, `updatedAt`, `history` and `comments` with their own visibility restrictions. Jira status means **what Jira records**, not verified real-world activity.

`NormalizedJiraIssueLink` required: `jiraInstanceKey`, `fromIssueKey`, `toIssueKey`, `relationType`, `observedAt`, `source=JIRA_EXPLICIT_LINK`; `relationType` includes `BLOCKS`, `BLOCKED_BY`, `PARENT_OF`, `CHILD_OF`, `RELATES_TO` with normalized direction, and the adapter must document Jira-specific link interpretation. Do **not** derive a Jira issue link from same assignee, keyword similarity, or AI proposals.

`JiraIssueSearchQuery` must include Hub `projectId`, allowed provider instance(s), text/key filter, page limit and cursor. Backend caps candidate count and total calls; provider pagination must not bypass budgets. `GetIssueLinksAsync` returns actual links for permitted issues and source observation timestamps.

## 3. Mock implementation requirements

- Deterministic seed fixtures for three key demos: Google Login, Sales Export, Discount scope mismatch; include non-matching/negative issues.
- Support an explicit blocker `AUTH-101 is blocked by AUTH-102` and independent concurrent Apple Login `AUTH-103`; ticket linkage **only** via an explicit fixture record.
- Provide cases for not-found, forbidden project, timeout, stale/partial result and cyclic links.
- Mock Jira never mutates tickets; it is test input, not an operational issue store.
- Define ground truth separately from input fixture; do not compute expected answer using the same model under test.

## 4. Failure types

| Condition | Normalized signal | Backend behavior |
| --- | --- | --- |
| Not found | `null` or typed not-found result | Report absent, do not invent data |
| Permission denied | `ProviderForbidden` | Return safe access error; avoid information leak |
| Timeout/rate limit | `ProviderTransientError` | Bounded retry in later job processing or partial result |
| Schema/data conflict | `ProviderDataInvalid` | Reject item; preserve structured diagnostics |
| Missing optional Jira field | `null` + freshness/coverage metadata | Do not infer a value |
| Pagination exhausted/budget | page with `nextCursor` or stop flag | Backend limits still apply |

## 5. Shared adapter contract tests

`PR-01` issue lookup returns same canonical identity; `PR-02` issue link direction retained; `PR-03` search respects provider/HUB project filters; `PR-04` pagination does not drop or duplicate within snapshot; `PR-05` missing optional fields remain unknown; `PR-06` source actor role is metadata-derived; `PR-07` meeting metadata can exist without a transcript; `PR-08` timeouts/errors are normalized; `PR-09` all methods are read-only; `PR-10` both Mock and Real adapters pass the same tests where provider capability exists.

## 6. Real integration migration gate (deferred)

Before calling a real integration ready, run a bounded sandbox contract spike: verify user/app credentials, issue search and links APIs, real pagination, changelog access, permissions, redaction, timezone, rate limits, and mapping from real project to Hub project. Do not widen AI access to solve provider gaps.
