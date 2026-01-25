# Project Restructuring Migration Guide

## Overview

The project has been reorganized to improve maintainability and separate concerns:

- **`lib/`** - Shared utilities and common code
- **`builders/`** - IR building scripts (Domain extraction)
- **`tests/invariants/`** - Invariant validation tests
- **`tools/`** - One-off utilities and helper scripts

## Directory Structure

```
service_fusion/
├── lib/                      # Shared utilities
│   ├── __init__.py
│   └── ir_loader.py         # IRDataLoader class
│
├── builders/                 # IR building (Domain extraction)
│   ├── __init__.py
│   ├── build_operations.py  # Domain 1: Operations
│   ├── build_schemas.py     # Domain 2: Schemas
│   ├── build_serialization.py # Domain 3: Serialization
│   └── build_refs.py        # Domain 4: References
│
├── tests/invariants/         # Invariant tests
│   ├── __init__.py
│   ├── framework.py         # Test framework
│   ├── test_invariant_1.py  # Operation-Schema Usage
│   ├── test_invariant_2.py  # Field Name Serialization
│   ├── test_invariant_3.py  # Media Type Mapping (TODO)
│   └── run_all.py           # Test runner
│
├── tools/                    # Utilities
│   ├── sync_spec.py
│   ├── build_endpoint_model.py
│   └── ...
│
└── scripts/                  # DEPRECATED (to be removed)
```

## Import Changes

### Before (old structure)
```python
from invariant_test_framework import IRDataLoader, InvariantTest
```

### After (new structure)
```python
from lib.ir_loader import IRDataLoader
from tests.invariants.framework import InvariantTest
```

## Command Changes

### Builder Scripts

**Before:**
```bash
uv run python scripts/build_ir_schemas.py --config configs/servicefusion.toml
```

**After:**
```bash
uv run python builders/build_schemas.py --config configs/servicefusion.toml
```

### Test Scripts

**Before:**
```bash
uv run python scripts/validate_ir_invariant_1.py --config configs/servicefusion.toml
```

**After:**
```bash
uv run python tests/invariants/test_invariant_1.py --config configs/servicefusion.toml
```

**Run all tests:**
```bash
uv run python tests/invariants/run_all.py --config configs/servicefusion.toml -v -s
```

## Migration Steps

### Phase 1: Parallel Operation (Current)
- New structure created alongside old `scripts/` directory
- Both old and new paths work
- Old scripts remain functional during transition

### Phase 2: Update References
- [ ] Update `run.sh` to use new paths
- [ ] Update documentation to reference new locations
- [ ] Test all builders and tests with new structure

### Phase 3: Cleanup
- [ ] Archive old `scripts/` directory
- [ ] Remove deprecated files
- [ ] Update CI/CD pipelines (if any)

## Benefits

1. **Clear Separation of Concerns**
   - Builders vs Tests vs Tools vs Libraries

2. **Easier Navigation**
   - Related files grouped together
   - Clear purpose for each directory

3. **Better Imports**
   - Logical import paths (`from lib.ir_loader import ...`)
   - No more flat namespace pollution

4. **Scalability**
   - Easy to add new tests/builders/tools
   - Clear conventions to follow

5. **Maintainability**
   - Shared code in one place (`lib/`)
   - Test framework separate from implementation
