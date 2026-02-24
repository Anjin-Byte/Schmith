# Typed Python Architecture and Development Guidelines

## 1. Purpose and Scope

This document defines standards for building large Python systems with strong static typing and predictable modular architecture.

Goals:

- Keep systems maintainable as team size and code volume grow.
- Enforce strict type safety (Pylance/Pyright strict mode).
- Make behavior easy to test at unit, integration, and system levels.
- Prevent architectural drift by using consistent composition and boundaries.

This applies to:

- Services and applications.
- Shared libraries.
- Domain modules and infrastructure modules.
- Test code and CI quality gates.

---

## 2. Core Architecture Principles

### 2.1 Design for Explicit Boundaries

Large systems should be organized into bounded contexts (business capabilities), then layered by responsibility.

Recommended layers:

1. `domain`: Pure business rules and entities.
2. `application`: Use-cases/orchestration.
3. `infrastructure`: External systems (DB, HTTP, message brokers, files).
4. `interfaces`: Entry points (CLI, HTTP handlers, workers).

Rules:

- `domain` must not import from `infrastructure` or interface frameworks.
- `application` may depend on `domain`, and on abstract protocols for external dependencies.
- `infrastructure` implements protocols defined by `application`/`domain`.
- Interface layer wires dependencies in the composition root.

### 2.2 Dependency Inversion by Protocol

Use `typing.Protocol` for ports.

- Application logic accepts protocol interfaces, not concrete clients.
- Infrastructure modules provide concrete adapters.
- Swap adapters in tests with typed fakes/stubs.

### 2.3 Composition Root

Create one composition root per deployable process that wires concrete implementations.

- No hidden global singletons.
- No implicit side effects on import.
- Dependency graph should be visible in one place for each runtime entrypoint (API server, CLI app, worker, scheduler).

### 2.4 Data Contracts Are Explicit

Use typed DTOs for external I/O boundaries:

- Prefer `dataclass(frozen=True, slots=True)` for immutable structures.
- Use explicit parsing/validation at boundaries.
- Do not pass raw `dict[str, Any]` through core layers.

---

## 3. Type System Standards (Strict Pylance/Pyright)

### 3.1 Required Settings

Pylance uses Pyright type analysis. Use strict mode and fail CI on type errors.

Recommended `pyrightconfig.json`:

```json
{
  "typeCheckingMode": "strict",
  "pythonVersion": "3.12",
  "stubPath": "typings",
  "include": ["src", "tests", "tools"],
  "exclude": ["**/__pycache__", ".venv", "dist", "build"],
  "reportMissingTypeStubs": "warning",
  "reportUnknownVariableType": "error",
  "reportUnknownMemberType": "error",
  "reportUnknownArgumentType": "error",
  "reportUnknownParameterType": "error",
  "reportUnknownLambdaType": "error",
  "reportUnknownReturnType": "error",
  "reportUntypedFunctionDecorator": "error",
  "reportUntypedClassDecorator": "error",
  "reportUntypedBaseClass": "error",
  "reportUntypedNamedTuple": "error",
  "reportPrivateImportUsage": "error"
}
```

### 3.2 Annotation Rules

- All public functions, methods, and class attributes must be explicitly typed.
- Internal functions should also be typed; avoid implicit `Any`.
- Never use bare containers like `list` or `dict`; always parameterize.
- Prefer `Sequence[T]`, `Mapping[K, V]`, and immutable interfaces for inputs.
- Return concrete, stable types from public APIs.

### 3.3 `Any` and Dynamic Behavior

- `Any` is disallowed in domain and application code.
- `Any` is also disallowed in public function signatures across all layers.
- If dynamic content is unavoidable:
  - Isolate it in boundary adapters only (HTTP/DB/message/file integration edges).
  - Convert to typed DTOs immediately after parsing.
  - Document conversion assumptions.
- Quarantine rule:
  - `Any` may exist only in a short parsing zone.
  - Parsed values must be narrowed/validated before crossing into application/domain modules.
  - `Any` must not be returned from adapter interfaces.

