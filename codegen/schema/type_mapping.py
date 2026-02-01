"""Type mapping utilities for converting IR types to C# types.

This module handles the conversion of IR schema types to their corresponding
C# type representations, including handling of arrays, nullable types, and
complex nested types.
"""

import re
from typing import Any

# Mapping from IR primitive schema IDs to C# types
IR_TO_CSHARP_TYPE: dict[str, str] = {
    "schema:types/string": "string",
    "schema:types/integer": "int",
    "schema:types/number": "double",
    "schema:types/boolean": "bool",
    "schema:types/datetime": "DateTime",
    "schema:types/date": "DateOnly",
    "schema:types/time": "TimeOnly",
    "schema:types/any": "JsonElement",
    "schema:types/array": "object[]",
    "schema:types/object": "object",
}


def extract_clean_name(schema_id: str, name_hint: str | None) -> str:
    """Extract a clean type name from schema_id or name_hint.

    Args:
        schema_id: The schema ID (e.g., "schema:types/typ.Customer")
        name_hint: Optional name hint from the schema

    Returns:
        Clean name suitable for C# class naming (e.g., "Customer")
    """
    if name_hint:
        name = name_hint
        # Strip common prefixes
        if name.startswith("typ."):
            name = name[4:]
        return name

    # Fall back to parsing schema_id
    if "anon/" in schema_id:
        hash_part = schema_id.split("anon/")[-1][:8]
        return f"Anonymous_{hash_part}"

    return schema_id.split("/")[-1]


def json_name_to_csharp_property(json_name: str) -> str:
    """Convert a JSON field name to a C# property name (PascalCase).

    Args:
        json_name: JSON field name (e.g., "customer_name", "first-name")

    Returns:
        PascalCase property name (e.g., "CustomerName", "FirstName")
    """
    parts = re.split(r"[_\-\s]+", json_name)
    return "".join(part.capitalize() for part in parts if part)


def _enum_meta(schema: dict) -> tuple[list, list] | tuple[None, None]:
    """Return enum values and names if present on a schema."""
    enum_values = schema.get("enum_values")
    if enum_values is None:
        enum_values = (schema.get("constraints") or {}).get("enum")
    enum_names = schema.get("enum_names")
    if enum_names is None:
        enum_names = schema.get("x-enumNames")
    if isinstance(enum_values, list):
        return enum_values, enum_names if isinstance(enum_names, list) else None
    return None, None


def schema_id_to_csharp_type(
    schema_id: str,
    schemas_by_id: dict[str, dict],
    nullable: bool | None = None,
) -> tuple[str, bool]:
    """Convert an IR schema_id to a C# type.

    Args:
        schema_id: The schema ID to convert
        schemas_by_id: Dictionary mapping schema IDs to schema data
        nullable: Whether the type should be nullable

    Returns:
        Tuple of (csharp_type, is_complex_type)
        - csharp_type: The C# type string (e.g., "string", "Customer", "int[]")
        - is_complex_type: True if this is a complex/object type
    """
    # Check primitive types first
    if schema_id in IR_TO_CSHARP_TYPE:
        return (IR_TO_CSHARP_TYPE[schema_id], False)

    # Look up the schema
    schema = schemas_by_id.get(schema_id)
    if not schema:
        return ("object", False)

    kind = schema.get("kind", "object")

    if kind in ("string", "integer", "number", "boolean", "datetime", "date", "time", "any"):
        return (IR_TO_CSHARP_TYPE.get(f"schema:types/{kind}", "object"), False)

    enum_values, _ = _enum_meta(schema)
    if enum_values is not None:
        name_hint = schema.get("name_hint")
        if name_hint:
            clean_name = extract_clean_name(schema_id, name_hint)
            return (clean_name, False)
        return ("string", False)

    # Handle arrays
    if kind == "array":
        items_id = schema.get("items_schema_id")
        if items_id:
            item_type, _ = schema_id_to_csharp_type(items_id, schemas_by_id)
            return (f"{item_type}[]", True)
        return ("object[]", True)

    # Handle named complex types
    name_hint = schema.get("name_hint")
    if name_hint:
        clean_name = extract_clean_name(schema_id, name_hint)
        return (clean_name, True)

    # Primitives by kind
    if kind in ("string", "integer", "number", "boolean"):
        return (IR_TO_CSHARP_TYPE.get(f"schema:types/{kind}", "object"), False)

    return ("object", False)


