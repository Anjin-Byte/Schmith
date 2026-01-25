"""Schema ID generation utilities for OpenAPI specifications."""

from typing import Any, Optional

from builders.shared.hashing import canonical_json_hash


def schema_id_from_ref(ref: str) -> str:
    """
    Generate a schema ID from an OpenAPI $ref string.

    Args:
        ref: A JSON reference string (e.g., "#/components/schemas/Pet").

    Returns:
        A canonical schema ID (e.g., "schema:components/Pet").
    """
    if ref.startswith("#/components/schemas/"):
        return f"schema:components/{ref.split('/')[-1]}"
    if ref.startswith("#/components/"):
        return f"schema:components/{ref.lstrip('#/components/')}".replace("/", "_")
    if ref.startswith("#/definitions/"):
        return f"schema:definitions/{ref.split('/')[-1]}"
    return f"schema:ref/{ref.lstrip('#/')}".replace("/", "_")


def schema_id_for_schema(schema: Any) -> Optional[str]:
    """
    Generate a schema ID for an OpenAPI schema object.

    For schemas with $ref, returns the referenced schema ID.
    For inline schemas, returns an anonymous hash-based ID.

    Args:
        schema: An OpenAPI schema object (dict) or None.

    Returns:
        A schema ID string, or None if schema is not a dict.
    """
    if not isinstance(schema, dict):
        return None
    ref = schema.get("$ref")
    if isinstance(ref, str):
        return schema_id_from_ref(ref)
    return f"schema:anon/{canonical_json_hash(schema)}"
