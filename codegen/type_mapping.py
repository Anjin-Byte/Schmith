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


def build_field_info(
    prop: dict,
    schemas_by_id: dict[str, dict],
    nested_type_names: set[str] | None = None,
) -> dict[str, Any]:
    """Build field information for a schema property.

    Args:
        prop: Property definition from schema
        schemas_by_id: Dictionary mapping schema IDs to schema data
        nested_type_names: Optional set of nested type names for type inference

    Returns:
        Dictionary containing field metadata for code generation
    """
    json_name = prop.get("json_name", "")
    schema_id = prop.get("schema_id", "")
    description = (prop.get("description") or "").strip()

    csharp_type, is_complex = schema_id_to_csharp_type(schema_id, schemas_by_id)
    csharp_name = json_name_to_csharp_property(json_name)

    # Check if this field should use a nested type
    if nested_type_names and csharp_type == "object":
        for nested_name in nested_type_names:
            if nested_name.lower().endswith(json_name.lower()):
                csharp_type = nested_name
                is_complex = True
                break

    # Determine nullability
    nullable = prop.get("nullable")
    required = prop.get("required", False)

    # For non-required fields, default to nullable unless explicitly marked
    if not required and nullable is None:
        nullable = True

    return {
        "json_name": json_name,
        "csharp_name": csharp_name,
        "csharp_type": csharp_type,
        "is_complex_type": is_complex,
        "description": description,
        "required": required,
        "nullable": nullable,
        "read_only": prop.get("read_only"),
        "write_only": prop.get("write_only"),
        "deprecated": prop.get("deprecated"),
        "schema_id": schema_id,
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