### 3.4 Narrowing and Validation

- Use `TypeGuard`/`assert` and dedicated validators to narrow unknown data.
- Avoid unchecked casts. `cast()` requires a comment explaining why it is safe.

### 3.5 Exceptions and Result Types

- Prefer typed domain exceptions over generic `Exception`.
- For expected business failures, consider typed `Result`/error objects.
- Do not leak transport-layer exceptions (HTTP client errors, DB exceptions) into domain layer.

### 3.6 Third-Party Typing and Stub Policy

- Prefer libraries with first-class type hints or published `types-*` stubs.
- If a required dependency lacks type hints:
  - Add local stubs under `typings/`.
  - Or wrap the dependency behind a typed adapter and isolate untyped calls.
- Temporary suppressions for missing stubs must include:
  - A tracked work item ID.
  - Owner.
  - Expiration date.
- CI should block net-new missing-stub warnings unless explicitly allowlisted with expiration.

---

## 4. Project and File Organization

## 4.1 Standard Workspace Layout

```text
repo/
  pyproject.toml
  pyrightconfig.json
  README.md
  docs/
    architecture/
      system-overview.md
      decision-records/
    standards/
      typed-python-guidelines.md
  src/
    my_system/
      __init__.py
      bootstrap/                # composition root, DI wiring
      shared/                   # cross-cutting utilities, typed primitives
      context_a/
        domain/
          entities.py
          value_objects.py
          services.py
          events.py
          errors.py
          protocols.py
        application/
          commands.py
          queries.py
          handlers.py
          dto.py
        infrastructure/
          repositories/
          clients/
          persistence/
          mappers.py
        interfaces/
          http/
          cli/
          workers/
      context_b/
        ...
  tests/
    unit/
      context_a/
      context_b/
    integration/
      context_a/
      context_b/
    contract/
      api/
      messaging/
    e2e/
    fixtures/
    conftest.py
  tools/
    scripts/
    quality/
```

### 4.2 Module Size and Cohesion Rules

- Prefer small modules with one dominant responsibility.
- Split files before they exceed maintainability thresholds.
  - Soft threshold: 300 lines.
  - Hard threshold: 500 lines (requires refactor plan).
- Avoid “god modules” (e.g., one service file with unrelated behaviors).

### 4.3 Import Discipline

- Use absolute imports from `src` package root.
- Forbid cyclic imports in CI.
- Keep cross-context access behind explicit application APIs or shared contracts.

### 4.4 Shared Package Governance

`shared/` is often abused. Restrict it to:

- Cross-cutting primitives (`Clock`, typed IDs, pagination types).
- Framework-neutral helpers.
- No business logic specific to one context.

---

## 5. Layer Responsibilities

### 5.1 Domain Layer

Must contain:

- Entities/value objects with invariants.
- Domain services and policies.
- Domain events and typed errors.

Must not contain:

- HTTP/SQL code.
- Framework annotations.
- Logging side effects except through abstracted port if needed.

### 5.2 Application Layer

Must contain:

- Use-case handlers.
- Transaction boundaries (if applicable).
- DTO mapping between domain and interfaces.

Rules:

- One use-case per command/query handler.
- Handlers should be orchestration-focused and thin.
- Business rules remain in domain objects/services.

### 5.3 Infrastructure Layer

Contains concrete adapters:

- Repository implementations.
- API clients.
- Queue publishers/consumers.
- File/storage adapters.

Rules:

- Validate and map external payloads into typed boundary models.
- Keep retry/backoff/circuit-breaker behavior at this layer.
- Never expose raw transport types into domain/application.

### 5.4 Interface Layer

Examples:

- FastAPI routers.
- CLI commands.
- Job workers.

Rules:

- Parse request -> call application handler -> map response.
- No business rule branching in handlers/controllers.
- All dependencies resolved through bootstrap/composition root.

---

## 6. Typing Patterns for Large Systems

### 6.1 Strongly Typed IDs and Value Objects

Avoid mixing primitive IDs:

