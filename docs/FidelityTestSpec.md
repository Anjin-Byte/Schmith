# Spec-to-IR Fidelity Test Suite Specification

**Version**: 1.0
**Status**: Draft
**Created**: 2026-01-25

---

## 1. Overview

### 1.1 Purpose

The Fidelity Test Suite validates that the IR (Intermediate Representation) accurately captures information from source API specifications. Unlike the existing Invariant tests which check internal IR consistency, Fidelity tests detect **data loss during extraction**.

### 1.2 Motivation

Bug investigation revealed that array item type information present in source specs was silently dropped during IR construction. All 5 existing invariant tests passed because the IR was internally consistent—the data loss was invisible.

### 1.3 Scope

| In Scope | Out of Scope |
|----------|--------------|
| RAML 1.0 specifications | OpenAPI adapter (separate spec) |
| Schema type information | Operation parameter validation |
| Property-level type references | Security scheme extraction |
| Array item types | Authentication flows |
| Nested/inline schema linking | Non-schema metadata |

---

## 2. Architecture

### 2.1 Test Flow

```
┌─────────────┐     ┌──────────────────┐     ┌─────────────────┐
│ Source Spec │────>│ Spec Parser      │────>│ Expected Facts  │
│ (RAML/OAS)  │     │ (adapter-aware)  │     │ (ground truth)  │
└─────────────┘     └──────────────────┘     └────────┬────────┘
                                                      │
                                                      │ compare
                                                      v
┌─────────────┐     ┌──────────────────┐     ┌─────────────────┐
│ IR Domains  │────>│ IR Loader        │────>│ Actual Facts    │
│ (JSON files)│     │ (existing)       │     │ (from IR)       │
└─────────────┘     └──────────────────┘     └────────┬────────┘
                                                      │
                                                      v
                                             ┌─────────────────┐
                                             │ Discrepancies   │
                                             │ (test failures) │
                                             └─────────────────┘
```

### 2.2 Directory Structure

```
tests/
├── invariants/           # Existing: IR-to-IR consistency
│   ├── framework.py
│   ├── run_all.py
│   └── test_invariant_*.py
│
└── fidelity/             # New: Spec-to-IR accuracy
    ├── __init__.py
    ├── framework.py      # Base class and utilities
    ├── spec_parser.py    # Adapter-aware spec parsing
    ├── run_all.py        # Run all fidelity tests
    ├── test_fidelity_1_array_items.py
    ├── test_fidelity_2_nested_schemas.py
    ├── test_fidelity_3_type_preservation.py
    └── test_fidelity_4_reference_completeness.py
```

### 2.3 Dependencies

- `lib.ir_loader.IRDataLoader` - existing IR loading
- `builders.shared.io.load_spec` - existing spec loading
- `pipeline.config` - existing configuration

---

## 3. Framework Specification

### 3.1 Base Class: `FidelityTest`

```python
class FidelityTest(ABC):
    """Base class for spec-to-IR fidelity tests."""

    def __init__(self, root_dir: str, spec_name: str, spec_path: str, adapter: str):
        """
        Args:
            root_dir: Project root directory
            spec_name: API name (e.g., "servicefusion")
            spec_path: Path to source specification file
            adapter: Spec format ("raml" or "openapi")
        """

    @property
    @abstractmethod
    def fidelity_id(self) -> str:
        """Unique identifier for this fidelity test."""

    @property
    @abstractmethod
    def output_filename(self) -> str:
        """Filename for the test report JSON."""

    @abstractmethod
    def extract_expected_facts(self, spec: dict) -> List[dict]:
        """Extract expected facts from source specification."""

    @abstractmethod
    def extract_actual_facts(self, loader: IRDataLoader) -> List[dict]:
        """Extract actual facts from IR."""

    @abstractmethod
    def compare_facts(
        self,
        expected: List[dict],
        actual: List[dict]
    ) -> List[dict]:
        """Compare expected vs actual, return discrepancies."""

    def run(self, verbose: bool = False) -> int:
        """Execute test and write report. Returns exit code."""

    def generate_report(self, discrepancies: List[dict]) -> dict:
        """Generate standardized JSON report."""
```

### 3.2 Report Format

