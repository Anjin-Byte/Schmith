# Schmith v2 — Implementation Document

## Overview

This document maps the v2 implementation against the legacy codebase. For each
component it specifies: whether logic is ported as-is, ported with changes, or
written from scratch — and what the changes are and why.

---

## Proposed Module Structure

```
v2/
  schmith/
    adapters/
      base.py              # ApiAdapter base class + NodeClassification  [NEW]
      spec/
        openapi.py         # OpenAPI → in-memory IR                      [PORTED, minor changes]
        raml.py            # RAML → in-memory IR                         [PORTED, minor changes]
      api/                 # API-specific adapter implementations
        __init__.py        # Adapter registry/loader                     [NEW]
    ir/
      models.py            # SchemaNode, Endpoint, OperationResponse      [NEW]
      store.py             # In-memory schema store                      [NEW, replaces IRLoader]
      composition.py       # Composition resolver                        [PORTED, as-is]
    generation/
      type_tree.py         # Type closure traversal                      [PORTED, modified]
      type_mapping.py      # IR → C# type mapping                        [PORTED, as-is]
      prompt.py            # Prompt packet builder                       [PORTED, simplified]
      llm.py               # LLM provider caller                        [PORTED, minor changes]
      prompts.json         # LLM instruction text                        [PORTED, as-is]
    shared/
      hashing.py           # Canonical JSON hashing                      [PORTED, as-is]
      provenance.py        # Provenance dataclass                        [PORTED, as-is]
      schema_ids.py        # Schema ID generation                        [PORTED, as-is]
    pipeline.py            # 6-stage orchestrator                        [NEW]
    cli.py                 # Entry point                                 [NEW]
  config.yaml              # Per-API setup config                        [NEW]
  pyproject.toml
```

---

## Components: Ported As-Is

These modules contain pure logic with no architectural assumptions that need
to change. They can be copied from legacy and used directly, with only import
path updates.

---

### `schmith/shared/hashing.py`

**Legacy source:** `legacy/builders/shared/hashing.py`

`canonical_json_hash` produces a stable SHA-1 hash from a schema object. Used
for anonymous schema ID generation and deduplication. No changes needed.

---

### `schmith/shared/provenance.py`

**Legacy source:** `legacy/builders/shared/provenance.py`

The `Provenance` dataclass records where in the source spec a piece of IR came
from. It is passed through every schema and field record for traceability. No
changes needed.

---

### `schmith/shared/schema_ids.py`

**Legacy source:** `legacy/builders/shared/schema_ids.py`

`schema_id_from_ref` and `schema_id_for_schema` produce stable, canonical
schema IDs from OpenAPI `$ref` strings and inline schema objects respectively.
These are the keys used throughout the schema store. No changes needed.

---

### `schmith/ir/composition.py`

**Legacy source:** `legacy/codegen/ir/composition.py`

`CompositionResolver` merges properties from `allOf`/`oneOf`/`anyOf` composition
members recursively, with caching and depth-guarded cycle detection. It depends
only on a `SchemaResolver` callable (`schema_id -> dict | None`), making it fully
decoupled from the storage layer. No changes needed.

---

### `schmith/generation/type_mapping.py`

**Legacy source:** `legacy/codegen/schema/type_mapping.py`

Pure functions for converting IR types to C# types:

- `IR_TO_CSHARP_TYPE` — primitive schema ID → C# type name mapping
- `schema_id_to_csharp_type` — resolves a schema ID to its C# type string
- `build_field_info` — builds a field metadata dict for code generation
- `json_name_to_csharp_property` — snake/kebab case → PascalCase
- `extract_clean_name` — extracts a clean class name from a schema ID or name hint
- `is_shapeless_schema` — detects free-form objects that should map to `JsonElement`
- `format_data_object_name` — appends `DataObject` suffix

All of these are stateless and depend only on the schema dict format, not on
any file I/O or global state. No changes needed.

---

### `schmith/generation/prompts.json`

**Legacy source:** `legacy/codegen/generation/prompts.json`