```python
from typing import NewType

EmployeeId = NewType("EmployeeId", int)
CompanyId = NewType("CompanyId", int)
```

### 6.2 Protocol-Driven Ports

```python
from typing import Protocol

class EmployeeReader(Protocol):
    async def get_employee(self, employee_id: EmployeeId) -> Employee | None: ...
```

### 6.3 Immutable DTOs

```python
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class EmployeeSnapshot:
    id: EmployeeId
    email: str
    is_active: bool
```

### 6.4 Typed Config

- Load config once in bootstrap layer.
- Validate into typed config object.
- Inject config object into adapters/services.

---

## 7. Error Handling and Observability Standards

### 7.1 Error Taxonomy

Use explicit classes:

- `DomainError`
- `ValidationError`
- `NotFoundError`
- `ConcurrencyError`
- `ExternalDependencyError`

### 7.2 Logging

- Use structured logs (key-value).
- Include correlation IDs and context identifiers.
- Do not log secrets or PII.

### 7.3 Metrics and Tracing

Capture:

- Latency per use-case.
- External dependency success/failure rates.
- Retry counts, timeout counts.
- Queue lag and dead-letter metrics.

---

## 8. Testing Standards (Thoroughness and Organization)

### 8.1 Test Pyramid Targets

Target ratio:

- Unit tests: 70%
- Integration tests: 20%
- Contract and end-to-end tests: 10%

### 8.2 Required Test Types

1. Unit tests
   - Domain invariants.
   - Application orchestration with mocked/fake ports.
   - Pure mapping and validation functions.
2. Integration tests
   - Repository behavior against real test DB.
   - External client adapters using mock server or sandbox.
3. Contract tests
   - Verify API payload compatibility for each external integration.
   - Snapshot schema checks for critical payloads.
4. End-to-end tests
   - Minimal but high-value business flows.
   - Validate bootstrap wiring and runtime config.

### 8.3 Test Workspace Organization

Rules:

- Mirror production package structure under `tests/unit` and `tests/integration`.
- Keep reusable fixtures in `tests/fixtures`.
- Keep test data in dedicated folders near tests.
- For each context, organize tests by layer:
  - `tests/unit/context_a/domain/...`
  - `tests/unit/context_a/application/...`
  - `tests/integration/context_a/infrastructure/...`

### 8.4 Thoroughness Requirements

For each use-case handler, minimum expectations:

- Success path.
- Validation failure path.
- Dependency error path.
- Idempotency/retry behavior (if applicable).
- Edge cases (empty input, null-equivalent, boundary values).

For each domain entity/value object:

- Constructor/creation invariants.
- Mutation rules.
- Equality and hashing semantics (if implemented).

For each adapter:

- Happy path payload mapping.
- Unexpected/malformed payload handling.
- Timeout/retry/error conversion behavior.

### 8.5 Coverage and Quality Gates

Suggested minimums:

- Line coverage: 90% for domain/application packages.
- Branch coverage: 80% overall.
- Critical module coverage floor: 95%.

Coverage alone is not enough. PRs must include:

- Assertions on business behavior (not just execution).
- Negative path tests for failure handling.
- Regression tests for bug fixes.

### 8.6 Deterministic Testing Rules

- No real network calls in unit tests.
- Freeze time via clock abstraction.
- Seed randomness for reproducibility.
- Avoid sleeps; use awaitable synchronization primitives.

---

## 9. CI/CD Enforcement

Minimum required CI stages:

1. `ruff check` (or equivalent linting).
2. `ruff format --check` (or formatter check).
3. `pyright` strict run.
4. `pytest` unit suite.
5. `pytest` integration suite.
6. `pytest` contract suite for changed integrations.
7. End-to-end smoke suite.
8. Coverage threshold enforcement.
9. Optional: mutation testing for critical domain modules.

Execution policy:

- Unit and integration tests run on every PR.
- Contract tests must run on every PR that changes external API/messaging adapters or schemas.
- End-to-end smoke tests run on merge to main and before release; teams may also require them on PR for high-risk changes.

