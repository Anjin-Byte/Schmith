"""Schema ID generation utilities."""

from typing import Any, cast

from schmith.shared.hashing import canonical_json_hash

Schema = dict[str, Any]

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


def schema_id_for_schema(schema: object) -> str | None:
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
    # Safe: we just confirmed schema is a dict; the spec adapter always produces
    # string keys, so casting to Schema (dict[str, Any]) is correct here.
    s: Schema = cast(Schema, schema)

    ref = s.get("$ref")
    if isinstance(ref, str):
        return schema_id_from_ref(ref)

    # For schemas that are purely primitive (no enum, properties, or composition),
    # return the canonical schema:types/... ID so all property declarations of
    # the same base type share one ID rather than each getting a unique hash.
    # This means {"type":"string","description":"ID","example":"abc"} resolves
    # to schema:types/string rather than schema:anon/<hash>.
    schema_type = s.get("type")
    if (
        isinstance(schema_type, str)
        and schema_type in _PRIMITIVE_TYPES
        and not s.get("enum")
        and not s.get("properties")
        and not s.get("allOf")
        and not s.get("oneOf")
        and not s.get("anyOf")
        and not s.get("items")
    ):
        fmt: str = s.get("format", "")
        if schema_type == "string" and fmt in _FORMAT_TYPE_MAP:
            return f"schema:types/{_FORMAT_TYPE_MAP[fmt]}"
        return f"schema:types/{schema_type}"

    return f"schema:anon/{canonical_json_hash(schema)}"
