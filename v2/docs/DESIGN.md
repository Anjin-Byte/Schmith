# Schmith v2 — Design Document

## Table of Contents

1. [Motivating Issues](#motivating-issues)
2. [Philosophy](#philosophy)
3. [Previous Work — Schmith Legacy](#previous-work--schmith-legacy)
4. [Requirements — Schmith v2](#requirements--schmith-v2)

---

## Motivating Issues

### The Gap Between Spec and Intent

API specification formats — OpenAPI 3.x, RAML 1.0, and their relatives — are languages for
describing the *structure* of data and the *shape* of HTTP interactions. They are not languages
for describing *intent*. An author writing an API spec can express that a field is a string, that
it is required, that it appears in a JSON array under a key named `items`. What the author cannot
express in the language of the spec itself is *why* the data is structured the way it is, *what*
the consumer is expected to do with it, or *which* piece of a response is the conceptually central
object versus which is wrapper infrastructure.

This gap is fundamental, not accidental. Spec formats are intentionally general — they describe the
contract between producer and consumer at the wire level. The semantic layer above that contract is
left implicit, governed by platform conventions, API design traditions, and choices that differ from
one API author to the next.

### The Array Unwrapping Problem

A concrete and common instance of this gap is the paginated list response. Consider an endpoint
`GET /customers` that returns:

```json
{
  "data": [...],
  "page": 1,
  "per_page": 25,
  "total": 142
}
```

The spec faithfully describes this structure. It defines a response schema with `data`, `page`,
`per_page`, and `total` properties. The `data` property is an array, and the array items are
`CustomerView` objects.

From the perspective of generating a DataObject, the meaningful type is `CustomerView`. The outer
wrapper — the pagination envelope — is infrastructure. But nothing in the spec says this. Another
API might use a flat array response with no envelope at all. Another might nest the real data two
or three levels deep behind keys named `result`, `payload`, or `response`. Some APIs use a generic
`PagedResult<T>` wrapper. Others define a one-off wrapper per resource.

There is no general rule that can reliably identify the "real" data object across all of these
patterns. This is API author convention, and it must be encoded by a human who knows the API.

### The Type Topology Problem

Even once the root DataObject is identified, the question of how to slice a nested type tree into
classes is not answerable from spec syntax alone. A nested object within a schema might deserve its
own named class, or it might be better inlined into the parent. An anonymous inline object might
have a natural name that a human familiar with the API would use, or it might be a one-off
structure with no conventional name.

These decisions form what can be called the *class topology* — the map of which schemas become
which classes and how they relate. The spec provides the structural raw material. The topology is
an interpretation of that structure, and interpretations vary by API, by resource type, and
sometimes by endpoint.

### The "100% Coverage" Problem

A prior assumption in this problem space was that a useful goal is to generate DataObjects for
every schema in an API spec — full coverage. This turns out to be ill-defined for several reasons:

- **What counts as a schema?** Inline anonymous objects, composition members (`allOf`/`oneOf`),
  array item types, and error response schemas all appear as schemas in a spec. Not all of them
  warrant a DataObject class.
- **What counts as a DataObject?** Wrapper types, pagination envelopes, error envelopes, and
  partial update payloads are all schemas, but they serve different purposes.
- **Coverage of what?** Schemas are not the only unit. Endpoints, operations, and resource types
  are all plausible units of coverage, and they do not map cleanly to schemas.

There is no canonical definition of full coverage. Pursuing it produces output that is technically
complete but practically cluttered, because it includes infrastructure types, wrapper types, and
internal spec artifacts alongside the semantically meaningful DataObjects.

### Per-API Semantics Are Unavoidable

All of the above issues reduce to the same underlying truth: there is a layer of meaning above the
spec that is specific to each API and its platform conventions. This layer cannot be eliminated or
fully generalized. Any tool that ignores it will produce output that is structurally correct but
semantically wrong in ways that require manual correction.

The question is not whether per-API semantics must be handled. They must. The question is where
and how to handle them — in a way that keeps the general codebase general, and the API-specific
knowledge explicit, local, and auditable.

---

## Philosophy

### Endpoint Focus Over Spec Exhaustion

The right unit of work is a single endpoint, not a whole spec. The question being answered is:
*"What is the DataObject for the response of this endpoint?"* — not *"What are all the DataObjects
in this spec?"*

This shift eliminates the coverage problem entirely. There is no ambiguity about what to generate
when the target is a specific endpoint with a specific response. The output is intentional rather
than exhaustive.

### Structural Analysis Is General; Semantic Interpretation Is Specific

The work of parsing a spec, normalizing it into an intermediate representation, traversing type
trees, and resolving references is general. It does not depend on which API is being processed.
This work belongs in general, reusable code.

The work of deciding which node in a response tree is the real DataObject, what to name an
anonymous wrapper, or whether a composition member should be its own class — this is specific. It
depends on the API, sometimes on the resource type, sometimes on the individual endpoint. This work
belongs in adapter code that is isolated from the general logic.

### Adapters as the Seam Between General and Specific

The adapter pattern is the right tool for managing this boundary. An adapter is a well-defined
interface through which specific knowledge is injected into a general process. The general code
calls hooks on the adapter at decision points. The default adapter implements every hook as a
no-op or pass-through, so the general code works without any adapter. An API-specific adapter
subclass overrides only the hooks it needs to, in plain Python, with full access to the type tree
and endpoint context.

This gives API-specific logic maximum flexibility (imperative code, not config files) while keeping
it structurally isolated. The general codebase never imports or references any specific adapter.

### Explicit Over Inferred

Where a decision must be made that could go multiple ways, it is better to require explicit
instruction than to guess. Guessing produces output that is wrong in subtle ways. Explicit
instruction produces output that is correct by construction and auditable by inspection.

The adapter interface embodies this: the general code makes conservative, safe default decisions,
and the adapter provides explicit overrides for cases where the default is wrong.

---

## Previous Work — Schmith Legacy

The original Schmith program (`legacy/`) was built to generate an exhaustive set of DataObject
classes from an API spec. It represents substantial learned knowledge about the problem space and
contains several components of real value.

### What Legacy Got Right

**Spec format adapters for IR normalization.**
Legacy correctly identified that OpenAPI and RAML have different syntactic conventions for the
same semantic structures. It solved this with format-specific adapters in `builders/adapters/`
that normalize both formats into a common intermediate representation. This separation is sound
and the pattern carries forward.

**The intermediate representation (IR) design.**
The IR models operations, schemas, serialization metadata, and reference graphs as separate
concerns stored in structured JSON. It captures provenance (traceability to spec source),
handles hash-based deduplication of anonymous schemas, and models composition
(`allOf`/`oneOf`/`anyOf`) explicitly. This is careful, detailed work.

**Type tree traversal (`codegen/schema/type_tree.py`).**
The `collect_type_closure` and `build_type_hierarchy` functions implement a two-phase traversal
(naming then collection) that recursively resolves the full set of types reachable from a root
schema. It handles cycles, anonymous type naming via `NamingContext`, edge extraction across all
reference kinds (properties, array items, composition members, additional properties), and
deduplication. This is a strong foundation.

**Edge extraction isolation (`extract_all_edges`).**
All schema-kind-specific logic for following references is isolated in a single function. The
traversal itself is generic. This is a good architectural boundary.

**Invariant test framework.**
The suite of five invariant tests over the IR validates structural consistency before code
generation. This kind of integrity checking between pipeline stages is valuable practice.

**LLM-based code generation with prompt packets.**
The approach of building structured prompt packets from IR data and sending them to an LLM for
C# generation — with pagination for large schemas and a detailed system prompt for code
conventions — is effective. It decouples schema analysis from code synthesis cleanly.

### Where Legacy Fell Short

**Exhaustive coverage as the goal.**
The program tried to generate DataObjects for everything in a spec. This goal has no canonical
definition, produces cluttered output, and requires post-processing to identify what is actually
useful. The fundamental requirement was wrong.

**No mechanism for API-specific semantics.**
Legacy had spec-format adapters but no API-specific adapters. All semantic interpretation was done
by general code, which means it could only guess at author intent. For any given API, some
generated output would be structurally correct but semantically wrong — and there was no way to
correct this without modifying the general code.

**Root schema selection was implicit.**
The decision of which schema to use as the DataObject for a given endpoint was handled upstream
by the caller, with no hook for API-specific logic. The array unwrapping problem, for example,
had no systematic solution.

**Schema filtering via config was not expressive enough.**
`codegen/filters.toml` allowed coarse-grained inclusion/exclusion of schema categories. This is
insufficient for the topology decisions that real API adapters need to make.

### Key Legacy Modules as Reference

| Module | Value for v2 |
|--------|-------------|
| `legacy/builders/adapters/openapi/` | Reference for OpenAPI → IR normalization |
| `legacy/builders/adapters/raml/` | Reference for RAML → IR normalization |
| `legacy/codegen/schema/type_tree.py` | Strong reference for type closure traversal and naming |
| `legacy/codegen/schema/type_mapping.py` | Reference for IR → C# type mapping |
| `legacy/codegen/ir/composition.py` | Reference for flattening allOf, handling oneOf/anyOf |
| `legacy/builders/shared/schema_ids.py` | Reference for schema ID generation and hashing |
| `legacy/builders/shared/provenance.py` | Reference for provenance annotation |
| `legacy/codegen/generation/prompts.json` | Reference for C# code generation instructions |

---

## Requirements — Schmith v2

### Inputs

- An API spec file (OpenAPI 3.x or RAML 1.0)
- A specific endpoint (HTTP method + path, e.g. `GET /customers`)

### Output

- A C# DataObject class (or cluster of classes) representing the response schema for that endpoint
- This includes the root DataObject and all nested types required to fully define it

### Non-Goals

- Exhaustive DataObject generation for an entire spec
- Defining or pursuing any notion of "full API coverage"
- Handling endpoints other than the one explicitly requested

---

### Architecture

#### Stage 1 — Spec Parsing → IR

The spec is parsed by a format-specific adapter and normalized into an intermediate
representation. This stage is format-aware but API-agnostic.

- OpenAPI and RAML are supported via separate adapters
- The IR captures: operations, schemas (named and anonymous), serialization metadata,
  composition, and reference relationships
- Provenance is tracked throughout

This stage is largely portable from legacy.

#### Stage 2 — Endpoint Resolution

Given the endpoint input, the relevant operation is located in the IR and its response schema
node is identified. This produces the *candidate root* — the schema the spec associates with the
response.

#### Stage 3 — API Adapter: Root Resolution

The candidate root is passed to the API adapter's `resolve_root` hook. The adapter may return
the candidate unchanged (default) or may return a different node — for example, the item type
inside a pagination wrapper array.

This is the primary hook for addressing the array unwrapping problem and similar
platform-convention issues.

#### Stage 4 — Type Tree Construction

Starting from the resolved root, the full type tree is traversed and collected. All reachable
schemas — named and anonymous, at arbitrary depth — are included.

This stage uses logic descended from legacy's `type_tree.py`.

#### Stage 5 — API Adapter: Tree Transformation

The assembled type tree is passed to the API adapter's `transform_tree` hook. The adapter may
restructure, prune, annotate, or collapse nodes before code generation.

This hook addresses topology decisions: collapsing wrapper types, merging split schemas, marking
nodes for inlining, etc.

#### Stage 6 — Code Generation

The processed type tree is used to build a prompt packet and generate C# DataObject code via
LLM. The root type receives `[PrimaryKey]` and `[DataObject]` attributes. Nested types are
generated as supporting records and enums.

---

### API Adapter Interface

All hooks have default pass-through implementations. An API-specific adapter subclasses
`ApiAdapter` and overrides only the hooks it needs.

```python
class ApiAdapter:

    def resolve_root(self, endpoint: Endpoint, response_node: SchemaNode) -> SchemaNode:
        """
        Given the candidate root schema for an endpoint's response, return the
        schema node that is the actual DataObject.

        Use this to unwrap pagination envelopes, follow indirection, or select
        the correct branch of a union type.

        Default: return response_node unchanged.
        """
        return response_node

    def transform_tree(self, root: SchemaNode) -> SchemaNode:
        """
        Given the resolved root node, transform the type tree before class
        generation. The adapter may restructure, prune, annotate, or collapse
        nodes.

        Use this to: collapse wrapper types, rename nodes, merge schemas that
        the spec expresses separately, or mark nodes for inlining.

        Default: return root unchanged.
        """
        return root

    def name_anonymous(self, node: SchemaNode, context: NamingContext) -> str | None:
        """
        Provide a name for an anonymous schema node. Returning None defers to
        the general naming logic.

        Use this when the spec's anonymous inline object has a known conventional
        name within the API's platform.

        Default: return None.
        """
        return None

    def classify_node(self, node: SchemaNode, context: TreeContext) -> NodeClassification | None:
        """
        Classify a node in the type tree: should it become a named class, be
        inlined into its parent, or be collapsed away entirely?

        Returning None defers to the general classification heuristics.

        Default: return None.
        """
        return None
```

#### NodeClassification values

```python
class NodeClassification(Enum):
    NAMED_CLASS  # Generate as its own named record/class
    INLINE       # Fold properties into the parent class
    COLLAPSE     # Treat as transparent; follow through to children
```

---

### Invariants

The following must hold at all stages:

1. The general pipeline code must never import or reference a specific API adapter.
2. The default adapter (all pass-throughs) must produce valid, compilable output for any spec
   without requiring any adapter override.
3. All adapter hooks receive sufficient context to make their decisions without needing to
   reach outside the hook's arguments.
4. Anonymous type naming must be deterministic — identical inputs always produce identical names.
5. The type tree collected for generation must include every type referenced by the root DataObject,
   transitively, at arbitrary depth.

---

### Design Constraints

- **Python** — consistent with legacy
- **uv** for dependency management — consistent with legacy
- **LLM-based C# generation** — the generation approach from legacy is sound and carries forward
- **No config-driven filtering** — schema inclusion/exclusion decisions belong in adapter code,
  not in TOML filter files
- **Legacy is reference, not dependency** — v2 may draw patterns and logic from legacy but must
  not import from it