The LLM instruction text for C# DataObject generation. Contains the full system
prompt and code conventions. Portable as-is.

---

## Components: Ported With Changes

These modules are carried forward from legacy but require meaningful modifications
to fit the v2 architecture.

---

### `schmith/adapters/spec/openapi.py`

**Legacy source:** `legacy/builders/adapters/openapi/schemas.py` +
`legacy/builders/adapters/openapi/operations.py`

The legacy adapters were designed to write IR output to disk (via the build scripts
`build_schemas.py`, `build_operations.py`). In v2, there is no disk-based IR.
The adapters produce in-memory dicts that go directly into `SchemaStore`.

**Changes:**

1. **Output target.** The functions return dicts directly rather than writing
   JSON files. `extract_schemas` returns `dict[str, dict]` (schema_id → schema
   record) and `extract_operations` returns `list[dict]`. These are loaded
   directly into `SchemaStore`.

2. **Naming strategy removed.** The legacy adapter supported configurable naming
   strategies (verbose, semantic, resource) for operation and response schema
   names. In v2, naming of response schemas is not needed at the adapter level —
   the type tree handles naming. The `NamingStrategy` dependency and `naming_config`
   parameter are dropped.

3. **Scope.** The legacy `extract_schemas` extracted schemas from the entire
   spec — all `components/schemas` entries plus all inline schemas from every
   operation. In v2, we still extract the full component schema registry
   (needed for `$ref` resolution) but we only need to extract inline schemas
   from the target endpoint. The function signature gains an optional
   `target_path` / `target_method` filter parameter for this purpose.

4. **Module consolidation.** Legacy had separate files for operations vs schemas.
   In v2 these are combined in one spec adapter file per format.

The core logic — `register_schema`, `build_field`, `resolve_ref`,
`detect_nullable`, `extract_constraints`, `extract_composition`,
`_collapse_single_ref_schema` — is unchanged.

---

### `schmith/adapters/spec/raml.py`

**Legacy source:** `legacy/builders/adapters/raml/schemas.py` +
`legacy/builders/adapters/raml/operations.py`

Same changes as the OpenAPI adapter above: remove disk I/O, remove naming strategy,
add optional endpoint filter.

---

### `schmith/generation/type_tree.py`

**Legacy source:** `legacy/codegen/schema/type_tree.py`

The most significant porting change. Legacy `collect_type_closure` and
`build_type_hierarchy` contain hardcoded heuristics for naming and classification.
In v2, these decision points must be exposed to the `ApiAdapter` via hooks.

**Changes:**

1. **`name_anonymous` hook.** In `traverse_and_name`, the point where
   `build_name_from_context` is called is gated: if an `ApiAdapter` is present,
   `adapter.name_anonymous(node, context)` is called first. If it returns a
   non-`None` string, that name is used instead of the general heuristic. The
   `should_name_schema` / `reserve_type_name` flow remains otherwise unchanged.

2. **`classify_node` hook.** In `process_schema`, before deciding whether to
   collect a schema as a named class or skip it, `adapter.classify_node(node, context)`
   is called. If it returns `NodeClassification.INLINE` or
   `NodeClassification.COLLAPSE`, the schema is handled accordingly. If it
   returns `None`, the existing heuristics apply.

3. **`adapter` parameter.** Both `collect_type_closure` and `build_type_hierarchy`
   gain an optional `adapter: ApiAdapter | None = None` parameter. When `None`,
   all hooks are no-ops and behaviour is identical to legacy.

4. **`TreeContext` passed to hooks.** A `TreeContext` dataclass (see new
   components below) is constructed and passed to `classify_node`. It contains
   the schema's parent node, edge kind, and depth.

**Unchanged:** `SchemaEdge`, `NamingContext`, `extract_all_edges`,
`is_primitive_schema`, `get_primitive_type_name`, `resolve_type_name`,
`_build_type_entry`, `collect_composition_properties`.

---

### `schmith/generation/prompt.py`

**Legacy source:** `legacy/codegen/generation/prompt_packets.py`

