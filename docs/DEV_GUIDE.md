# Developer Guide

## Typed Python Policy

All Python code in this repository should be fully typed.

- Add explicit type hints for function signatures, return values, and key variables.
- Use standard typing constructs from `typing` (e.g., `Optional`, `List`, `Dict`, `TypedDict`).
- Prefer data classes and well-defined models when shaping data across modules.
- Avoid `Any` unless there is no reasonable alternative; document why when used.
- Keep types up to date as interfaces evolve.

## Typed Data Boundaries

When working with untyped external data (API specs, JSON/YAML), choose the lightest approach that keeps typing useful.

### Explicit casts
- Use when you know the shape from context or after a guard.
- Good for small, localized narrowing of `Any` or `dict`.
- Trade-off: can hide mistakes if overused.

### Type guards
- Use `isinstance` checks or helper validators to narrow types safely.
- Best for boundary layers where data may be malformed or incomplete.
- Trade-off: more code, but improves runtime safety.

### `TypedDict` / Protocol models
- Use when the schema is stable and reused in multiple places.
- Best for shared structures like IR models or well-defined spec fragments.
- Trade-off: more upfront modeling and maintenance.

### Rule of thumb for this repo
- Ingestion adapters: prefer guards + small casts to contain `Any`.
- IR + analysis code: prefer full typing with models.
