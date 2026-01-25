# Archived Code

This directory contains code and documentation that has been superseded or completed.

## Archived Scripts

| File | Replaced By | Date |
|------|-------------|------|
| `generate_prompt_packets.py` | `codegen/prompt_packets.py` | 2026-01-24 |
| `generate_grouped_packets.py` | `codegen/prompt_packets.py` | 2026-01-24 |
| `generate_data_objects.py` | `codegen/code_generator.py` | 2026-01-24 |
| `list_xchange_objects.py` | `codegen/cli.py` (list command) | 2026-01-24 |

## Archived Documentation

| File | Reason | Date |
|------|--------|------|
| `IR_MIGRATION_PLAN.md` | Migration completed | 2026-01-24 |
| `IR_PHASE0_CHECKLIST.md` | Phase 0 completed | 2026-01-24 |
| `IR_PHASE2_TASKS.md` | Phase 2 completed | 2026-01-24 |
| `MIGRATION_GUIDE.md` | Project restructuring completed | 2026-01-24 |

## Archived Modules

| Directory | Reason | Date |
|-----------|--------|------|
| `ingest/` | Legacy spec parsing; replaced by `builders/` adapters | 2026-01-24 |
| `tools/` | Legacy analysis utilities; only consumer of `ingest/` | 2026-01-24 |

### `ingest/` Contents
- `adapter.py` - Spec adapter loader
- `model.py` - ResponseSchema dataclass
- `validation.py` - Runtime type checking
- `spec_adapters/` - OpenAPI and RAML adapters

### `tools/` Contents
- `identify_list_detail.py` - List vs detail endpoint detection
- `build_type_graph.py` - Type relationship graph builder
- `build_endpoint_model.py` - Normalized endpoint model builder
- `sync_spec.py` - Spec fetcher and summarizer

## New Usage

The functionality from these scripts is now available via the unified CLI:

```bash
# List DataObjects (replaces list_xchange_objects.py)
python -m codegen list servicefusion

# Generate prompt packets (replaces generate_prompt_packets.py)
python -m codegen packets servicefusion

# Generate grouped packets (replaces generate_grouped_packets.py)
python -m codegen packets servicefusion --grouped

# Generate C# code (replaces generate_data_objects.py)
python -m codegen generate servicefusion
```

See `python -m codegen --help` for full documentation.