Build fails on:

- Any Pyright error.
- Any lint/format error.
- Any executed test failure (unit, integration, contract, end-to-end smoke).
- Coverage below thresholds.
- Net-new missing-stub warnings that are not on an approved allowlist.

### 9.1 Enforceable Quality Gate Commands

Use explicit, scriptable commands in CI.

Example:

```bash
ruff check src tests tools
ruff format --check src tests tools
pyright
pytest tests/unit -q --maxfail=1 --disable-warnings --cov=src --cov-branch --cov-report=xml --cov-report=term-missing
pytest tests/integration -q --maxfail=1 --disable-warnings
pytest tests/contract -q --maxfail=1 --disable-warnings
pytest tests/e2e -q --maxfail=1 --disable-warnings -m smoke
python tools/quality/check_coverage_thresholds.py coverage.xml
python tools/quality/check_missing_stubs_allowlist.py
```

Coverage threshold checker should validate:

- Overall branch coverage >= 80%.
- Domain/application line coverage >= 90%.
- Critical package/module floors >= 95%.

Contract and e2e jobs may be conditionally executed by change scope, but when executed they are required to pass.

---

## 10. Code Review Checklist

Reviewers should verify:

1. Types
   - No new `Any` leakage outside approved boundary parsing zones.
   - Public APIs fully typed.
   - No unnecessary casts.
2. Architecture
   - Layer boundaries respected.
   - No infrastructure imports in domain.
   - New dependency wired through composition root.
3. Modularity
   - Module size/cohesion acceptable.
   - No hidden side effects at import time.
4. Testing
   - Positive and negative cases covered.
   - Tests located in correct workspace structure.
   - Critical behavior covered with assertions.
5. Observability/Safety
   - Errors mapped consistently.
   - Logs structured and safe.
   - Timeouts/retries explicit for external calls.

---

## 11. Definition of Done for New Features

A feature is complete only when:

1. Code compiles and passes strict Pyright/Pylance checks.
2. Layer boundaries and protocol-driven design are respected.
3. Required tests are added and passing for change scope (unit/integration always; contract and end-to-end smoke when applicable).
4. Coverage thresholds remain satisfied.
5. Docs are updated:
   - Architecture impact summary.
   - Public API/contract changes.
   - Operational notes if needed.

---

## 12. Recommended Tooling Baseline

- Python 3.12+
- Pyright (strict)
- Pylance in editors
- Ruff (lint + format)
- Pytest + pytest-cov
- Hypothesis for property-based tests (where useful)
- Pre-commit for local enforcement

Example baseline commands:

```bash
ruff check src tests tools
ruff format --check src tests tools
pyright
pytest -q --maxfail=1 --disable-warnings --cov=src --cov-report=term-missing
```

---

## 13. Adoption Plan for Existing Codebases

For legacy code, adopt incrementally:

1. Enable Pyright strict for new/modified modules first.
2. Introduce Protocol ports around highest-risk dependencies.
3. Split oversized modules by context and layer.
4. Add missing tests around business-critical flows.
5. Remove `Any` hotspots and unchecked casts.
6. Raise CI gates over time until full strict compliance.

Track progress with:

- Typed module percentage.
- Strict-check pass rate.
- Coverage trend by package.
- Defect escape rate for integration failures.

---

## 14. Anti-Patterns (Disallowed)

- Business logic in controllers/routes/CLI handlers.
- Global mutable state shared across contexts.
- Raw `dict` payloads crossing domain boundaries.
- Catch-all `except Exception` with silent fallback.
- Unbounded module growth and circular imports.
- Skipping strict typing due to “temporary” shortcuts.

---

## 15. Final Standard

Large Python systems in this workspace should be:

- Strictly typed and statically validated.
- Architecturally segmented by context and layer.
- Composed via explicit dependency wiring.
- Covered by thorough, organized, deterministic tests.
- Enforced by CI quality gates, not manual convention alone.

These rules are intended to make correctness, maintainability, and operational reliability the default outcome at scale.
