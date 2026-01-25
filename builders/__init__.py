"""IR Builders Package.

This package contains the IR (Intermediate Representation) builders that
extract structured data from API specifications.

Structure:
    adapters/           Format-specific extraction logic
        openapi/        OpenAPI/Swagger adapter
        raml/           RAML adapter
    shared/             Shared utilities (hashing, I/O, provenance)
    build_*.py          Orchestrator scripts that delegate to adapters

Each domain (operations, schemas, serialization, refs) has its own
orchestrator script that:
1. Loads the spec using the appropriate adapter
2. Extracts domain-specific data
3. Writes IR files to the output directory
"""
