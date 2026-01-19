# IR Migration Plan

This plan migrates the current `ResponseSchema`-based flow to the full IR described in
`ir_requirements/IR_Spec.md` and the on-disk layout in `ir_requirements/IR_Output_Contract.md`.
It keeps facts and decisions separate and aligns with the domain notes, policies, and invariant tests in
`ir_requirements/`.

## Phase 0: Baseline + Alignment
- Align on requirements in:
  - `ir_requirements/IR_Spec.md`
  - `ir_requirements/IR_Output_Contract.md`
  - `ir_requirements/Index.md`
- Use domain notes as source of truth:
  - `ir_requirements/Domain_1_Operations/Domain_1_Operations.md`
  - `ir_requirements/Domain_1_Operations/Domain_1_Operations_OpenAPI.md`
  - `ir_requirements/Domain_1_Operations/Domain_1_Operations_RAML.md`
  - `ir_requirements/Domain_2_Schemas_and_Fields/Domain_2_Schemas_and_Fields.md`
  - `ir_requirements/Domain_2_Schemas_and_Fields/Domain_2_Schemas_and_Fields_OpenAPI.md`
  - `ir_requirements/Domain_2_Schemas_and_Fields/Domain_2_Schemas_and_Fields_RAML.md`
  - `ir_requirements/Domain_3_Serialization_Surface/Domain_3_Serialization_Surface.md`
  - `ir_requirements/Domain_3_Serialization_Surface/Domain_3_Serialization_Surface_OpenAPI.md`
  - `ir_requirements/Domain_3_Serialization_Surface/Domain_3_Serialization_Surface_RAML.md`
  - `ir_requirements/Domain_4_Reference_Topology/Domain_4_Reference_Topology.md`
  - `ir_requirements/Domain_4_Reference_Topology/Domain_4_Reference_Topology_OpenAPI.md`
  - `ir_requirements/Domain_4_Reference_Topology/Domain_4_Reference_Topology_RAML.md`
- Adopt policies:
  - `ir_requirements/Normalization_and_Availability_Policy.md`
  - `ir_requirements/Invariant_Failure_Logging_Policy.md`
- Establish invariant test baseline:
  - `ir_requirements/Invariant_Tests_Index.md`
  - `ir_requirements/Invariant_Test_Requirement_Structure.md`
  - `ir_requirements/Redundant Invariants.md`
  - `ir_requirements/Cross-Domain Consistency Check Prompt.md`

## Phase 1: Introduce IR Layout (Facts-Only)
- Implement the on-disk layout from `ir_requirements/IR_Output_Contract.md`:
  - `ir/<spec-name>/manifest.json`
  - `ir/<spec-name>/operations/index.json`
  - `ir/<spec-name>/schemas/index.json`
  - `ir/<spec-name>/refs/edges.json`
  - `ir/<spec-name>/serialization/media_types.json`
  - `ir/<spec-name>/serialization/json_paths.json`
- Ensure required files and naming rules are met per `IR_Output_Contract.md`.
- Start with the “Minimal Next Step” listed in `IR_Spec.md`:
  1) `schemas/index.json`
  2) `operations/index.json`
  3) `refs/edges.json`

## Phase 2: Domain 1 — Operations
- Extract `OperationIR` with method, path, tags, and schema references.
- Capture declared vs effective surfaces (RAML traits/resourceTypes).
- Validate with:
  - `ir_requirements/Invariant_Test_1_Operation_Schema_Usage.md`
  - `ir_requirements/Domain_1_Operations/Domain_1_Operations.md`
  - `ir_requirements/Domain_1_Operations/Domain_1_Operations_OpenAPI.md`
  - `ir_requirements/Domain_1_Operations/Domain_1_Operations_RAML.md`
- Phase 2 task list: `docs/IR_PHASE2_TASKS.md`

## Phase 3: Domain 2 — Schemas + Fields
- Normalize schema and field details to `SchemaIR` and `FieldIR`.
- Preserve provenance pointers for traceability.
- Validate with:
  - `ir_requirements/Invariant_Test_2_Field_Name_Serialization.md`
  - `ir_requirements/Normalization_and_Availability_Policy.md`
  - `ir_requirements/Domain_2_Schemas_and_Fields/Domain_2_Schemas_and_Fields.md`
  - `ir_requirements/Domain_2_Schemas_and_Fields/Domain_2_Schemas_and_Fields_OpenAPI.md`
  - `ir_requirements/Domain_2_Schemas_and_Fields/Domain_2_Schemas_and_Fields_RAML.md`
- Phase 3 implementation: `scripts/build_ir_schemas.py`

## Phase 4: Domain 3 — Serialization Surface
- Record media types per request/response body.
- Record exact JSON field names/casing.
- Ensure `serialization/*` indexes fully cover Domain 1 + 2 facts per `IR_Output_Contract.md`.
- Validate with:
  - `ir_requirements/Invariant_Test_3_Media_Type_Mapping.md`
  - `ir_requirements/Domain_3_Serialization_Surface/Domain_3_Serialization_Surface.md`
  - `ir_requirements/Domain_3_Serialization_Surface/Domain_3_Serialization_Surface_OpenAPI.md`
  - `ir_requirements/Domain_3_Serialization_Surface/Domain_3_Serialization_Surface_RAML.md`
- Phase 4 implementation: `scripts/build_ir_serialization.py`

## Phase 5: Domain 4 — Reference Topology
- Build `refs/edges.json` and `refs/adjacency.json`.
- Validate with:
  - `ir_requirements/Invariant_Test_4_Reference_Edge_Consistency.md`
  - `ir_requirements/Domain_4_Reference_Topology/Domain_4_Reference_Topology.md`
  - `ir_requirements/Domain_4_Reference_Topology/Domain_4_Reference_Topology_OpenAPI.md`
  - `ir_requirements/Domain_4_Reference_Topology/Domain_4_Reference_Topology_RAML.md`
- Phase 5 implementation: `scripts/build_ir_refs.py`

## Phase 6: Provenance + Coverage
- Emit provenance files:
  - `ir/<spec-name>/provenance/sources.json`
  - `ir/<spec-name>/provenance/mapping.json`
- Validate with:
  - `ir_requirements/Invariant_Test_5_Provenance_Coverage.md`
  - `ir_requirements/Invariant_Failure_Logging_Policy.md`

## Phase 7: Analysis Outputs (Decisions)
- Move analysis results to `analysis/<spec-name>/...`.
- Include structured evidence and warnings per `IR_Spec.md`.
- Use `ir_requirements/Invariant_Failure_Logging_Policy.md` for standard error reports.
 - Reference process prompts as needed:
  - `ir_requirements/Domain Alignment Prompt.md`
  - `ir_requirements/Cross-Domain Consistency Check Prompt.md`
  - `ir_requirements/API_Specific_Alignment_Prompt.md`

## Phase 8: Deprecate ResponseSchema
- Keep `ResponseSchema` as a temporary compatibility shim.
- Switch analysis tools to IR outputs once stable, then remove the old response-centric reports.

## Notes
- Facts and decisions must remain separated as described in `ir_requirements/IR_Spec.md`.
- Use invariant tests as CI gates once the new IR is introduced.
