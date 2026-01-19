# Phase 2 Tasks (Domain 1 — Operations)

This phase extracts OperationIR facts into the IR layout defined by:
- `ir_requirements/Domain_1_Operations/Domain_1_Operations.md`
- `ir_requirements/Domain_1_Operations/Domain_1_Operations_OpenAPI.md`
- `ir_requirements/Domain_1_Operations/Domain_1_Operations_RAML.md`
- `ir_requirements/Normalization_and_Availability_Policy.md`

## Tasks
- [ ] Define `OperationIR`, `OperationSurfaceIR`, `ParameterIR`, `BodyIR`, `ResponseIR` shapes in code.
- [ ] Implement OpenAPI extraction for:
  - method/path/operation_id
  - parameters (path/query/header/cookie)
  - request bodies by media type
  - responses by status code + media type
  - summary/description/tags
  - provenance pointers
- [ ] Implement RAML extraction for:
  - declared vs effective operations (traits/resourceTypes)
  - parameters by location
  - request/response bodies by media type
  - summary/description mapping
  - provenance and `via` chain
- [ ] Emit `operations/index.json` and per-operation detail files under `ir/<spec-name>/operations/`.
- [ ] Add availability markers for each canonical field (`native|adapter|absent`).
- [ ] Integrate output into `ir/<spec-name>/manifest.json` operation counts.
- [ ] Validate against `ir_requirements/Invariant_Test_1_Operation_Schema_Usage.md`.

## Notes
- Do not infer analysis-derived facts (keys, envelopes) in this phase.
- Keep output facts-only and preserve provenance for traceability.