Legacy prompt packet generation was designed around batch processing of many
schemas, with grouping (parent/child), pagination (max fields per page), and
filter application. In v2, a packet is built for exactly one root schema and
its type closure.

**Changes:**

1. **No batch processing.** No iteration over all IR schemas, no filter
   application, no grouping logic. The function takes a pre-resolved type
   tree (output of `build_type_hierarchy`) directly.

2. **Pagination retained.** Large schemas may still exceed LLM context limits.
   The max-fields-per-page pagination logic is retained.

3. **No coverage reports.** No manifest writing, no endpoint coverage reports.

4. **Simplified signature:**
   ```python
   def build_prompt_packet(
       root_type: dict,
       nested_types: list[dict],
       endpoint: Endpoint,
       max_fields_per_page: int = 6,
   ) -> dict
   ```

The field info building logic (`build_field_info`, enum handling, constraint
rendering) is unchanged.

---

### `schmith/generation/llm.py`

**Legacy source:** `legacy/codegen/providers/llm.py` +
`legacy/codegen/generation/code_generator.py`

**Changes:**

1. **No packet file I/O.** Legacy read packets from disk and wrote generated
   `.cs` files to disk. In v2, packets are passed in-memory and generated code
   is returned as a string.

2. **No manifest writing.** No `generated/<api>/manifest.json` output.

3. **Combined.** Legacy split provider (Anthropic/OpenAI adapter) and
   code_generator (packet reading, LLM calling, output writing) into two files.
   In v2 these are one module.

The provider abstraction (Anthropic vs OpenAI API call), system prompt loading,
and output sanitization (strip namespace declarations etc.) are unchanged.

---

## Components: New

These have no direct legacy equivalent and must be written from scratch.

---

### `schmith/adapters/base.py`

The `ApiAdapter` base class and associated types.

```python
from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from schmith.ir.models import SchemaNode, Endpoint
    from schmith.generation.type_tree import NamingContext, TreeContext


class NodeClassification(Enum):
    NAMED_CLASS = "named_class"   # Generate as its own record/class
    INLINE      = "inline"        # Fold properties into parent
    COLLAPSE    = "collapse"      # Transparent; follow through to children


class ApiAdapter:
    """
    Base adapter — all methods are pass-throughs.

    Subclass this and override only the hooks you need. The general pipeline
    calls these at each decision point. Returning None from any hook defers
    to the general heuristic.
    """

    def resolve_root(
        self,
        endpoint: "Endpoint",
        response_node: "SchemaNode",
    ) -> "SchemaNode":
        """
        Select the actual DataObject root from the endpoint's response schema.

        The candidate is the schema the spec directly associates with the
        response. Override to unwrap pagination envelopes, follow indirection,
        or select a specific branch of a union.
        """
        return response_node

    def transform_tree(self, root: "SchemaNode") -> "SchemaNode":
        """
        Transform the type tree before class generation.

        Override to collapse wrappers, rename nodes, merge schemas, or mark
        nodes for inlining. The full tree is reachable via the root node.
        """
        return root

    def name_anonymous(
        self,
        node: "SchemaNode",
        context: "NamingContext",
    ) -> str | None:
        """
        Provide a name for an anonymous schema node.

        Return a string to override the general naming heuristic.
        Return None to defer.
        """
        return None

    def classify_node(
        self,
        node: "SchemaNode",
        context: "TreeContext",
    ) -> NodeClassification | None:
        """
        Classify a node: named class, inline into parent, or collapse.

        Return a NodeClassification to override the general heuristic.
        Return None to defer.
        """
        return None
```

---

### `schmith/ir/models.py`

Lightweight dataclasses for the v2 IR layer. These are passed into adapter
hooks and through the pipeline.

