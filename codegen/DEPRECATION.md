# Deprecation Notice: Flat Prompt Packets

## Overview

Flat prompt packets are **deprecated** and will be removed in a future version.
Use **grouped packets** instead for proper nested type support.

## What's Being Deprecated

The following are deprecated and scheduled for removal:

### Methods in `prompt_packets.py`
- `PromptPacketBuilder.build_flat_packet()` - builds a single flat packet
- `PromptPacketBuilder.build_flat_packets()` - builds all flat packets

### CLI Behavior
- Running `python -m codegen packets <ir>` without `--grouped` flag
- Running `python -m codegen generate <ir>` without `--grouped` flag
- The `prompt_packets/flat/` directory structure

### Configuration
- Setting `grouped = false` in `config.toml` under `[generation]`

## Why Flat Packets Are Deprecated

Flat packets have a fundamental limitation: they generate one DataObject per schema
without understanding the relationships between parent and child schemas. This leads to:

1. **Missing nested types**: Deeply nested objects (grandchildren, great-grandchildren)
   are not included in the generated code
2. **Duplicate type definitions**: Related types may be generated separately instead
   of being grouped logically
3. **Incomplete context**: The LLM doesn't have full visibility into type relationships

Grouped packets solve these problems by:
- Including all nested types (children, grandchildren, etc.) in a single packet
- Providing the LLM with complete context about type relationships
- Generating cohesive DataObject files with all related types

## Migration Guide

### Step 1: Update CLI Usage

Before (deprecated):
```bash
python -m codegen packets servicefusion
python -m codegen generate servicefusion
```

After (recommended):
```bash
python -m codegen packets servicefusion --grouped
python -m codegen generate servicefusion --grouped
```

### Step 2: Update Configuration

In `codegen/config.toml`, ensure grouped is enabled:

```toml
[generation]
# Flat packets are DEPRECATED - use grouped packets
grouped = true
```

### Step 3: Update Code Using the Python API

Before (deprecated):
```python
builder = PromptPacketBuilder(loader)
for packet in builder.build_flat_packets():
    process(packet)
```

After (recommended):
```python
builder = PromptPacketBuilder(loader)
for packet in builder.build_grouped_packets():
    process(packet)
```

### Step 4: Clean Up Old Flat Packets

Once migrated, you can remove old flat packet directories:

```bash
rm -rf prompt_packets/flat/
```

## Already Removed (Legacy Heuristic Code)

The following legacy code that supported heuristic-based approaches has been removed:

### Removed from `schema_filter.py`
- `find_parent_child_relationships()` - Used naming conventions to guess parent-child
  relationships (e.g., "Customer" → "CustomerAddress"). Produced false positives.
  Replaced by `find_parent_child_relationships_from_ir()` which uses actual IR reference data.

### Removed from `type_mapping.py`
- `nested_type_names` parameter in `build_field_info()` - Was used for name-based type
  inference fallback. The IR now provides direct `schema_id` references that are authoritative.

These heuristic approaches were removed because they guessed relationships based on naming
patterns rather than using the actual schema reference data from the IR.

## Timeline

- **Current**: Deprecation warnings added; flat packets still functional; legacy heuristics removed
- **Next major version**: Flat packet methods will raise errors by default
- **Future version**: Flat packet code will be completely removed

## Questions?

If you have use cases that require flat packets and cannot migrate to grouped
packets, please open an issue to discuss your requirements.
