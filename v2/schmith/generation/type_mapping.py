"""Type mapping utilities for converting IR types to C# types."""

from __future__ import annotations

import re
from typing import Any

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
    if name_hint:
        name = name_hint
        if name.startswith("typ."):
            name = name[4:]
        return name
    if "anon/" in schema_id:
        return f"Anonymous_{schema_id.split('anon/')[-1][:8]}"
    return schema_id.split("/")[-1]


def _extract_template_discriminator(prefix: str, content: str) -> str:
    """Extract the meaningful snake_case discriminator from a %{...} placeholder.

    Strips common ID/definition suffixes and removes words that duplicate the
    surrounding property name prefix, leaving only the semantic discriminator.

    Examples:
        prefix="custom_field_", content="custom_field_boolean_definition_id"
          → "boolean"
        prefix="custom_field_", content="custom_field_lov_entry_definition_id"
          → "lov_entry"
    """
    for suffix in ("_definition_id", "_definition", "_id"):
        if content.endswith(suffix):
            content = content[:-len(suffix)]
            break

    prefix_parts = [p for p in re.split(r"[_\-\s]+", prefix.strip("_-")) if p]
    content_parts = [p for p in content.split("_") if p]

    # Skip content parts that match the start of the prefix
    i = 0
    while i < len(prefix_parts) and i < len(content_parts) and prefix_parts[i].lower() == content_parts[i].lower():
        i += 1
    remaining = content_parts[i:]
    if not remaining:
        remaining = content_parts[-1:]  # Fallback: take last part

    return "_".join(remaining)


def json_name_to_csharp_property(json_name: str) -> str:
    # Replace %{...} template placeholders with their semantic discriminator.
    # e.g. "custom_field_%{custom_field_boolean_definition_id}" → "custom_field_boolean"
    def _replace_template(m: re.Match) -> str:
        prefix = json_name[: m.start()]
        return _extract_template_discriminator(prefix, m.group(1))

    cleaned = re.sub(r"%\{([^}]+)\}", _replace_template, json_name)
    parts = re.split(r"[_\-\s]+", cleaned)
    return "".join(part.capitalize() for part in parts if part)


def _enum_meta(schema: dict) -> tuple[list, list] | tuple[None, None]:
    enum_values = schema.get("enum_values")
    if enum_values is None:
        enum_values = (schema.get("constraints") or {}).get("enum")
    enum_names = schema.get("enum_names")
    if enum_names is None:
        enum_names = schema.get("x-enumNames")
    if isinstance(enum_values, list):
        return enum_values, enum_names if isinstance(enum_names, list) else None
    return None, None


def is_shapeless_schema(
    schema: dict | None,
    schemas_by_id: dict[str, dict],
    depth: int = 0,
) -> bool:
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
        return is_shapeless_schema(schemas_by_id.get(addl_id), schemas_by_id, depth + 1)
    if kind == "array":
        items_id = schema.get("items_schema_id")
        if not items_id:
            return True
        return is_shapeless_schema(schemas_by_id.get(items_id), schemas_by_id, depth + 1)
    return False


def is_shapeless_schema_id(schema_id: str, schemas_by_id: dict[str, dict]) -> bool:
    return is_shapeless_schema(schemas_by_id.get(schema_id), schemas_by_id)


def schema_id_to_csharp_type(
    schema_id: str,
    schemas_by_id: dict[str, dict],
    nullable: bool | None = None,
) -> tuple[str, bool]:
    if schema_id in IR_TO_CSHARP_TYPE:
        return (IR_TO_CSHARP_TYPE[schema_id], False)
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
            return (extract_clean_name(schema_id, name_hint), False)
        return ("string", False)
    if kind == "array":
        items_id = schema.get("items_schema_id")
        if items_id:
            item_type, _ = schema_id_to_csharp_type(items_id, schemas_by_id)
            return (f"{item_type}[]", True)
        return ("object[]", True)
    name_hint = schema.get("name_hint")
    if name_hint:
        return (extract_clean_name(schema_id, name_hint), True)
    if kind in ("string", "integer", "number", "boolean"):
        return (IR_TO_CSHARP_TYPE.get(f"schema:types/{kind}", "object"), False)
    if is_shapeless_schema(schema, schemas_by_id):
        return ("JsonElement", False)
    return ("object", False)


def build_field_info(prop: dict, schemas_by_id: dict[str, dict]) -> dict[str, Any]:
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
        csharp_type = extract_clean_name(schema_id, name_hint) if name_hint else f"{csharp_name}Enum"

    items_schema_id = prop.get("items_schema_id")
    if items_schema_id and csharp_type == "object[]":
        item_type, _ = schema_id_to_csharp_type(items_schema_id, schemas_by_id)
        if item_type != "object":
            csharp_type = f"{item_type}[]"
            is_complex = True

    type_unresolved = csharp_type in ("object", "object[]")
    is_shapeless = is_shapeless_schema_id(schema_id, schemas_by_id) if schema_id else False

    nullable = prop.get("nullable")
    required = prop.get("required", False)
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
    if name.endswith("DataObject"):
        return name
    return f"{name}DataObject"
