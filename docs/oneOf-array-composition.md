# oneOf Array Composition Handling

## Overview

This document describes how the Schmith IR and codegen pipeline handles `oneOf` compositions where the variants are arrays. This pattern is common in APIs that support multiple "views" of the same resource (e.g., default, extended, compact).

## The Pattern

Many APIs return different field sets based on query parameters. In OpenAPI, this is often modeled as:

```yaml
responses:
  200:
    content:
      application/json:
        schema:
          type: object
          properties:
            data:
              oneOf:
                - type: array
                  title: default
                  items:
                    # 26 base fields
                - type: array
                  title: extended
                  items:
                    # 26 base fields + 10 extra fields
                - type: array
                  title: ids_only
                  items:
                    # just id field
```

## The Problem

Prior to the fix, `collect_composition_properties()` in `type_tree.py` only collected properties from composition members that were objects. When members were arrays, it would:

1. See the `oneOf` composition
2. Look at each member (arrays)
3. Find no direct `properties` on the arrays
4. Return an empty field list

This resulted in schemas like `GETProjectsCommitmentContractsResponse200Data` showing **0 fields** even though the array items had 29 fields combined across variants.

## The Solution

Modified `collect_composition_properties()` to descend into array `items_schema_id` when processing composition members:

```python
def collect_from_member(member: dict) -> None:
    """Collect properties from a member, descending into arrays."""

    # If member is an array, descend into items schema
    if member.get("kind") == "array":
        items_id = member.get("items_schema_id")
        if items_id:
            items_schema = get_schema(items_id)
            if items_schema:
                collect_from_member(items_schema)
        return

    # Collect properties from object schemas
    # ... (existing logic)
```

## Semantic Implications

### What This Means for Generated Code

The fix **merges properties from all oneOf variants** into a single field list. For example:

| Variant | Fields |
|---------|--------|
| `default` | id, type, number, status, ... (26 fields) |
| `extended` | all default fields + custom_fields, external_data, vendor (29 fields) |
| `ids_only` | id (1 field) |

**Result:** The generated schema shows all 29 fields as if they're always present.

### Trade-offs

| Approach | Pros | Cons |
|----------|------|------|
| **Merge all fields (current)** | Simple, complete | Over-promises field presence |
| **Discriminated union** | Accurate per-variant | Complex, more types to generate |
| **Base fields only** | Conservative | Loses variant-specific fields |

### When This Matters

1. **Nullable fields are fine** - If all fields are treated as potentially null/optional, the merged approach works well.

2. **Required fields are risky** - If codegen marks fields as non-null based on `required`, the `ids_only` variant will fail validation.

3. **LLM prompts are affected** - The LLM sees all 29 fields when generating code, which could lead to it expecting fields that aren't always present.

## Affected Schemas

This pattern appears in several Procore API endpoints:

- `/commitment_contracts` - default, extended, ids_only views
- `/prime_contracts` - similar view pattern
- `/budget/views` - multiple response shapes
- Many other list endpoints with configurable response detail

## Detection

Schemas affected by this pattern can be identified by:

1. Having `composition.kind == "oneOf"` or `"anyOf"`
2. Where all members have `kind == "array"`
3. And item schemas have different property sets

## Future Considerations

### Option 1: Add Variant Metadata

Enhance the prompt packet to indicate which fields belong to which variant:

```json
{
  "fields": [
    {"name": "id", "variants": ["default", "extended", "ids_only"]},
    {"name": "custom_fields", "variants": ["extended"]},
    ...
  ]
}
```

### Option 2: Discriminated Union Generation

Generate separate types per variant:

```csharp
// Base interface
interface ICommitmentContract { ... }

// Variant types
class DefaultCommitmentContract : ICommitmentContract { ... }
class ExtendedCommitmentContract : DefaultCommitmentContract { ... }
class IdsOnlyCommitmentContract : ICommitmentContract { ... }
```

### Option 3: Response Wrapper with Variant Info

Include variant information in the response wrapper:

```csharp
class CommitmentContractsResponse {
    public string View { get; set; } // "default", "extended", "ids_only"
    public CommitmentContract[] Data { get; set; }
}
```

## Related Changes

This fix also required updates to the serialization adapter to maintain IR consistency:

1. **Composition traversal** - `collect_inline_json_paths()` now processes `allOf`/`oneOf`/`anyOf` members
2. **additionalProperties traversal** - Nested schemas in dictionary types are now registered

These changes ensured `invariant_2_field_name_serialization` continues to pass.

## References

- Fix commit: `type_tree.py` - `collect_composition_properties()` array handling
- Fix commit: `serialization.py` - composition and additionalProperties traversal
- Related issue: Empty Fields section for `GETProjectsCommitmentContractsResponse200Data`