```json
{
  "fidelity_id": "fidelity_1_array_items",
  "spec_name": "servicefusion",
  "spec_path": "spec/servicefusion/api.json",
  "adapter": "raml",
  "timestamp": "2026-01-25T10:30:00Z",
  "status": "FAIL",
  "summary": {
    "expected_count": 15,
    "actual_count": 12,
    "discrepancy_count": 3
  },
  "discrepancies": [
    {
      "location": "schema:types/typ.Customer.contacts",
      "expected": {
        "property_name": "contacts",
        "is_array": true,
        "items_type_name": "CustomerContact"
      },
      "actual": {
        "property_name": "contacts",
        "schema_id": "schema:types/array",
        "items_schema_id": null
      },
      "issue": "Array item type not preserved"
    }
  ]
}
```

### 3.3 Output Location

```
analysis/<spec_name>/fidelity/
├── fidelity_1_array_items.json
├── fidelity_2_nested_schemas.json
├── fidelity_3_type_preservation.json
└── fidelity_4_reference_completeness.json
```

---

## 4. Test Specifications

### 4.1 Fidelity Test 1: Array Item Type Preservation

#### 4.1.1 Purpose

Verify that array-typed properties with inline or referenced item types in the source spec have their item type information preserved in the IR.

#### 4.1.2 Preconditions

- Source spec exists and is parseable
- IR has been built for the spec
- IR schemas domain is populated

#### 4.1.3 Expected Facts Extraction (from Source Spec)

For RAML specs, extract all properties where:
- `type == "array"` AND
- `items` is defined (either inline object or type reference)

Capture:
```python
{
    "parent_schema": str,      # e.g., "typ.Customer"
    "property_name": str,      # e.g., "contacts"
    "items_type_name": str,    # e.g., "CustomerContact" or None if anonymous
    "items_is_inline": bool,   # True if items is inline definition
    "source_pointer": str,     # JSON pointer to property in spec
}
```

#### 4.1.4 Actual Facts Extraction (from IR)

For each IR schema, extract all properties where:
- `schema_id == "schema:types/array"`

Capture:
```python
{
    "parent_schema_id": str,   # e.g., "schema:types/typ.Customer"
    "property_name": str,      # e.g., "contacts"
    "property_schema_id": str, # e.g., "schema:types/array"
    "json_pointer": str,       # e.g., "$.contacts"
}
```

Also check the parent schema's `items_schema_id` field (though this is typically null for object schemas—the issue is at property level).

#### 4.1.5 Comparison Logic

```python
def compare_facts(expected, actual) -> List[Discrepancy]:
    discrepancies = []

    for exp in expected:
        # Find matching actual by parent_schema + property_name
        act = find_matching_actual(exp, actual)

        if act is None:
            discrepancies.append(MissingProperty(exp))
            continue

        # Check if IR preserves item type information
        # This requires checking if there's a way to recover items_type
        # from the IR (currently there isn't - that's the bug)

        if exp["items_type_name"] is not None:
            # Source spec has typed items
            # IR should have a reference to that type somehow
            if not ir_has_items_type_reference(act, exp["items_type_name"]):
                discrepancies.append(ItemTypeLost(exp, act))

    return discrepancies
```

#### 4.1.6 Pass Criteria

- PASS: All array properties with typed items in source spec have recoverable item type information in IR
- FAIL: Any array property loses its item type information

#### 4.1.7 Known Limitation

Currently, this test will **always fail** until the bug is fixed, because the IR schema property model doesn't have an `items_schema_id` field—only top-level array schemas do.

---

### 4.2 Fidelity Test 2: Nested Schema Completeness

#### 4.2.1 Purpose

Verify that inline/nested schema definitions in the source spec are:
1. Extracted as separate IR schemas
2. Properly linked from their parent context

#### 4.2.2 Expected Facts Extraction

For RAML specs, find all inline type definitions:
- Properties with `type` as an object (inline schema)
- Array `items` with object definitions
- `additionalProperties` with object definitions

Capture:
```python
{
    "parent_context": str,     # Where the inline schema appears
    "inline_name": str | None, # Name if provided (e.g., "CustomerContact")
    "inline_kind": str,        # "property_type" | "array_items" | "additional_props"
    "property_count": int,     # Number of properties in inline schema
    "source_pointer": str,
}
```

