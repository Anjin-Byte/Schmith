# SpecBridge

[![Tests](https://github.com/Anjin-Byte/SpecBridge/actions/workflows/tests.yml/badge.svg)](https://github.com/Anjin-Byte/SpecBridge/actions/workflows/tests.yml)

**Turns one endpoint of a third-party API spec into a typed, PII-classified data contract.**

Onboarding a partner's API means reading their specification, working out which part of each response is the object you actually care about, mapping it onto your own types, and deciding which fields carry sensitive data. SpecBridge does that one endpoint at a time: it parses an OpenAPI or RAML spec, resolves the endpoint's full schema closure, classifies every field for PII, and generates a ready-to-use C# DataObject — nested types, enums, and `[JsonPropertyName]` / `[Description]` / `[Required]` / `[Nullable]` / `[WriteOnly]` attributes filled in.

Each type gets its own dedicated LLM call; large types are automatically split across pages and stitched back together.

```bash
specbridge GET /customers/{id}
```

```
Resolving GET /customers/{id}
  3 types  ·  4 LLM calls
  ✓ CustomerDataObject.cs written to output/GET_customers_{id}/
```

```csharp
public class CustomerDataObject
{
    [JsonPropertyName("id")]
    [Description("Unique customer identifier")]
    [Required]
    public int Id { get; set; }

    [JsonPropertyName("email")]
    [Description("Primary contact email")]
    [WriteOnly]                      // ← flagged by the PII pre-pass
    public string Email { get; set; }

    [JsonPropertyName("status")]
    public CustomerStatus? Status { get; set; }
}
```

*(Illustrative — attribute set and shape are what the tool emits; field names depend on your spec.)*

---

## The problem it solves

API spec formats describe *structure*, not *intent*. A spec can say a response has a `data` array under a `page`/`total` envelope — but nothing in the spec says the envelope is infrastructure and the array item is the object you actually want. That judgment is API-author convention, and it differs per provider.

The same questions come back with every new data source: which field is the real record, which wrapper is transport, which of two near-identical schema variants is authoritative, which columns are sensitive. The answers are specific to one provider and don't transfer to the next — so the integration cost is per-provider and recurring, and it lands on whoever understands both the provider's data and what the consuming system needs.

SpecBridge isolates that per-provider knowledge in pluggable adapters rather than hardcoding it in the pipeline. The core stays spec-format-neutral; provider quirks stay in one file, under test, where they can be read and corrected by someone who knows the API. [docs/DESIGN.md](docs/DESIGN.md) works through this in depth.

---

## Scope

SpecBridge and the v1 pipeline it replaced have been run against five provider APIs across two specification formats:

| Provider | Format | Schemas | Operations |
|---|---|---:|---:|
| Procore | OpenAPI 3 | 14,119 | 2,319 |
| UKG (v2 client) | OpenAPI 3 | 2,707 | 334 |
| Paycore | OpenAPI 3 | 2,265 | 53 |
| ServiceFusion | OpenAPI 3 | 138 | 27 |
| PeopleDoc (UKG) | RAML 1.0 | 95 | — |

The Procore specification alone is a 39 MB combined OAS document. Working at that size is what drove the endpoint-scoped design: resolving one endpoint's schema closure on demand is tractable, while generating exhaustively across a whole provider is not — and produces mostly output nobody asked for.

Provider data is rarely clean. The Procore adapter exists because that spec splits object schemas into `Normal`/`Extended` `allOf` segments and wraps list responses in single-key `data` envelopes — two conventions that produce silently wrong types if taken literally.

---

## How it works

Generation runs as a staged pipeline:

1. **Spec load** — Parse the API spec (OpenAPI JSON/YAML or RAML) into a schema store.
2. **Endpoint match** — Find the operation and 2xx response for the given `METHOD /path`.
3. **Root resolve** — Identify the root DataObject type, unwrapping pagination envelopes as needed.
4. **Type tree** — Recursively resolve the full closure of nested object and enum types.
5. **Transform** — Apply API-specific normalization via the adapter hook.
6. **PII classification** — Classify every field for sensitive data so PII fields are marked `[WriteOnly]` and borderline cases are flagged for human review.
7. **Code generation** — Build structured prompt packets and submit one LLM call per type (per page). Validate each block and retry with the specific errors attached; assemble outputs into a single `.cs` file.

The pipeline is adapter-driven: API-specific wrapping logic (envelope unwrapping, naming conventions, type overrides) lives in a pluggable `ApiAdapter` subclass rather than in the core.

---

## Installation

Requires Python 3.11+. The project uses [uv](https://docs.astral.sh/uv/) for environment management.

```bash
git clone https://github.com/Anjin-Byte/SpecBridge.git
cd SpecBridge

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

Copy and edit `config.yaml` in the directory where you run `specbridge`:

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

pii:
  enabled: true                 # classify fields for PII before generating
  # batch_size: 20              # fields per classification call

validation:
  enabled: true                 # deterministic checks after each generation
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
specbridge GET /customers
specbridge GET /customers/{id}
specbridge POST /jobs --status 201

# Preview what would be generated without calling the LLM
specbridge GET /customers --dry-run

# Use a different config file
specbridge GET /customers --config path/to/config.yaml

# Enable pipeline invariant checks for debugging
specbridge GET /customers --debug
```

Each run writes a directory under `output/`:

```
output/GET_customers/
  CustomerDataObject.cs   ← generated C# code
  ir.json                 ← IR snapshot, validation summary
  schema.md               ← human-readable schema for review
  codegen/
    prompts.json          ← exact system+user prompt sent per LLM call
    pages.json            ← raw LLM outputs per page (source of truth for .cs)
  pii/                    ← only when the PII pre-pass runs
    prompts.json          ← classification prompt per field batch
    pages.json            ← raw classification outputs
```

### Validate previously generated output

```bash
# Validate a single output directory
specbridge validate output/GET_customers/

# Validate multiple directories (shell glob supported)
specbridge validate output/GET_*/

# Exit with status 1 if any errors are found (useful in CI)
specbridge validate output/ --fail-on-errors
```

Validation checks run deterministically against the `.cs` file and the IR — no LLM required. Checks include: brace balance, missing/phantom/duplicate JSON property names, undeclared property types, and template artifact detection. See [docs/CLI.md](docs/CLI.md) for the full check list with codes and severity levels.

---

## Sensitive data

Before any code is generated, every field in the closure is classified against a fixed set of sensitive-data criteria — government identifiers, payment details, compensation, health data, credentials, contact information, and confidential business data. Fields that classify as sensitive are emitted with `[WriteOnly]`.

Three properties matter more than the classification itself:

- **Borderline fields are escalated, not decided.** A field that is sensitive in one context and not in another is flagged `// [REVIEW: ...]` with the reasoning attached, so a human rules on it rather than the tool guessing quietly.
- **Failure never means "safe."** If a classification response can't be parsed, or a field is missing from it, that field is recorded as unclassified and excluded from generation. There is no path where a failed check silently produces an unmarked field.
- **Every decision is auditable.** Each classification carries a one-sentence justification, and the full prompt and raw response for every batch are written to `pii/`. A reviewer can reconstruct why any given field was marked the way it was.

Classification runs on the resolved closure, so inherited and deeply nested fields are covered, not just the top-level record.

---

## Lineage and reproducibility

Generated output is traceable back to the specification that produced it.

Every registered schema and operation carries a `Provenance` record naming the source file and the exact JSON pointer it came from — down to the individual response content type. When a generated type looks wrong, "where did this come from?" has a recorded answer rather than requiring a re-read of a 39 MB spec. Both the OpenAPI and RAML adapters populate it, so the trail survives regardless of the provider's format.

Each run's outputs are fingerprinted with a canonical hash of the IR. Because the hash is canonical, it is stable across key ordering and formatting noise, and changes only when the underlying schema actually changes — so stale output is detectable after a provider revises their spec, instead of being found later by whatever breaks downstream.

Assembly is deterministic: the same page outputs always produce the same `.cs`. Reruns are diffable, and a single type can be regenerated and reassembled without touching the rest.

---

## Output artifacts

| File | Description |
|---|---|
| `<Name>DataObject.cs` | Generated C# class. Derived artifact — reconstructed from `pages.json`. |
| `ir.json` | Intermediate representation: endpoint metadata, root type, nested types, validation summary. |
| `schema.md` | Markdown summary of the full type closure for human review. |
| `codegen/prompts.json` | The exact system and user prompt text sent to the LLM for each page of each type. Stable across models — re-submittable to any provider. |
| `codegen/pages.json` | Raw LLM output per page. Authoritative source for the `.cs` file. `ir_hash` field enables staleness detection after spec changes. |

### codegen/pages.json structure

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
from specbridge.adapters.base import ApiAdapter
from specbridge.ir.models import Endpoint, SchemaNode

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

[`specbridge/adapters/procore.py`](specbridge/adapters/procore.py) is the reference implementation. It handles two real Procore quirks: `allOf` schemas split into `Normal`/`Extended` segments (which the LLM otherwise emits as a class literally named `Normal`), and `{ "data": [...] }` list envelopes that would otherwise produce a useless wrapper class.

---

## Development

```bash
# Run all tests
uv run pytest tests/ -q

# Run with coverage
uv run pytest tests/ -q --cov=specbridge --cov-report=term-missing

# Run a specific test file
uv run pytest tests/test_assembly.py -v
```

### Project structure

```
specbridge/
  assembly.py          ← stitch page outputs; assemble final .cs from PageEntry list
  pipeline.py          ← stage orchestration
  pipeline_invariants.py ← optional structural checks between stages
  validation.py        ← deterministic post-generation checks
  cli.py               ← CLI entry point (generate + validate subcommands)
  generation/
    llm.py             ← LLMProvider protocol, Anthropic/OpenAI/DryRun implementations
    pages.py           ← PageEntry frozen dataclass; utcnow(); page_entry_to_dict()
    prompt.py          ← prompt packet construction; page prompt builder
    type_mapping.py    ← C# type inference from schema field descriptors
    type_tree.py       ← recursive type closure resolution
  pii.py               ← PII/sensitive-data classification pre-pass
  adapters/
    base.py            ← ApiAdapter base class with pass-through hooks
    procore.py         ← reference adapter: allOf segments, data envelopes
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
tests/                 ← 18 files, 447 tests
docs/
  DESIGN.md                           ← problem statement and design rationale
  CLI.md                              ← full config, flag, and exit-code reference
  IMPLEMENTATION.md                   ← migration record (historical)
  GENERATION_STABILITY.md             ← LLM output stability improvement specs
  PARTIAL_REGENERATION.md             ← partial regeneration system design
  TYPED_PYTHON_ARCHITECTURE_GUIDELINES.md ← coding standards
```

Roughly 6,200 lines of source against 4,650 lines of tests.

### Project history

The first-generation pipeline built a file-based IR on disk and generated exhaustively across whole APIs. It is archived at the `v1-legacy` tag (`git checkout v1-legacy`); [docs/IMPLEMENTATION.md](docs/IMPLEMENTATION.md) records what carried over and what was rewritten, and why.

---

## Key design decisions

**The `.cs` is a derived artifact.** `pages.json` is the source of truth. The final `.cs` is always reconstructed from raw per-page LLM outputs via `assemble_from_pages`. This means a single type can be regenerated by updating its entries in `pages.json` and reassembling — no regex parsing of the `.cs` required.

**Prompts are stable across models.** A prompt is computed from the IR once, stored in `codegen/prompts.json`, and can be resubmitted to any model. Switching providers does not require recomputing page boundaries.

**Each type is its own LLM call.** Root object, nested objects, and enums are never merged into a single prompt. This bounds the context per call and makes partial regeneration trivially scoped to one type.

**Adapters encode API conventions.** Envelope unwrapping, nested field promotion, and naming overrides are per-API logic that belongs in an adapter, not in the pipeline. The core pipeline stays spec-format-neutral.

**Validation failures are fed back, not retried blind.** When a generated block fails a check, the specific errors are injected into the retry prompt as a correction block. Retrying with the error text attached fixes most single-field mistakes on the first attempt.

**Generation is scoped to one endpoint, on demand.** The predecessor generated exhaustively across an entire provider, which meant a spec revision invalidated everything at once and most output was never consumed. Scoping to a single endpoint keeps each run small enough to review, and makes the blast radius of a provider change proportionate to what actually changed.
