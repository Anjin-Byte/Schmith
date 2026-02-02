"""Type tree resolution for complete nested type definitions.

This module provides recursive type resolution to build a complete picture
of all types reachable from a root schema, stopping only at primitives.

The goal is to ensure code generation has full definitions for every
complex type referenced anywhere in the schema tree, regardless of whether
types are "owned" (inline) or defined elsewhere (named schemas).
"""

from typing import Any

from .type_mapping import IR_TO_CSHARP_TYPE, extract_clean_name, json_name_to_csharp_property


# Primitive schema IDs that don't need expansion
PRIMITIVE_SCHEMA_IDS = set(IR_TO_CSHARP_TYPE.keys())

# Primitive kinds that don't need type definitions
PRIMITIVE_KINDS = {"string", "integer", "number", "boolean", "null"}


def is_primitive_schema_id(schema_id: str) -> bool:
    """Check if a schema ID represents a primitive type."""
    return schema_id in PRIMITIVE_SCHEMA_IDS


def is_primitive_schema(schema: dict | None) -> bool:
    """Check if a schema represents a primitive type (by kind)."""
    if schema is None:
        return False
    kind = schema.get("kind", "")
    # A schema is primitive if it has a primitive kind and no properties
    if kind in PRIMITIVE_KINDS:
        return not schema.get("properties") and not schema.get("enum_values")
    return False


def get_primitive_type_name(schema: dict | None) -> str | None:
    """Get the C# type name for a primitive schema.

    Returns the type name (e.g., 'string', 'int') or None if not primitive.
    """
    if schema is None:
        return None
    kind = schema.get("kind", "")
    if kind not in PRIMITIVE_KINDS:
        return None
    if schema.get("properties") or schema.get("enum_values"):
        return None

    # Map IR kinds to C# types
    kind_to_csharp = {
        "string": "string",
        "integer": "int",
        "number": "double",
        "boolean": "bool",
        "null": "object",
    }
    return kind_to_csharp.get(kind, "object")


def resolve_type_name(
    schema_id: str,
    schema: dict | None,
    name_overrides: dict[str, str] | None = None,
) -> str | None:
    """Resolve a human-readable type name from schema ID and schema data.

    Args:
        schema_id: The schema ID
        schema: The schema data (may be None if not found)

    Returns:
        Type name suitable for code generation, or None if unresolvable
    """
    if is_primitive_schema_id(schema_id):
        return None  # Primitives don't need type definitions

    if schema is None:
        return None

    if name_overrides:
        override = name_overrides.get(schema_id)
        if override:
            return override

    name_hint = schema.get("name_hint")
    if name_hint:
        return extract_clean_name(schema_id, name_hint)

    # Try to extract from schema ID patterns
    if "definitions/" in schema_id:
        return schema_id.split("definitions/")[-1]
    if "components/" in schema_id:
        return schema_id.split("components/")[-1]
    if schema_id.startswith("schema:types/typ."):
        return schema_id.split("schema:types/typ.")[-1]
    if schema_id.startswith("schema:types/typ/"):
        return schema_id.split("schema:types/typ/")[-1]

    # For anonymous schemas without name_hint, generate a name from hash
    if "anon/" in schema_id:
        hash_part = schema_id.split("anon/")[-1][:8]
        return f"Anonymous_{hash_part}"

    return None


