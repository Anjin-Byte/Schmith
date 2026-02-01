# Schmith

API spec analysis and C# code generation pipeline for Trimble XChange DataObjects.

Schmith ingests OpenAPI/RAML specs, builds a normalized Intermediate Representation (IR), validates it with invariant tests, and generates C# DataObjects using LLM prompt packets.

## Quick Start

```bash
# Install dependencies
uv sync

# Build IR (example: OpenAPI)
uv run python builders/build_operations.py --config configs/paycore.toml --adapter openapi
uv run python builders/build_schemas.py --config configs/paycore.toml --adapter openapi
uv run python builders/build_serialization.py --config configs/paycore.toml --adapter openapi
uv run python builders/build_refs.py --config configs/paycore.toml

# Run invariant tests
uv run python tests/invariants/run_all.py --config configs/paycore.toml -v

# Generate prompt packets + C# code
uv run python -m codegen packets paycore
uv run python -m codegen generate paycore
```

Tip: `run.sh` captures a full end-to-end sequence for a single API.

## Pipeline Overview

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  API Spec   │───▶│  IR Build   │───▶│  Invariant  │───▶│   Codegen   │
│ (RAML/OAS)  │    │ (4 Domains) │    │    Tests    │    │  (LLM/C#)   │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
     spec/              ir/             analysis/      prompt_packets/
                                                         generated/
```

### Stage 1: Spec Ingestion
- Supports OpenAPI 3.x (YAML/JSON) and RAML 1.0
- Specs stored in `spec/<api-name>/` or referenced by URL

### Stage 2: IR Building
Builds a normalized Intermediate Representation across four domains:

| Domain | Builder | Output |
|--------|---------|--------|
| Operations | `build_operations.py` | Endpoints, parameters, request/response bodies |
| Schemas | `build_schemas.py` | Type definitions, fields, constraints + field metadata |
| Serialization | `build_serialization.py` | Media types, JSON field names |
| References | `build_refs.py` | Schema relationships and dependencies |

Output: `ir/<api-name>/`

### Stage 3: Invariant Testing
Validates IR consistency:
- **Invariant 1**: Operation-Schema Usage (all referenced schemas exist)
- **Invariant 2**: Field Name Serialization (JSON paths match schema fields)
- **Invariant 3**: Media Type Mapping (content types properly mapped)
- **Invariant 4**: Reference Edge Consistency (schema refs match edge graph)
- **Invariant 5**: Provenance Coverage (traceability back to spec)

Output: `analysis/<api-name>/invariants/`

### Stage 4: Code Generation
Generate C# DataObjects using LLMs:

```bash
# List available DataObjects
uv run python -m codegen list servicefusion

# Generate prompt packets
uv run python -m codegen packets servicefusion

# Generate C# code
uv run python -m codegen generate servicefusion
```

Output: `prompt_packets/grouped/<api>/`, `generated/<api>/`
Generated output layout:
- `generated/<api>/_source/` C# source files (symlinked into object folders)
- `generated/<api>/_schemas/` schema markdown (symlinked into object folders)
- `generated/<api>/_reports/` coverage and other reports
- `generated/<api>/manifest.json` manifest for traversal and lookup

Notes:
- Prompt packets use type-tree resolution to include all reachable types and track composition-only members.
- Inline enums are given stable, field-based names to avoid anonymous enum types.

## Project Structure

```
schmith/
├── builders/             # IR build pipeline (OpenAPI/RAML adapters)
│   ├── adapters/         # Spec format adapters
│   ├── shared/           # Builder utilities
│   ├── build_operations.py
│   ├── build_schemas.py
│   ├── build_serialization.py
│   └── build_refs.py
│
├── codegen/              # LLM code generation tools
│   ├── cli.py            # Unified CLI
│   ├── config.toml       # Codegen settings
│   ├── filters.toml      # Schema filtering rules
│   ├── generation/       # Prompt packet + code generation
│   ├── ir/               # IR loading + composition helpers
│   ├── providers/        # LLM provider adapters
│   └── schema/           # Schema filters + type mapping
│
├── tests/invariants/     # Invariant test suite (5 tests)
│   ├── framework.py
│   ├── test_invariant_1.py
│   ├── test_invariant_2.py
│   ├── test_invariant_3.py
│   ├── test_invariant_4.py
│   ├── test_invariant_5.py
│   └── run_all.py
│
├── configs/              # Per-API configs for builders/tests
│   ├── paycore.toml
│   ├── servicefusion.toml
│   └── ukg_v2_client.toml
│
├── docs/                 # Domain docs and SDK notes
├── pipeline/             # Shared pipeline config helpers
├── prompt_packets/       # Generated LLM prompt packets
├── generated/            # Generated C# output + reports + manifest
├── ir/                   # Normalized IR per API
├── spec/                 # Input specs
└── reports/              # Pipeline reports
```

## Configuration

### API Configuration (`configs/*.toml`)

```toml
[api]
name = "servicefusion"

[spec]
url = "https://docs.servicefusion.com/api.json"

[output]
spec_dir = "spec"
reports_dir = "reports"
```

### Pipeline Default (`config.toml`)

Used by pipeline utilities and invariants when `--config` is not provided.

### Codegen Configuration (`codegen/config.toml`)

```toml
[paths]
ir_dir = "ir"
packets_dir = "prompt_packets"  # packets_dir/grouped/<ir>/
generated_dir = "generated"

[llm]
provider = "openai"    # or "anthropic"
model = ""             # empty = provider default
max_tokens = 4096

[prompting]
max_fields_per_page = 10
```

### Schema Filters (`codegen/filters.toml`)

Centralized inclusion/exclusion rules for DataObject generation. Use this to:
- include/exclude errors, anonymous schemas, variants, primitives
- apply regex filters
- add explicit include/exclude lists

### Prompt Text (`codegen/generation/prompts.json`)

Override or extend the LLM instruction and example code used when generating C#.

### Environment Variables (`.env`)

```bash
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
```

## Codegen CLI

```bash
# Show configuration and filters
uv run python -m codegen config

# List available IRs or DataObjects
uv run python -m codegen list
uv run python -m codegen list servicefusion -v
uv run python -m codegen list servicefusion --json

# Show parent-child schema groups
uv run python -m codegen groups servicefusion

# Show schema coverage report (roots vs nested, writes generated/<ir>/_reports/coverage.md)
uv run python -m codegen coverage servicefusion

# Endpoint response coverage report (writes generated/<ir>/_reports/endpoints.md)
uv run python -m codegen endpoints servicefusion

# Show prompt pagination view
uv run python -m codegen pages servicefusion --show-fields

# Generate prompt packets
uv run python -m codegen packets servicefusion
uv run python -m codegen packets servicefusion --schema Customer
uv run python -m codegen packets servicefusion --dry-run

# Generate C# code
uv run python -m codegen generate servicefusion
uv run python -m codegen generate servicefusion --schema Job
uv run python -m codegen generate servicefusion --limit 5
uv run python -m codegen generate servicefusion --dry-run --show-prompt
uv run python -m codegen generate servicefusion --no-clean

Notes:
- `--dry-run` skips LLM calls and `.cs` output, but still writes scaffolding and `manifest.json`.
- Output directories are cleaned by default; use `--no-clean` to keep existing files.
```

## Building IR Manually

```bash
# Build single API
uv run python builders/build_operations.py --config configs/servicefusion.toml --adapter raml
uv run python builders/build_schemas.py --config configs/servicefusion.toml --adapter raml
uv run python builders/build_serialization.py --config configs/servicefusion.toml --adapter raml
uv run python builders/build_refs.py --config configs/servicefusion.toml

# Run invariant tests
uv run python tests/invariants/run_all.py --config configs/servicefusion.toml -v
```

## Requirements

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

## License

Internal use only.
