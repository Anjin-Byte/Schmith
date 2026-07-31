# Schmith

**Endpoint-focused C# DataObject generator for API specifications.**

Schmith reads an OpenAPI or RAML spec, locates a specific endpoint, resolves its full type closure, and uses an LLM to generate a ready-to-use C# DataObject class — with all nested types, enums, `[JsonPropertyName]`, `[Description]`, `[Required]`, and `[Nullable]` attributes filled in. Each type gets its own dedicated LLM call; large types are automatically split across pages and stitched back together.

---

## How it works

Generation runs as a six-stage pipeline:

1. **Spec load** — Parse the API spec (OpenAPI JSON/YAML or RAML) into a schema store.
2. **Endpoint match** — Find the operation and 2xx response for the given `METHOD /path`.
3. **Root resolve** — Identify the root DataObject type, unwrapping pagination envelopes as needed.
4. **Type tree** — Recursively resolve the full closure of nested object and enum types.
5. **Transform** — Apply API-specific normalization via the adapter hook.
6. **Code generation** — Build structured prompt packets and submit one LLM call per type (per page). Assemble outputs into a single `.cs` file.

The pipeline is adapter-driven: API-specific wrapping logic (envelope unwrapping, naming conventions, type overrides) lives in a pluggable `ApiAdapter` subclass rather than in the core.

---

## Installation

