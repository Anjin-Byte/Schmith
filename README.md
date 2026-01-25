# Schmith

API spec analysis and C# code generation pipeline for Trimble XChange DataObjects.

Schmith processes OpenAPI and RAML specifications into a normalized Intermediate Representation (IR), validates consistency through invariant tests, and generates C# DataObject code using LLMs.

## Quick Start

```bash
# Install dependencies
uv sync

# Run the interactive demo
./demo.sh

# Or run specific stages
./demo.sh build      # Build IR for all specs
./demo.sh test       # Run invariant tests
./demo.sh codegen    # Demo code generation CLI
```

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
- Specs stored in `spec/<api-name>/`

### Stage 2: IR Building
Builds a normalized Intermediate Representation across four domains:

| Domain | Builder | Output |
|--------|---------|--------|
| Operations | `build_operations.py` | Endpoints, parameters, request/response bodies |
| Schemas | `build_schemas.py` | Type definitions, fields, constraints |
| Serialization | `build_serialization.py` | Media types, JSON field names |
| References | `build_refs.py` | Schema relationships and dependencies |

Output: `ir/<api-name>/`

### Stage 3: Invariant Testing
Validates IR consistency:
- **Invariant 1**: Operation-Schema Usage (all referenced schemas exist)
- **Invariant 2**: Field Name Serialization (JSON paths match schema fields)
- **Invariant 3**: Media Type Mapping (content types properly mapped)

Output: `analysis/<api-name>/invariants/`

### Stage 4: Code Generation
Generate C# DataObjects using LLMs:

```bash
# List available DataObjects
python -m codegen list servicefusion

# Generate prompt packets
python -m codegen packets servicefusion

# Generate C# code
python -m codegen generate servicefusion
```

Output: `prompt_packets/`, `generated/`

## Project Structure

```
schmith/
├── builders/           # IR building scripts
│   ├── adapters/       # Spec format adapters (OpenAPI, RAML)
│   ├── shared/         # Shared builder utilities
│   ├── build_operations.py
│   ├── build_schemas.py
│   ├── build_serialization.py
│   └── build_refs.py
│
├── codegen/            # Code generation package
│   ├── config.toml     # Generation settings
│   ├── cli.py          # Unified CLI
│   ├── ir_loader.py    # IR loading utilities
│   ├── prompt_packets.py
│   ├── llm_providers.py
│   └── code_generator.py
│
├── tests/invariants/   # Invariant test suite
│   ├── framework.py    # Test framework
│   ├── test_invariant_1.py
│   ├── test_invariant_2.py
│   ├── test_invariant_3.py
│   └── run_all.py
│
├── configs/            # Per-API configuration
│   ├── servicefusion.toml
│   └── ukg_v2_client.toml
│
├── lib/                # Shared utilities
├── pipeline/           # Pipeline utilities
├── ir_requirements/    # IR specification docs (symlink)
├── DataObjectExamples/ # Reference C# examples
└── archive/            # Archived/superseded code
```

## Configuration

### API Configuration (`configs/*.toml`)

```toml
[api]
name = "servicefusion"

[spec]
url = "https://docs.servicefusion.com/api.json"

[output]
ir_dir = "ir"
```

### Codegen Configuration (`codegen/config.toml`)

```toml
[paths]
ir_dir = "ir"
packets_dir = "prompt_packets"
generated_dir = "generated"

[llm]
provider = "openai"    # or "anthropic"
model = ""             # empty = provider default

[generation]
grouped = true         # group parent-child schemas

[prompting]
max_fields_per_page = 10

[filters]
exclude_patterns = [".*Body$", ".*View$"]
```

### Environment Variables (`.env`)

```bash
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
```

## Codegen CLI

```bash
# Show configuration
python -m codegen config

# List available IRs
python -m codegen list

# List DataObjects for an IR
python -m codegen list servicefusion
python -m codegen list servicefusion -v        # verbose
python -m codegen list servicefusion --json    # JSON output

# Show parent-child schema groups
python -m codegen groups servicefusion

# Show prompt pagination view
python -m codegen pages servicefusion
python -m codegen pages servicefusion --schema Customer
python -m codegen pages servicefusion --show-fields

# Generate prompt packets
python -m codegen packets servicefusion
python -m codegen packets servicefusion --grouped    # with nested types
python -m codegen packets servicefusion --dry-run   # preview only

# Generate C# code
python -m codegen generate servicefusion
python -m codegen generate servicefusion --limit 5       # limit count
python -m codegen generate servicefusion --schema Job    # specific schema
python -m codegen generate servicefusion --dry-run       # preview prompts
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

## Supported APIs

| API | Spec Format | Config |
|-----|-------------|--------|
| ServiceFusion | RAML 1.0 | `configs/servicefusion.toml` |
| UKG V2 Client | OpenAPI 3.x | `configs/ukg_v2_client.toml` |

## Requirements

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

## License

Internal use only.
