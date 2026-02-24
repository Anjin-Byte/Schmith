# Builders

IR build pipeline that normalizes API specs (OpenAPI/RAML) into the Schmith IR.

## Domains

Each builder writes into `ir/<api>/`:

- `build_operations.py`: endpoints, parameters, request/response bodies
- `build_schemas.py`: type definitions, fields, constraints
- `build_serialization.py`: media types + JSON field names
- `build_refs.py`: schema relationships and dependency graph

## Adapters

Adapters live in `builders/adapters/` and implement spec parsing for:

- OpenAPI 3.x
- RAML 1.0

Use `--adapter openapi` or `--adapter raml` when running builders.

Adapter notes:
- Field metadata (nullable, readOnly/writeOnly, deprecated) and constraints are captured into the IR.
- OpenAPI adapter collapses pure single-ref `allOf` wrappers to preserve referenced schema names.
- Composition in IR records `allOf`/`oneOf`/`anyOf`. Only `allOf` is flattened by default; `oneOf`/`anyOf` are preserved as unions unless a downstream merge policy is enabled.

## Example

```bash
uv run python builders/build_operations.py --config configs/paycore.toml --adapter openapi
uv run python builders/build_schemas.py --config configs/paycore.toml --adapter openapi
uv run python builders/build_serialization.py --config configs/paycore.toml --adapter openapi
uv run python builders/build_refs.py --config configs/paycore.toml
```

## Config

Builders read `configs/<api>.toml` (or `config.toml`) for:

- `api.name`
- `spec.url` (local path or URL)
- `output.spec_dir` / `output.reports_dir`