Requires Python 3.11+. The project uses [uv](https://docs.astral.sh/uv/) for environment management.

```bash
git clone https://github.com/Anjin-Byte/Schmith.git
cd Schmith

# Install with uv (creates .venv automatically)
uv sync

# Install with a specific LLM provider
uv sync --extra anthropic     # Anthropic Claude
uv sync --extra openai        # OpenAI GPT
uv sync --extra all           # Both providers
```

Or with pip:

```bash
pip install -e ".[anthropic]"
pip install -e ".[openai]"
pip install -e ".[all]"
```

---

## Configuration

Copy and edit `config.yaml` in the directory where you run `schmith`:

```yaml
api:
  spec: path/to/api_spec.json   # OpenAPI JSON/YAML or RAML file
  format: openapi               # openapi | openapi3 | swagger | oas | raml
  adapter: null                 # optional: dotted path to ApiAdapter subclass

llm:
  provider: anthropic           # anthropic | openai
  # model: claude-opus-4-6     # optional model override
  # api_key: sk-ant-...        # or set ANTHROPIC_API_KEY / OPENAI_API_KEY
  # target_input_tokens: 3500  # token budget per LLM call (prompt pages sized to fit)
  # min_page_size: 5            # minimum fields per page regardless of token budget

output:
  dir: output                   # directory for generated artifacts

codegen:
  fields_per_page: null         # optional hard override for fields per page
  enum_values_per_page: 30      # enum values per LLM call
  max_retries: 2                # retry attempts per type when validation finds errors
```

API keys can also be set as environment variables:

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export OPENAI_API_KEY=sk-...
```

For a complete reference covering every config key, all CLI flags, exit codes, artifact structure, and common patterns, see [docs/CLI.md](docs/CLI.md).

---

## Usage

### Generate a DataObject

```bash
# Generate C# for a specific endpoint
schmith GET /customers
schmith GET /customers/{id}
schmith POST /jobs --status 201

# Preview what would be generated without calling the LLM
schmith GET /customers --dry-run

# Use a different config file
schmith GET /customers --config path/to/config.yaml

# Enable pipeline invariant checks for debugging
schmith GET /customers --debug
```

Each run writes a directory under `output/`:

```
output/GET_customers/
  CustomerDataObject.cs   ← generated C# code
  ir.json                 ← IR snapshot, validation summary
  schema.md               ← human-readable schema for review
  prompts.json            ← exact system+user prompt sent per LLM call
  pages.json              ← raw LLM outputs per page (source of truth for .cs)
```

### Validate previously generated output

```bash
# Validate a single output directory
schmith validate output/GET_customers/

# Validate multiple directories (shell glob supported)
schmith validate output/GET_*/

# Exit with status 1 if any errors are found (useful in CI)
schmith validate output/ --fail-on-errors
```

Validation checks run deterministically against the `.cs` file and the IR — no LLM required. Checks include: brace balance, missing/phantom/duplicate JSON property names, undeclared property types, and template artifact detection. See [docs/CLI.md](docs/CLI.md) for the full check list with codes and severity levels.

---

## Output artifacts

| File | Description |
|---|---|
| `<Name>DataObject.cs` | Generated C# class. Derived artifact — reconstructed from `pages.json`. |
| `ir.json` | Intermediate representation: endpoint metadata, root type, nested types, validation summary. |
| `schema.md` | Markdown summary of the full type closure for human review. |
| `prompts.json` | The exact system and user prompt text sent to the LLM for each page of each type. Stable across models — re-submittable to any provider. |
| `pages.json` | Raw LLM output per page. Authoritative source for the `.cs` file. `ir_hash` field enables staleness detection after spec changes. |

### pages.json structure

```json
{
  "version": 1,
  "endpoint": {"method": "GET", "path": "/customers"},
  "ir_hash": "sha1:a3f9...",
  "pages": [
    {
      "index": 0,
      "type_name": "Customer",
      "is_root": true,
      "page": 1,
      "total_pages": 2,
      "model": "claude-haiku-4-5-20251001",
      "generated_at": "2026-02-25T10:30:05Z",
      "output": "public class CustomerDataObject\n{\n    ..."
    }
  ]
}
```

---

## Adapter system

The adapter hook allows API-specific behaviour without modifying core pipeline logic.

```python
from schmith.adapters.base import ApiAdapter
from schmith.ir.models import Endpoint, SchemaNode

class MyApiAdapter(ApiAdapter):
    def resolve_root(self, endpoint: Endpoint, node: SchemaNode) -> SchemaNode:
        # Unwrap a custom envelope structure
        ...

    def transform_tree(self, root_type, nested_types):
        # Rename, drop, or promote types as needed
        ...
```

Reference the adapter in `config.yaml`:

```yaml
api:
  adapter: mypackage.adapters.MyApiAdapter
```

Built-in adapters for Procore, Paycore, ServiceFusion, and UKG are included in the `builders/` directory of the parent repository.

---

## Development

```bash
# Run all tests
uv run pytest tests/ -q

# Run with coverage
uv run pytest tests/ -q --cov=schmith --cov-report=term-missing

# Run a specific test file
uv run pytest tests/test_assembly.py -v
```

### Project structure

```
schmith/
  assembly.py          ← stitch page outputs; assemble final .cs from PageEntry list
  pipeline.py          ← six-stage orchestration
  pipeline_invariants.py ← optional structural checks between stages
  validation.py        ← deterministic post-generation checks
  cli.py               ← CLI entry point (generate + validate subcommands)
  generation/
    llm.py             ← LLMProvider protocol, Anthropic/OpenAI/DryRun implementations
    pages.py           ← PageEntry frozen dataclass; utcnow(); page_entry_to_dict()
    prompt.py          ← prompt packet construction; page prompt builder
    type_mapping.py    ← C# type inference from schema field descriptors
    type_tree.py       ← recursive type closure resolution
  adapters/
    base.py            ← ApiAdapter base class with pass-through hooks
    spec/
      openapi.py       ← OpenAPI schema/operation extraction
      raml.py          ← RAML schema/operation extraction
  ir/
    models.py          ← Endpoint, SchemaNode, OperationResponse dataclasses
    store.py           ← SchemaStore (schema_id → schema dict lookup)
    composition.py     ← allOf / anyOf / oneOf resolution
  shared/
    hashing.py         ← canonical_json_hash for IR fingerprinting
    provenance.py      ← source tracing helpers
    schema_ids.py      ← schema ID normalization
tests/
  test_assembly.py
  test_pagination.py
  test_validation.py
  test_pipeline_invariants.py
  ... (16 test files, ~371 tests)
docs/
  DESIGN.md                           ← problem statement and design rationale
  IMPLEMENTATION.md                   ← phase-by-phase implementation log
  GENERATION_STABILITY.md             ← LLM output stability improvement specs
  PARTIAL_REGENERATION.md             ← partial regeneration system design
  TYPED_PYTHON_ARCHITECTURE_GUIDELINES.md ← coding standards
```

---

## Key design decisions

**The `.cs` is a derived artifact.** `pages.json` is the source of truth. The final `.cs` is always reconstructed from raw per-page LLM outputs via `assemble_from_pages`. This means a single type can be regenerated by updating its entries in `pages.json` and reassembling — no regex parsing of the `.cs` required.

**Prompts are stable across models.** A prompt is computed from the IR once, stored in `prompts.json`, and can be resubmitted to any model. Switching providers does not require recomputing page boundaries.

**Each type is its own LLM call.** Root object, nested objects, and enums are never merged into a single prompt. This bounds the context per call and makes partial regeneration trivially scoped to one type.

**Adapters encode API conventions.** Envelope unwrapping, nested field promotion, and naming overrides are per-API logic that belongs in an adapter, not in the pipeline. The core pipeline stays spec-format-neutral.