```python
@dataclass
class Endpoint:
    method: str          # "GET", "POST", etc. (uppercase)
    path: str            # "/customers/{id}"


@dataclass
class OperationResponse:
    status_code: str     # "200", "201", etc.
    schema_id: str | None
    media_type: str | None
    description: str | None


@dataclass
class SchemaNode:
    """
    A navigable wrapper around a raw schema dict.

    This is what adapter hooks receive. It provides enough context to make
    navigation and classification decisions without requiring the adapter to
    parse raw dict internals.
    """
    schema_id: str
    schema: dict                     # Raw IR schema record
    parent: "SchemaNode | None"      # None for root
    edge_kind: str | None            # "property", "array_items", "composition_member", etc.
    depth: int                       # Distance from root (0 = root)

    def get(self, key: str, default=None):
        return self.schema.get(key, default)

    @property
    def kind(self) -> str:
        return self.schema.get("kind", "object")

    @property
    def name_hint(self) -> str | None:
        return self.schema.get("name_hint")

    @property
    def is_anonymous(self) -> bool:
        return "anon/" in self.schema_id

    @property
    def properties(self) -> list[dict]:
        return self.schema.get("properties", [])
```

---

### `schmith/ir/store.py`

In-memory schema store. Replaces the file-based `IRLoader`.

In legacy, IR was written to disk between stages and `IRLoader` read it back.
In v2, everything lives in memory within a single pipeline run.

```python
class SchemaStore:
    """
    In-memory registry of all schemas extracted from a spec.

    Populated by a spec adapter, consumed by type tree traversal and
    composition resolution.
    """

    def __init__(self, schemas: dict[str, dict]):
        self._schemas = schemas

    def get(self, schema_id: str) -> dict | None:
        return self._schemas.get(schema_id)

    def all(self) -> dict[str, dict]:
        return self._schemas

    def resolver(self):
        """Return a SchemaResolver callable for use with CompositionResolver."""
        return lambda schema_id: self._schemas.get(schema_id)
```

The store is passed as-is to `CompositionResolver` and `collect_type_closure`.
No file reading, no manifest parsing, no lazy loading from disk.

---

### `schmith/generation/type_tree.py` — `TreeContext`

New dataclass passed to `classify_node`.

```python
@dataclass
class TreeContext:
    parent: SchemaNode | None    # The parent node
    edge_kind: str | None        # How this node was reached from parent
    depth: int                   # Distance from root
    root_schema_id: str          # Schema ID of the tree root
```

---

### `schmith/pipeline.py`

The 6-stage orchestrator. This is the central new piece that wires everything
together.

```python
def run(
    spec_path: str,
    method: str,
    path: str,
    adapter: ApiAdapter | None = None,
    llm_config: dict | None = None,
) -> str:
    """
    Run the full pipeline: spec → C# DataObject source.

    Returns the generated C# code as a string.
    """
```

**Stage responsibilities:**

| Stage | Input | Output | Module called |
|-------|-------|--------|---------------|
| 1. Parse spec | spec file path | `SchemaStore`, raw operations list | `adapters/spec/openapi.py` or `raml.py` |
| 2. Resolve endpoint | method + path, operations list | `OperationResponse` (candidate schema_id) | new logic in `pipeline.py` |
| 3. Root resolution | candidate `SchemaNode`, `Endpoint` | resolved root `SchemaNode` | `adapter.resolve_root()` |
| 4. Build type tree | root `SchemaNode`, `SchemaStore`, adapter | `(root_type, nested_types)` | `generation/type_tree.py` |
| 5. Transform tree | root `SchemaNode` | transformed root `SchemaNode` | `adapter.transform_tree()` |
| 6. Generate code | `(root_type, nested_types)`, endpoint | C# source string | `generation/prompt.py` + `generation/llm.py` |

**Pipeline outputs three artifacts:**
- `ir.json` — the raw IR for the resolved type closure (after stage 4)
- `schema.md` — markdown documentation of the type tree (after stage 5)
- `<Name>DataObject.cs` — the generated C# source (after stage 6)

**Stage 2 — Endpoint resolution** is new logic with no legacy equivalent. It:
- Matches the provided `(method, path)` against extracted operations
- Selects the primary success response (prefers `200`, falls back to `201`, then
  the lowest 2xx)
- Returns an `OperationResponse` containing the `schema_id` for that response

**Stage 3 and 5** are single function calls to adapter hooks, each a one-liner
in the pipeline.

