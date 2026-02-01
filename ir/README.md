# IR Output

This directory is the root for generated IR outputs.

- `template/` provides the required on-disk layout and minimal JSON shapes
  described in `ir_requirements/IR_Output_Contract.md`.
- The generator should write to `ir/<spec-name>/...` and leave `template/` intact.
