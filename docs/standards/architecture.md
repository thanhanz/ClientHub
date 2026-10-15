## Architecture Guardrails

- Prefer a modular monolith over microservices.
- Follow SOLID pragmatically, not dogmatically.
- Keep application orchestration separate
  from infrastructure.
- Define interfaces at external boundaries
  or genuine variation points.
- Do not create interfaces for every class.
- Avoid unnecessary factories, generic
  repositories, mediator layers or event buses.
- Keep external provider DTOs separate
  from domain models.
- Use dependency injection for replaceable
  dependencies.
- Keep classes focused and methods readable.
- Do not introduce abstractions for hypothetical
  future requirements.
- Preserve existing contracts unless required.
- Add unit tests for business rules and
  integration tests for external boundaries.
- Explain the concrete need for each
  new abstraction.# Architecture Engineering Standards

## 1. Design Philosophy
- Prefer simplicity over speculative extensibility.
- Follow SOLID pragmatically.
- Prefer a modular monolith.
- Apply YAGNI.

## 2. Dependency Boundaries
- Domain must not depend on infrastructure.
- Application orchestrates through contracts.
- Infrastructure implements integrations.
- External DTOs must not leak into domain.

## 3. Abstraction Rules
- Use interfaces for genuine variation points.
- Do not create an interface for every class.
- Avoid unnecessary factories, repositories,
  mediator layers and event buses.
- Justify new abstractions.

## 4. Extensibility Rules
- New sources should not change business rules.
- Replacing an LLM provider should not
  require rewriting application orchestration.
- Preserve existing contracts.
- Prefer composition when appropriate.

## 5. Verification
- Unit-test business rules independently.
- Verify dependency boundaries.
- Test adapter contracts when valuable.
- Require evidence of compliance.