**Stage 4** calls `build_type_hierarchy` (ported from legacy `type_tree.py`) with
the `adapter` parameter threaded through.

---

### `schmith/adapters/api/__init__.py`

A simple registry that maps API names to adapter classes, and a loader that
can instantiate an adapter by name or from a module path.

```python
def load_adapter(adapter_ref: str | None) -> ApiAdapter:
    """
    Load an ApiAdapter by reference string or return the base adapter.

    adapter_ref examples:
        None                          → base ApiAdapter (all pass-throughs)
        "servicefusion"               → built-in named adapter
        "mypackage.adapters.MyApi"    → dotted module path
    """
```

---

### `config.yaml`

A single YAML file that configures the program for a specific API. Kept
intentionally minimal — it answers only the question *"where is the spec and
how should it be processed?"*

```yaml
api:
  name: servicefusion            # Human-readable name, used for output directory naming
  spec: spec/servicefusion.json  # Path to the spec file (relative to config location)
  format: openapi                # "openapi" or "raml"
  adapter: servicefusion         # Adapter name or dotted module path (optional)

llm:
  provider: anthropic            # "anthropic" or "openai"
  model: claude-sonnet-4-6
```

Nothing endpoint-specific lives in the config. Endpoint selection is the CLI's
responsibility.

---

### `schmith/cli.py`

Entry point. Loads `config.yaml` and accepts an endpoint specification. No
other arguments are needed for the common case.

```
Usage: schmith <method> <path> [--config <path>] [--status <code>] [--dry-run]

Arguments:
  method     HTTP method (GET, POST, etc.)
  path       Endpoint path (e.g. /customers/{id})

Options:
  --config   Path to config.yaml (default: ./config.yaml)
  --status   Target response status code (default: 200, fallback to lowest 2xx)
  --dry-run  Print the prompt packet and resolved schema without calling the LLM
```

**Output** — for a given endpoint the CLI writes three artifacts to
`output/<endpoint-slug>/`:

| File | Contents |
|------|----------|
| `ir.json` | The raw IR schema record for the resolved root and its type closure |
| `schema.md` | Markdown documentation of the resolved type tree |
| `<Name>DataObject.cs` | The generated C# DataObject source |

The output directory is derived from the endpoint: `GET /customers/{id}` →
`output/GET_customers_{id}/`.

---

## What Is Not Ported

The following legacy components are explicitly not carried into v2. They belong
to the exhaustive-generation model that v2 moves away from.

| Legacy module | Reason not ported |
|---------------|-------------------|
| `builders/build_schemas.py` | Batch pipeline script; v2 is on-demand |
| `builders/build_operations.py` | Same |
| `builders/build_serialization.py` | Serialization IR is not needed; field JSON names come from the schema record directly |
| `builders/build_refs.py` | Reference graph was used for batch coverage analysis; not needed for single-endpoint mode |
| `lib/ir_loader.py` | Replaced by in-memory `SchemaStore` |
| `codegen/schema/filter.py` | Filter logic for batch schema selection; not applicable |
| `codegen/schema/naming.py` | Naming strategy system (verbose/semantic/resource); in v2 this concern moves into `type_tree.py` + `ApiAdapter.name_anonymous` |
| `codegen/cli.py` | Legacy CLI was batch-oriented; replaced by new `cli.py` |
| `codegen/filters.toml` | Config-driven schema inclusion/exclusion; replaced by adapter code |
| `tests/invariants/` | Invariants validated the disk-based IR; the philosophy is preserved in v2 — see Testing section below |
| `codegen/generation/manifest.py` | Output manifest for batch traversal; not needed |
| `codegen/generation/endpoints_report.py` | Coverage report; not needed |
| `pipeline/config.py` | Config loading for batch pipeline |

---

## Testing

The legacy invariant test suite validated structural consistency of the disk-based
IR between pipeline stages. The specific tests are not portable because the
disk-based IR no longer exists. The *philosophy* is directly portable: assert
that each pipeline stage produces internally consistent output before the next
stage consumes it.

In v2 this takes two forms: **pipeline invariants** and **unit tests**.

---