def collect_type_closure(
    root_schema: dict,
    schemas_by_id: dict[str, dict],
    load_schema_detail: callable = None,
) -> dict[str, dict]:
    """Collect the transitive closure of all types reachable from a root schema.

    Recursively follows all type references (properties, array items,
    additionalProperties) until only primitives remain. This ensures
    code generation has complete definitions for all nested types.

    Args:
        root_schema: The root schema to start from
        schemas_by_id: Dict mapping schema IDs to schema data
        load_schema_detail: Optional function to load full schema details
            by ID (for lazy loading from files)

    Returns:
        Dict mapping type names to their full schema definitions.
        Each entry contains:
        - schema_id: The original schema ID
        - name: The resolved type name
        - kind: Schema kind (object, array, etc.)
        - properties: List of property definitions with resolved types
        - All other schema fields
    """
    collected: dict[str, dict] = {}
    visited: set[str] = set()
    sources_by_id: dict[str, set[str]] = {}
    anon_name_overrides: dict[str, str] = {}
    used_type_names: set[str] = set()

    def mark_source(schema_id: str, source: str | None) -> None:
        if not schema_id or not source:
            return
        sources_by_id.setdefault(schema_id, set()).add(source)

    def get_schema(schema_id: str) -> dict | None:
        """Get schema data, loading from file if needed."""
        if schema_id in schemas_by_id:
            schema = schemas_by_id[schema_id]
            # If we only have index data, try to load full details
            if load_schema_detail and "properties" not in schema:
                full = load_schema_detail(schema_id)
                if full:
                    return full
            return schema
        if load_schema_detail:
            return load_schema_detail(schema_id)
        return None

    def collect_composition_properties(schema: dict) -> list[dict]:
        """Collect properties from allOf/oneOf/anyOf composition members."""
        composition = schema.get("composition")
        if not composition:
            return []

        members = composition.get("members", [])
        all_props = []
        seen_names = set()

        for member_id in members:
            member = get_schema(member_id)
            if not member:
                continue

            # Recursively collect from member's composition
            member_props = collect_composition_properties(member)
            for prop in member_props:
                name = prop.get("json_name")
                if name and name not in seen_names:
                    all_props.append(prop)
                    seen_names.add(name)

            # Collect direct properties from member
            for prop in member.get("properties", []):
                name = prop.get("json_name")
                if name and name not in seen_names:
                    all_props.append(prop)
                    seen_names.add(name)

        return all_props

    def reserve_type_name(schema_id: str, base_name: str) -> None:
        """Reserve a type name for a schema ID, ensuring uniqueness."""
        if not schema_id or not base_name:
            return
        name = base_name
        if name in used_type_names and anon_name_overrides.get(schema_id) != name:
            hash_part = schema_id.split("anon/")[-1][:6] if "anon/" in schema_id else "dedupe"
            name = f"{name}_{hash_part}"
        anon_name_overrides[schema_id] = name
        used_type_names.add(name)

    def maybe_name_inline_enum(
        parent_name: str | None,
        prop_name: str | None,
        enum_schema_id: str | None,
        suffix: str | None = None,
    ) -> None:
        """Assign a stable name to an inline enum schema based on parent + field."""
        if not enum_schema_id or "anon/" not in enum_schema_id:
            return
        # Allow overriding Anonymous names with proper names
        existing_name = anon_name_overrides.get(enum_schema_id)
        if existing_name:
            if not existing_name.startswith("Anonymous"):
                return
            if not parent_name or parent_name.startswith("Anonymous"):
                return
            used_type_names.discard(existing_name)
        field_part = json_name_to_csharp_property(prop_name or "")
        if parent_name and field_part:
            base = f"{parent_name}{field_part}"
        elif field_part:
            base = field_part
        elif parent_name:
            base = f"{parent_name}Enum"
        else:
            base = "AnonymousEnum"
        if suffix:
            base = f"{base}{suffix}"
        reserve_type_name(enum_schema_id, base)

    def maybe_name_inline_schema(
        parent_name: str | None,
        prop_name: str | None,
        schema_id: str | None,
        suffix: str | None = None,
        prefer_parent: bool = False,
    ) -> None:
        """Assign a stable name to an inline anonymous schema based on parent + field."""
        if not schema_id or "anon/" not in schema_id:
            return
        # Allow overriding Anonymous names with proper names
        existing_name = anon_name_overrides.get(schema_id)
        if existing_name:
            # If it already has a proper name (not Anonymous), keep it
            if not existing_name.startswith("Anonymous_"):
                return
            # It has an Anonymous name - we can try to give it a better one
            # Only proceed if we have a non-Anonymous parent
            if not parent_name or parent_name.startswith("Anonymous_"):
                return
            # Remove the old Anonymous name from used_type_names
            used_type_names.discard(existing_name)
        schema = get_schema(schema_id)
        if not schema:
            return
        # If schema has a name_hint, respect it based on prefer_parent and is_inline
        if schema.get("name_hint"):
            if not prefer_parent:
                return  # Use the existing name_hint
            if not schema.get("is_inline", False):
                return  # Schema is shared/referenced, keep its name_hint
        # Schema has no name - assign one based on parent context
        field_part = json_name_to_csharp_property(prop_name or "")
        if parent_name and field_part:
            base = f"{parent_name}{field_part}"
        elif field_part:
            base = field_part
        elif parent_name:
            base = f"{parent_name}Nested"
        else:
            base = "Anonymous"
        if suffix:
            base = f"{base}{suffix}"
        reserve_type_name(schema_id, base)

    def name_array_items_recursive(
        parent_name: str | None,
        prop_name: str | None,
        items_id: str,
        suffix: str = "Item",
    ) -> None:
        """Recursively name array items at any nesting depth.

        For nested arrays (array of arrays), each level gets an additional 'Item' suffix:
        - First level: ParentFieldItem
        - Second level: ParentFieldItemItem
        - Third level: ParentFieldItemItemItem
        - etc.
        """
        maybe_name_inline_schema(parent_name, prop_name, items_id, suffix=suffix, prefer_parent=True)
        items_schema = get_schema(items_id)
        if not items_schema:
            return

        # Handle composition members at this level
        if items_schema.get("composition"):
            members = items_schema["composition"].get("members", [])
            for member_id in members:
                maybe_name_inline_schema(parent_name, prop_name, member_id, suffix=suffix, prefer_parent=True)

        # Recurse into nested arrays
        if items_schema.get("kind") == "array":
            inner_items_id = items_schema.get("items_schema_id")
            if inner_items_id:
                name_array_items_recursive(parent_name, prop_name, inner_items_id, suffix=suffix + "Item")

    def process_schema(schema_id: str, source: str | None = None) -> str | None:
        """Process a schema, collecting it and its dependencies.

        Returns the resolved type name, or None for primitives.
        """
        # Skip primitives by schema ID
        if is_primitive_schema_id(schema_id):
            return None

        if source:
            mark_source(schema_id, source)

        schema = get_schema(schema_id)
        if not schema:
            return None

        # Skip primitives by kind (must check before cycle detection)
        if is_primitive_schema(schema):
            return None

        kind = schema.get("kind", "object")

        # Handle arrays BEFORE cycle detection - arrays don't produce named types,
        # they just return the item type with []. We need to handle them every time
        # they're referenced, not just the first time.
        if kind == "array":
            items_id = schema.get("items_schema_id")
            if items_id:
                # First try to process as complex type
                item_type = process_schema(items_id, source=source)
                if item_type:
                    return f"{item_type}[]"

                # If None, check if items are primitive
                items_schema = get_schema(items_id)
                primitive_type = get_primitive_type_name(items_schema)
                if primitive_type:
                    return f"{primitive_type}[]"

                # Unknown item type
                return "object[]"
            return "object[]"

        # For non-array types, apply cycle detection
        type_name = resolve_type_name(schema_id, schema, anon_name_overrides)
        if type_name:
            used_type_names.add(type_name)
        if schema_id in visited:
            return type_name
        visited.add(schema_id)

        # Handle enums
        if schema.get("enum_values"):
            if type_name and type_name not in collected:
                entry = _build_type_entry(schema_id, type_name, schema)
                sources = sources_by_id.get(schema_id)
                if sources:
                    entry["sources"] = sorted(sources)
                collected[type_name] = entry
            return type_name

        # Skip non-object types (except unknown which might have properties via composition)
        if kind not in ("object", "unknown"):
            return None

        # Collect properties: direct + from composition (allOf/oneOf/anyOf)
        properties = list(schema.get("properties", []))
        composition_props = collect_composition_properties(schema)

        # Merge composition properties (avoid duplicates)
        seen_names = {p.get("json_name") for p in properties}
        for prop in composition_props:
            if prop.get("json_name") not in seen_names:
                properties.append(prop)
                seen_names.add(prop.get("json_name"))

        # Also process composition members to collect their types
        composition = schema.get("composition")
        if composition:
            for member_id in composition.get("members", []):
                process_schema(member_id, source="composition")

        # Skip if no properties and no composition
        if not properties and not composition:
            return None

        if not type_name:
            return None

        # Collect this type if not already collected
        if type_name not in collected:
            # Process all properties to collect their types
            processed_props = []
            for prop in properties:
                prop_schema_id = prop.get("schema_id", "")
                items_schema_id = prop.get("items_schema_id")
                prop_name = prop.get("json_name")

                # Resolve the property's type
                prop_type_name = None
                if prop_schema_id:
                    enum_values = prop.get("enum_values")
                    if enum_values:
                        maybe_name_inline_enum(type_name, prop_name, prop_schema_id)
                    else:
                        maybe_name_inline_schema(type_name, prop_name, prop_schema_id, prefer_parent=True)
                    prop_schema = get_schema(prop_schema_id)
                    if prop_schema and prop_schema.get("kind") == "array":
                        items_id = prop_schema.get("items_schema_id")
                        if items_id:
                            name_array_items_recursive(type_name, prop_name, items_id)
                    prop_type_name = process_schema(prop_schema_id, source="property")

                # Handle array properties with items_schema_id on the property
                if items_schema_id and not prop_type_name:
                    items_schema = get_schema(items_schema_id)
                    if items_schema and items_schema.get("enum_values"):
                        maybe_name_inline_enum(type_name, prop_name, items_schema_id, suffix="Item")
                    else:
                        name_array_items_recursive(type_name, prop_name, items_schema_id)
                    item_type = process_schema(items_schema_id, source="property")
                    if item_type:
                        prop_type_name = f"{item_type}[]"

                processed_props.append({
                    **prop,
                    "resolved_type": prop_type_name,
                })

            entry = _build_type_entry(
                schema_id, type_name, schema, processed_props
            )
            sources = sources_by_id.get(schema_id)
            if sources:
                entry["sources"] = sorted(sources)
            collected[type_name] = entry

        # Handle additionalProperties
        addl_props_id = schema.get("additional_properties_schema_id")
        if addl_props_id:
            process_schema(addl_props_id, source="property")

        return type_name

    # Start from root schema
    root_id = root_schema.get("id", "")
    process_schema(root_id)

    return collected