#### 4.2.3 Actual Facts Extraction

Search IR schemas for:
- Anonymous schemas (`schema:anon/*`)
- Named schemas that match inline definitions

Verify linkage exists from parent to nested schema.

#### 4.2.4 Pass Criteria

- PASS: Every inline schema in source has corresponding IR schema AND proper linkage
- FAIL: Any inline schema missing or unlinked

---

### 4.3 Fidelity Test 3: Type Information Preservation

#### 4.3.1 Purpose

Verify that type metadata survives extraction:
- Constraints (minLength, maxLength, pattern, minimum, maximum, etc.)
- Enums
- Formats (date-time, email, uri, etc.)
- Default values

#### 4.3.2 Expected Facts Extraction

For each property in source spec with type metadata:
```python
{
    "schema_name": str,
    "property_name": str,
    "constraints": {
        "minLength": int | None,
        "maxLength": int | None,
        "pattern": str | None,
        "minimum": number | None,
        "maximum": number | None,
        "enum": List[str] | None,
        "format": str | None,
        "default": Any | None,
    },
    "source_pointer": str,
}
```

#### 4.3.3 Actual Facts Extraction

From IR schema properties and constraints field:
```python
{
    "schema_id": str,
    "property_name": str,
    "constraints": dict,  # From schema["constraints"]
}
```

#### 4.3.4 Pass Criteria

- PASS: All constraints present in source are present in IR
- FAIL: Any constraint lost during extraction

---

### 4.4 Fidelity Test 4: Reference Relationship Completeness

#### 4.4.1 Purpose

Verify that ALL type relationships in source spec have corresponding edges in IR refs domain. Unlike Invariant 4, this test:
- Does NOT exclude primitive array types
- Validates from source spec perspective (not IR perspective)
- Catches missing edges due to extraction bugs

#### 4.4.2 Expected Facts Extraction

Extract all type references from source spec:
```python
{
    "from_type": str,          # Parent type name
    "to_type": str,            # Referenced type name
    "relationship": str,       # "property" | "items" | "additional_props"
    "property_name": str | None,
    "source_pointer": str,
}
```

Include:
- Property type references (non-primitive)
- Array items references
- additionalProperties references
- Composition references (allOf, oneOf, anyOf)

#### 4.4.3 Actual Facts Extraction

From IR refs/edges.json:
```python
{
    "from_schema_id": str,
    "to_schema_id": str,
    "kind": str,               # "property_ref" | "items_ref" | "additional_props_ref"
    "from_json_pointer": str,
}
```

#### 4.4.4 Comparison Logic

For each expected reference:
1. Resolve source type names to IR schema IDs
2. Check if corresponding edge exists in IR
3. Flag missing edges as discrepancies

#### 4.4.5 Pass Criteria

- PASS: Every type reference in source has corresponding IR edge
- FAIL: Any reference missing from IR edges

---

## 5. Spec Parser Specification

### 5.1 Purpose

The spec parser extracts "ground truth" facts from source specifications in an adapter-aware manner.

### 5.2 Interface

```python
class SpecParser(ABC):
    """Base class for spec format parsers."""

    @abstractmethod
    def parse_array_properties(self, spec: dict) -> List[ArrayPropertyFact]:
        """Extract all array properties with their item types."""

    @abstractmethod
    def parse_inline_schemas(self, spec: dict) -> List[InlineSchemaFact]:
        """Extract all inline schema definitions."""

    @abstractmethod
    def parse_type_constraints(self, spec: dict) -> List[TypeConstraintFact]:
        """Extract all type constraints and metadata."""

    @abstractmethod
    def parse_type_references(self, spec: dict) -> List[TypeReferenceFact]:
        """Extract all type-to-type references."""


class RAMLSpecParser(SpecParser):
    """Parser for RAML 1.0 specifications."""
    pass


class OpenAPISpecParser(SpecParser):
    """Parser for OpenAPI 3.x specifications."""
    pass


def get_parser(adapter: str) -> SpecParser:
    """Factory function for spec parsers."""
    if adapter == "raml":
        return RAMLSpecParser()
    elif adapter == "openapi":
        return OpenAPISpecParser()
    raise ValueError(f"Unknown adapter: {adapter}")
```

