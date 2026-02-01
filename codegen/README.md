# Codegen

LLM-driven C# DataObject generation from IR.

## What Lives Here

- `cli.py`: Unified CLI (`python -m codegen ...`).
- `config.toml`: Paths + LLM settings.
- `filters.toml`: Centralized schema filters (include/exclude rules).
- `generation/`: Prompt packet builder and code generator.
- `ir/`: IR loader + composition resolver.
- `schema/`: Schema filtering + C# type mapping.
- `providers/`: LLM provider adapters (Anthropic/OpenAI).

## Common Commands

```bash
# Show config + filters
uv run python -m codegen config

# List DataObjects for an IR (filtered by filters.toml)
uv run python -m codegen list paycore -v

# Show parent-child schema groups
uv run python -m codegen groups paycore

# Generate prompt packets
uv run python -m codegen packets paycore

# Generate C# code
uv run python -m codegen generate paycore
uv run python -m codegen generate paycore --no-clean

# Coverage report (writes generated/<ir>/_reports/coverage.md)
uv run python -m codegen coverage paycore

# Endpoint response coverage report (writes generated/<ir>/_reports/endpoints.md)
uv run python -m codegen endpoints paycore
```

## Configuration Notes

- `config.toml` controls paths, LLM provider, and prompt paging.
- `filters.toml` controls what schemas become DataObjects.
- `generation/prompts.json` overrides the base instructions and example code used in prompts.

## Outputs

- Prompt packets: `prompt_packets/grouped/<ir>/`
- Generated code: `generated/<ir>/_source/` (symlinked into object folders)
- Schema markdown: `generated/<ir>/_schemas/` (symlinked into object folders)
- Coverage report: `generated/<ir>/_reports/coverage.md`
- Manifest: `generated/<ir>/manifest.json`

Notes:
- `codegen generate --dry-run` still writes scaffolding and manifest, but skips LLM calls and `.cs` output.
- Output directories are cleaned by default; use `--no-clean` to keep existing files.
- Composition handling: `allOf` is flattened; `oneOf`/`anyOf` remain unions (no merging). If you opt to coerce `oneOf`/`anyOf` into an `allOf`-style merge, that intentionally widens the shape and should be documented for downstream consumers.

## Prompt Packet Details

- Uses type-tree resolution to collect all reachable types.
- Composition-only members are excluded from nested schema sections.
- Inline enums are assigned stable names derived from parent + field name.
- Field metadata (read-only/write-only/deprecated) and constraints are surfaced in prompts.
