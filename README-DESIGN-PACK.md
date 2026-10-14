# ClientHub design documentation

Architecture and contracts are maintained under docs/architecture and docs/contracts. Their reviewed subset and remaining proposed choices are recorded in [decisions](docs/architecture/decisions.md).

Use the single [numbered milestone roadmap](harness/README.md): 001 design, 002 harness, 003 ingestion/backend, 004 extraction/events, 005 mapping, 006 investigation, 007 demonstration. The imported unnumbered milestone definitions have been consolidated into these review packages; they are not an alternative execution plan.

Start at the [design checklist](harness/milestones/001_DesignFoundation/design-checklist.md). Run py scripts/validate-contracts.py for structural/example/reference checks; these checks do not verify runtime authorization or AI semantic correctness.

Approve each milestone's detailed gates separately before execution. Mock providers are sufficient for this demo; production connector validation is deferred.