def is_shapeless_schema(
    schema: dict | None,
    schemas_by_id: dict[str, dict],
    depth: int = 0,
) -> bool:
    """Return True if a schema has no defined shape (free-form)."""
    if schema is None:
        return True
    if depth > 5:
        return False

    if schema.get("enum_values") or (schema.get("constraints") or {}).get("enum"):
        return False
    if schema.get("composition"):
        return False
    if schema.get("properties"):
        return False

    kind = schema.get("kind", "")
    if kind in ("any", "unknown"):
        return True

    if kind == "object":
        addl_id = schema.get("additional_properties_schema_id")
        if not addl_id:
            return True
        addl_schema = schemas_by_id.get(addl_id)
        # If additionalProperties is also shapeless/any, treat as shapeless
        return is_shapeless_schema(addl_schema, schemas_by_id, depth + 1)

    if kind == "array":
        items_id = schema.get("items_schema_id")
        if not items_id:
            return True
        items_schema = schemas_by_id.get(items_id)
        return is_shapeless_schema(items_schema, schemas_by_id, depth + 1)

    return False


def is_shapeless_schema_id(
    schema_id: str,
    schemas_by_id: dict[str, dict],
) -> bool:
    """Return True if a schema_id resolves to a shapeless schema."""
    return is_shapeless_schema(schemas_by_id.get(schema_id), schemas_by_id)


def build_field_info(
    prop: dict,
    schemas_by_id: dict[str, dict],
) -> dict[str, Any]:
    """Build field information for a schema property.

    Args:
        prop: Property definition from schema
        schemas_by_id: Dictionary mapping schema IDs to schema data

    Returns:
        Dictionary containing field metadata for code generation
    """
    json_name = prop.get("json_name", "")
    schema_id = prop.get("schema_id", "")
    description = (prop.get("description") or "").strip()

    csharp_type, is_complex = schema_id_to_csharp_type(schema_id, schemas_by_id)
    csharp_name = json_name_to_csharp_property(json_name)

    enum_values = prop.get("enum_values")
    enum_names = prop.get("enum_names")
    if enum_values is None:
        schema = schemas_by_id.get(schema_id) if schema_id else None
        if schema:
            enum_values, enum_names = _enum_meta(schema)

    if enum_values is not None:
        schema = schemas_by_id.get(schema_id) if schema_id else None
        name_hint = schema.get("name_hint") if schema else None
        if name_hint:
            csharp_type = extract_clean_name(schema_id, name_hint)
        else:
            csharp_type = f"{csharp_name}Enum"

    # For array properties with items_schema_id on the property itself, resolve the item type
    # Note: Most arrays have items_schema_id on the referenced schema, which is already
    # handled by schema_id_to_csharp_type. This handles the rare case where it's on the property.
    items_schema_id = prop.get("items_schema_id")
    if items_schema_id and csharp_type == "object[]":
        item_type, _ = schema_id_to_csharp_type(items_schema_id, schemas_by_id)
        if item_type != "object":
            csharp_type = f"{item_type}[]"
            is_complex = True

    # Flag fields where type resolution returned 'object' - this indicates
    # the IR may be missing data or the schema couldn't be resolved.
    # The LLM will see this flag and can make an informed decision.
    # NOTE: Previously this code used name-based fallback heuristics which
    # matched field names to nested type names. This was removed because
    # the IR provides schema_id references that should be used directly.
    type_unresolved = csharp_type in ("object", "object[]")
    is_shapeless = is_shapeless_schema_id(schema_id, schemas_by_id) if schema_id else False

    # Determine nullability
    nullable = prop.get("nullable")
    required = prop.get("required", False)

    # For non-required fields, default to nullable unless explicitly marked
    if not required and nullable is None:
        nullable = True

    constraints = prop.get("constraints")
    if constraints is None:
        schema = schemas_by_id.get(schema_id) if schema_id else None
        constraints = (schema or {}).get("constraints")

    return {
        "json_name": json_name,
        "csharp_name": csharp_name,
        "csharp_type": csharp_type,
        "is_complex_type": is_complex,
        "type_unresolved": type_unresolved,
        "description": description,
        "required": required,
        "nullable": nullable,
        "read_only": prop.get("read_only"),
        "write_only": prop.get("write_only"),
        "deprecated": prop.get("deprecated"),
        "schema_id": schema_id,
        "enum_values": enum_values,
        "enum_names": enum_names,
        "constraints": constraints,
        "is_shapeless": is_shapeless,
    }


def format_data_object_name(name: str) -> str:
    """Format a schema name as an XChange DataObject class name.

    Args:
        name: Schema name (e.g., "Customer")

    Returns:
        DataObject class name (e.g., "CustomerDataObject")
    """
    if name.endswith("DataObject"):
        return name
    return f"{name}DataObject"
