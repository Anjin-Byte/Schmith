"""Schema ID generation utilities."""

from typing import Any, Optional

from schmith.shared.hashing import canonical_json_hash

# OpenAPI primitive types that map to canonical schema:types/... IDs.
# Schemas that are ONLY primitive types (no enum, properties, or composition)
# share the same canonical ID regardless of description/example/format metadata.
_PRIMITIVE_TYPES = {"string", "integer", "number", "boolean", "null"}

# OpenAPI string formats that map to more specific IR types.
_FORMAT_TYPE_MAP = {
    "date-time": "datetime",
    "datetime": "datetime",
    "date": "date",
    "time": "time",
}


def schema_id_from_ref(ref: str) -> str:
    """Generate a schema ID from an OpenAPI $ref string.

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
    """Generate a schema ID for an OpenAPI schema object.

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

    # For schemas that are purely primitive (no enum, properties, or composition),
    # return the canonical schema:types/... ID so all property declarations of
    # the same base type share one ID rather than each getting a unique hash.
    # This means {"type":"string","description":"ID","example":"abc"} resolves
    # to schema:types/string rather than schema:anon/<hash>.
    schema_type = schema.get("type")
    if (
        isinstance(schema_type, str)
        and schema_type in _PRIMITIVE_TYPES
        and not schema.get("enum")
        and not schema.get("properties")
        and not schema.get("allOf")
        and not schema.get("oneOf")
        and not schema.get("anyOf")
        and not schema.get("items")
    ):
        fmt = schema.get("format", "")
        if schema_type == "string" and fmt in _FORMAT_TYPE_MAP:
            return f"schema:types/{_FORMAT_TYPE_MAP[fmt]}"
        return f"schema:types/{schema_type}"

    return f"schema:anon/{canonical_json_hash(schema)}"