### 5.3 RAML Parser: Array Property Extraction

```python
def parse_array_properties(self, spec: dict) -> List[ArrayPropertyFact]:
    """
    Walk RAML spec types and extract array properties.

    RAML array property structure:
    {
        "type": "array",
        "items": {
            "type": "object",
            "name": "CustomerContact",  # May or may not be present
            "properties": [...]
        },
        "name": "contacts"
    }
    """
    facts = []

    types = spec.get("types", {})
    for type_name, type_def in types.items():
        if not isinstance(type_def, dict):
            continue

        properties = type_def.get("properties", [])
        for prop in properties:
            if prop.get("type") == "array":
                items = prop.get("items", {})
                facts.append(ArrayPropertyFact(
                    parent_schema=type_name,
                    property_name=prop.get("name"),
                    items_type_name=items.get("name") if isinstance(items, dict) else None,
                    items_is_inline=isinstance(items, dict) and "properties" in items,
                    source_pointer=f"types.{type_name}.properties.{prop.get('name')}",
                ))

    return facts
```

---

## 6. Execution

### 6.1 Command Line Interface

```bash
# Run all fidelity tests for an API
python -m tests.fidelity.run_all --config configs/servicefusion.toml

# Run specific fidelity test
python tests/fidelity/test_fidelity_1_array_items.py --config configs/servicefusion.toml

# Verbose output
python -m tests.fidelity.run_all --config configs/servicefusion.toml -v

# Run both invariants and fidelity tests
./run_tests.sh  # Updated to include fidelity suite
```

### 6.2 Exit Codes

| Code | Meaning |
|------|---------|
| 0 | All tests passed |
| 1 | One or more tests failed |
| 2 | Configuration or runtime error |

### 6.3 Integration with CI

```yaml
# Example GitHub Actions step
- name: Run Fidelity Tests
  run: |
    python -m tests.fidelity.run_all --config configs/servicefusion.toml
    python -m tests.fidelity.run_all --config configs/ukg_v2_client.toml
```

---

## 7. Implementation Priority

| Priority | Test | Rationale |
|----------|------|-----------|
| **P0** | Fidelity 1: Array Items | Directly catches the investigated bug |
| **P1** | Fidelity 4: Reference Completeness | Catches broader class of linkage bugs |
| **P2** | Fidelity 2: Nested Schemas | Validates inline schema extraction |
| **P3** | Fidelity 3: Type Preservation | Lower severity data loss |

---

## 8. Success Metrics

### 8.1 Test Effectiveness

The fidelity suite is successful if:
1. **Fidelity 1 fails** on current codebase (proves it catches the known bug)
2. **Fidelity 1 passes** after bug fix is applied
3. No new extraction bugs reach production undetected

### 8.2 Coverage Goals

| Metric | Target |
|--------|--------|
| Array properties validated | 100% of typed arrays |
| Inline schemas validated | 100% of inline definitions |
| Type constraints validated | 100% of constraint fields |
| Reference edges validated | 100% of non-primitive refs |

---

## 9. Open Questions

1. **OpenAPI adapter**: Should fidelity tests cover OpenAPI immediately or be RAML-only initially?
2. **Performance**: For large specs, should fact extraction be cached?
3. **Granularity**: Should discrepancies be reported per-property or aggregated per-schema?
4. **Fix verification**: Should fidelity tests be run as part of the bug fix PR validation?

---

## 10. Appendix: Data Structures

### 10.1 Fact Types

```python
@dataclass
class ArrayPropertyFact:
    parent_schema: str
    property_name: str
    items_type_name: str | None
    items_is_inline: bool
    source_pointer: str

@dataclass
class InlineSchemaFact:
    parent_context: str
    inline_name: str | None
    inline_kind: str  # "property_type" | "array_items" | "additional_props"
    property_count: int
    source_pointer: str

@dataclass
class TypeConstraintFact:
    schema_name: str
    property_name: str
    constraints: dict
    source_pointer: str

@dataclass
class TypeReferenceFact:
    from_type: str
    to_type: str
    relationship: str  # "property" | "items" | "additional_props"
    property_name: str | None
    source_pointer: str

@dataclass
class Discrepancy:
    location: str
    expected: dict
    actual: dict
    issue: str
```