### Pipeline Invariants

Lightweight structural assertions run at the end of each pipeline stage, active
in development and available via `--debug` at the CLI. Each invariant checks
the output of its stage before handing off to the next.

These are new — there is no direct legacy equivalent — but the approach is
descended from legacy's invariant framework.

| Invariant | Stage | What is checked |
|-----------|-------|-----------------|
| 1. Schema store completeness | After stage 1 | Every `schema_id` referenced in an operation response exists as a key in the `SchemaStore`. No dangling references. |
| 2. Endpoint resolution validity | After stage 2 | The `schema_id` returned by endpoint resolution exists in the `SchemaStore`. The resolved `OperationResponse` is not empty. |
| 3. Root node resolvability | After stage 3 | The `SchemaNode` returned by `adapter.resolve_root()` has a `schema_id` that exists in the `SchemaStore`. |
| 4. Type closure completeness | After stage 4 | Every `schema_id` referenced by any property in the collected type closure resolves to an entry in the `SchemaStore` or to a known primitive. No type in the closure references an unknown type. |
| 5. Type name uniqueness | After stage 4 | All type names in the closure are unique. No two distinct schemas produce the same C# class name. |
| 6. Transformed root validity | After stage 5 | The root returned by `adapter.transform_tree()` is still resolvable in the `SchemaStore`. |

These invariants are implemented as standalone functions in
`schmith/pipeline_invariants.py` — new module, no legacy equivalent — and
called by `pipeline.py` between stages when debug mode is active.

---

### Unit Tests

Located in `tests/`. Each test module covers one internal component in
isolation. No LLM calls are made in unit tests.

| Test module | Component under test | What is tested |
|-------------|----------------------|----------------|
| `tests/test_openapi_adapter.py` | `adapters/spec/openapi.py` | Schema extraction, operation extraction, `$ref` resolution, composition extraction, anonymous schema deduplication |
| `tests/test_raml_adapter.py` | `adapters/spec/raml.py` | Same as above for RAML format |
| `tests/test_schema_store.py` | `ir/store.py` | Store construction, lookup, resolver callable |
| `tests/test_composition.py` | `ir/composition.py` | `allOf`/`oneOf`/`anyOf` property merging, cycle detection, caching |
| `tests/test_type_tree.py` | `generation/type_tree.py` | Type closure collection, anonymous naming, cycle detection, adapter hook dispatch — default (no adapter) and with mock adapter overrides |
| `tests/test_type_mapping.py` | `generation/type_mapping.py` | IR → C# type conversion, field info building, shapeless detection, PascalCase conversion |
| `tests/test_endpoint_resolution.py` | `pipeline.py` (stage 2) | Matching by method + path, 2xx preference logic, no-match error handling |
| `tests/test_adapter_base.py` | `adapters/base.py` | Default pass-through behaviour of all hooks |
| `tests/test_pipeline_invariants.py` | `pipeline_invariants.py` | Each invariant detects the violation it is designed to catch, using minimal synthetic IR fixtures |

The legacy `tests/invariants/framework.py` established a clean pattern for
fixture-driven invariant testing. That pattern — construct a minimal IR fixture,
run the check, assert pass/fail — is worth replicating in
`tests/test_pipeline_invariants.py`.

---

## Dependency Summary

```
cli.py
  └─ pipeline.py
       ├─ adapters/spec/openapi.py    (or raml.py)
       │    └─ shared/schema_ids.py
       │    └─ shared/hashing.py
       │    └─ shared/provenance.py
       ├─ ir/store.py
       ├─ ir/models.py
       ├─ adapters/base.py
       ├─ adapters/api/__init__.py
       ├─ generation/type_tree.py
       │    ├─ ir/composition.py
       │    └─ generation/type_mapping.py
       ├─ generation/prompt.py
       │    └─ generation/type_mapping.py
       └─ generation/llm.py
            └─ generation/prompts.json
```

No module outside `adapters/api/` imports from a specific API adapter.
`pipeline.py` receives an `ApiAdapter` instance and calls its hooks — it never
imports concrete adapter subclasses directly.
