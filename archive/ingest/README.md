# Ingest Module

This package owns API spec ingestion and normalization into the IR used by analysis.
Adapters should be strict, predictable, and defensively typed because all downstream
reports rely on their output.

## IR Contract (ResponseSchema)

Adapters must yield `ingest.model.ResponseSchema` objects with:
- `method`: lowercased HTTP method string.
- `path`: request path as defined in the spec.
- `code`: response status code string.
- `root_type`: `"object"`, `"array"`, or `None` when unknown.
- `properties`: list of object properties (normalized dicts).
- `items`: array item schema dict when `root_type == "array"`, else `None`.

## Adapter Responsibilities

When implementing or modifying an adapter:
- Parse only supported spec formats and normalize them into `ResponseSchema`.
- Use explicit guards (`isinstance`) for JSON/YAML data to avoid `Any` leakage.
- Resolve `$ref`/`allOf` (OpenAPI) or analogous constructs (RAML) where possible.
- Skip endpoints without usable JSON response schemas.
- Keep output stable; avoid adding fields to `ResponseSchema` without updating all consumers.

## Runtime Validation

Adapters call `ingest.validation.validate_response_schema` before yielding a schema:
- If `pydantic` is installed, it validates the model structure.
- Otherwise, a manual check runs with a strict error message.

Optional runtime type checks (via `typeguard`) wrap adapter entrypoints when available.

## Adding a New Adapter

1) Implement a class with `name`, `load_spec`, and `iter_response_schemas`.
2) Register it in `ingest/spec_adapters/__init__.py`.
3) Ensure it yields valid `ResponseSchema` instances and passes validation.
4) Add tests or a fixture spec when possible.