def _build_type_entry(
    schema_id: str,
    type_name: str,
    schema: dict,
    processed_props: list[dict] | None = None,
) -> dict[str, Any]:
    """Build a type entry for the collected types dict."""
    props = processed_props if processed_props is not None else schema.get("properties", [])

    return {
        "schema_id": schema_id,
        "name": type_name,
        "kind": schema.get("kind", "object"),
        "description": schema.get("description"),
        "properties": props,
        "required": schema.get("required", []),
        "enum_values": schema.get("enum_values"),
        "enum_names": schema.get("enum_names"),
        "is_inline": schema.get("is_inline", False),
    }


def build_type_hierarchy(
    root_schema: dict,
    schemas_by_id: dict[str, dict],
    load_schema_detail: callable = None,
) -> tuple[dict, list[dict]]:
    """Build root type info and list of all nested types.

    This is a convenience function that separates the root type from
    its dependencies for prompt building.

    Args:
        root_schema: The root schema
        schemas_by_id: Dict mapping schema IDs to schema data
        load_schema_detail: Optional function to load full schema details

    Returns:
        Tuple of (root_type_info, nested_types_list)
        - root_type_info: The processed root type
        - nested_types_list: List of all other types in dependency order
    """
    all_types = collect_type_closure(root_schema, schemas_by_id, load_schema_detail)

    root_id = root_schema.get("id", "")
    root_name = resolve_type_name(root_id, root_schema)

    root_type = all_types.pop(root_name, None)
    if root_type is None:
        # Build root type entry if not in collected (shouldn't happen normally)
        root_type = _build_type_entry(root_id, root_name or "Root", root_schema)

    # Sort nested types alphabetically for consistent output
    nested_types = sorted(all_types.values(), key=lambda t: t["name"])

    return root_type, nested_types
