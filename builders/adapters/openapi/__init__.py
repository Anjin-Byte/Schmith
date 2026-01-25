"""OpenAPI/Swagger specification adapter."""

from builders.adapters.openapi.operations import extract_operations
from builders.adapters.openapi.schemas import extract_schemas
from builders.adapters.openapi.serialization import extract_serialization

__all__ = [
    "extract_operations",
    "extract_schemas",
    "extract_serialization",
]
