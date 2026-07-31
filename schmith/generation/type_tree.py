"""Type tree resolution for complete nested type definitions.

This module provides recursive type resolution to build a complete picture
of all types reachable from a root schema, stopping only at primitives.

The goal is to ensure code generation has full definitions for every
complex type referenced anywhere in the schema tree, regardless of whether
types are "owned" (inline) or defined elsewhere (named schemas).

Architecture:
- SchemaEdge: Uniform representation of any reference between schemas
- NamingContext: Propagated context for generating names during traversal
- extract_all_edges: Single function that extracts all edges from any schema
- traverse_and_name: Single recursive function that handles all nesting patterns

Adapter hooks:
- adapter.name_anonymous(node, ctx) is called during phase 1 for anonymous
  schemas, before falling back to build_name_from_context.
- adapter.classify_node(node, tree_ctx) is called during phase 2 before a
  schema is added to the collected set. INLINE → skip entirely; COLLAPSE →
  process children but don't emit a type entry; None/NAMED_CLASS → normal.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any, Callable, Literal

from schmith.adapters.base import ApiAdapter, NodeClassification, TreeContext
from schmith.generation.type_mapping import (
    IR_TO_CSHARP_TYPE,
    extract_clean_name,
    is_shapeless_schema,
    json_name_to_csharp_property,
)
from schmith.ir.models import SchemaNode


# Primitive schema IDs that don't need expansion
PRIMITIVE_SCHEMA_IDS = set(IR_TO_CSHARP_TYPE.keys())

# Primitive kinds that don't need type definitions
PRIMITIVE_KINDS = {"string", "integer", "number", "boolean", "null"}


# -----------------------------------------------------------------------------
# Data Structures for Generalized Traversal
# -----------------------------------------------------------------------------


@dataclass
class SchemaEdge:
    """A reference from one schema to another.

    This provides a uniform representation for all types of schema references:
    properties, array items, composition members, and additionalProperties.
    """

    target_id: str
    edge_kind: Literal["property", "array_items", "composition_member", "additional_properties"]
    property_name: str | None = None  # For naming context (e.g., "items", "data")
    has_enum: bool = False  # Whether the target is an enum


@dataclass
class NamingContext:
    """Propagated context during traversal for generating names.

    This context flows through the schema graph, accumulating information
    needed to generate meaningful names for anonymous schemas.
    """

    parent_name: str | None  # Name of the containing type
    property_name: str | None  # Name of the property/field that led here
    suffix_stack: list[str] = field(default_factory=list)  # ["Item"] for arrays
    visited: set[str] = field(default_factory=set)  # Cycle detection (shared)

    def child_context(
        self,
        new_parent: str | None = None,
        new_property: str | None = None,
        add_suffix: str | None = None,
        reset_suffix: bool = False,
    ) -> "NamingContext":
        """Create a child context for recursion.

        When *reset_suffix* is True the suffix stack is cleared before any
        *add_suffix* is applied.  Use this for property / composition edges so
        an "Item" suffix accumulated while naming array-item schemas does not
        bleed into unrelated property children of those schemas.
        """
        new_suffix_stack = [] if reset_suffix else self.suffix_stack.copy()
        if add_suffix:
            new_suffix_stack.append(add_suffix)
        return NamingContext(
            parent_name=new_parent if new_parent is not None else self.parent_name,
            property_name=new_property,
            suffix_stack=new_suffix_stack,
            visited=self.visited,  # Shared reference for cycle detection
        )


# -----------------------------------------------------------------------------
# Primitive Detection
# -----------------------------------------------------------------------------


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

    kind_to_csharp = {
        "string": "string",
        "integer": "int",
        "number": "double",
        "boolean": "bool",
        "null": "object",
    }
    return kind_to_csharp.get(kind, "object")


# -----------------------------------------------------------------------------
# Edge Extraction (The ONLY place with schema-kind-specific logic)
# -----------------------------------------------------------------------------


def extract_all_edges(schema: dict, get_schema_fn: Callable[[str], dict | None]) -> list[SchemaEdge]:
    """Extract all outgoing edges from a schema.

    This is the single point of schema-kind-specific logic. All types of
    references (properties, arrays, compositions, additionalProperties) are
    normalized into a uniform edge representation.
    """
    edges: list[SchemaEdge] = []
    kind = schema.get("kind", "object")

    # 1. Properties (objects have these directly, compositions inherit them)
    for prop in schema.get("properties", []):
        prop_schema_id = prop.get("schema_id")
        prop_items_id = prop.get("items_schema_id")
        prop_name = prop.get("json_name")
        has_enum = bool(prop.get("enum_values"))

        if prop_schema_id:
            # Check if this property points to an array
            prop_schema = get_schema_fn(prop_schema_id)
            if prop_schema and prop_schema.get("kind") == "array":
                # Add edge to the array schema itself (for processing)
                edges.append(SchemaEdge(
                    target_id=prop_schema_id,
                    edge_kind="property",
                    property_name=prop_name,
                    has_enum=has_enum,
                ))
                # Also add edge to array items
                items_id = prop_schema.get("items_schema_id")
                if items_id:
                    items_schema = get_schema_fn(items_id)
                    items_has_enum = bool(items_schema.get("enum_values")) if items_schema else False
                    edges.append(SchemaEdge(
                        target_id=items_id,
                        edge_kind="array_items",
                        property_name=prop_name,
                        has_enum=items_has_enum,
                    ))
            else:
                edges.append(SchemaEdge(
                    target_id=prop_schema_id,
                    edge_kind="property",
                    property_name=prop_name,
                    has_enum=has_enum,
                ))

        # Handle properties with direct items_schema_id (legacy format)
        if prop_items_id:
            items_schema = get_schema_fn(prop_items_id)
            items_has_enum = bool(items_schema.get("enum_values")) if items_schema else False
            edges.append(SchemaEdge(
                target_id=prop_items_id,
                edge_kind="array_items",
                property_name=prop_name,
                has_enum=items_has_enum,
            ))

    # 2. Array items (for array schemas)
    if kind == "array":
        items_id = schema.get("items_schema_id")
        if items_id:
            items_schema = get_schema_fn(items_id)
            items_has_enum = bool(items_schema.get("enum_values")) if items_schema else False
            edges.append(SchemaEdge(
                target_id=items_id,
                edge_kind="array_items",
                property_name=None,
                has_enum=items_has_enum,
            ))

    # 3. Composition members (allOf/oneOf/anyOf)
    composition = schema.get("composition")
    if composition:
        for member_id in composition.get("members", []):
            edges.append(SchemaEdge(
                target_id=member_id,
                edge_kind="composition_member",
                property_name=None,
                has_enum=False,
            ))

    # 4. Additional properties
    addl_props_id = schema.get("additional_properties_schema_id")
    if addl_props_id:
        addl_schema = get_schema_fn(addl_props_id)
        addl_has_enum = bool(addl_schema.get("enum_values")) if addl_schema else False
        edges.append(SchemaEdge(
            target_id=addl_props_id,
            edge_kind="additional_properties",
            property_name="AdditionalProperties",
            has_enum=addl_has_enum,
        ))

    return edges


# -----------------------------------------------------------------------------
# Type Name Resolution
# -----------------------------------------------------------------------------


def resolve_type_name(
    schema_id: str,
    schema: dict | None,
    name_overrides: dict[str, str] | None = None,
) -> str | None:
    """Resolve a human-readable type name from schema ID and schema data."""
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


# -----------------------------------------------------------------------------
# Naming Helpers
# -----------------------------------------------------------------------------


def _trim_parent_name(name: str | None, max_words: int = 3) -> str | None:
    """Trim a PascalCase parent name to at most *max_words* trailing words.

    Prevents deeply-nested anonymous schemas from accumulating excessively long
    type names by capping how much parent context is propagated.

    Example (max_words=3):
        "TimesheetEntriesCustomFieldsItem" → "EntriesCustomFieldsItem"  (5→3)
        "CompanyUser" → "CompanyUser"  (2≤3, unchanged)
    """
    if name is None:
        return None
    words = re.findall(r"[A-Z][a-z0-9]*", name)
    if len(words) <= max_words:
        return name
    return "".join(words[-max_words:])


# -----------------------------------------------------------------------------
# Main Collection Function
# -----------------------------------------------------------------------------


def collect_type_closure(
    root_schema: dict[str, Any],
    schemas_by_id: dict[str, dict[str, Any]],
    load_schema_detail: Callable[[str], dict[str, Any] | None] | None = None,
    adapter: ApiAdapter | None = None,
) -> dict[str, dict[str, Any]]:
    """Collect the transitive closure of all types reachable from a root schema.

    Uses a two-phase approach:
    1. Naming phase: traverse and assign names to all anonymous schemas.
    2. Collection phase: traverse and collect type definitions.

    If an adapter is provided, two hooks are called:
    - adapter.name_anonymous(node, ctx) during phase 1, before falling back
      to build_name_from_context.
    - adapter.classify_node(node, tree_ctx) during phase 2, before adding a
      type to the collected set. INLINE skips the type entirely; COLLAPSE
      processes children but omits the type entry; None/NAMED_CLASS is normal.
    """
    collected: dict[str, dict[str, Any]] = {}
    visited: set[str] = set()
    sources_by_id: dict[str, set[str]] = {}
    anon_name_overrides: dict[str, str] = {}
    used_type_names: set[str] = set()

    root_id = root_schema.get("id", "")

    # -------------------------------------------------------------------------
    # Helper Functions
    # -------------------------------------------------------------------------

    def mark_source(schema_id: str, source: str | None) -> None:
        if not schema_id or not source:
            return
        sources_by_id.setdefault(schema_id, set()).add(source)

    def get_schema(schema_id: str) -> dict | None:
        """Get schema data, loading from file if needed."""
        if schema_id in schemas_by_id:
            schema = schemas_by_id[schema_id]
            if load_schema_detail and "properties" not in schema:
                full = load_schema_detail(schema_id)
                if full:
                    return full
            return schema
        if load_schema_detail:
            return load_schema_detail(schema_id)
        return None

    def reserve_type_name(schema_id: str, base_name: str) -> str:
        """Reserve a type name for a schema ID, ensuring uniqueness."""
        if not schema_id or not base_name:
            return base_name
        name = base_name
        if name in used_type_names and anon_name_overrides.get(schema_id) != name:
            hash_part = schema_id.split("anon/")[-1][:6] if "anon/" in schema_id else "dedupe"
            name = f"{name}_{hash_part}"
        anon_name_overrides[schema_id] = name
        used_type_names.add(name)
        return name

    def build_name_from_context(ctx: NamingContext, is_enum: bool = False) -> str:
        """Build a type name from naming context.

        The parent name is trimmed to at most 3 PascalCase words so that
        deeply-nested anonymous schemas don't accumulate runaway prefixes.
        """
        field_part = json_name_to_csharp_property(ctx.property_name or "")
        suffix = "".join(ctx.suffix_stack)
        parent = _trim_parent_name(ctx.parent_name)

        if parent and field_part:
            base = f"{parent}{field_part}"
        elif field_part:
            base = field_part
        elif parent:
            base = f"{parent}{'Enum' if is_enum else 'Nested'}"
        else:
            base = "AnonymousEnum" if is_enum else "Anonymous"

        if suffix:
            base = f"{base}{suffix}"
        return base

    def should_name_schema(schema_id: str, schema: dict | None, ctx: NamingContext) -> bool:
        """Determine if a schema needs a name assigned."""
        if not schema_id or "anon/" not in schema_id:
            return False  # Not anonymous

        existing_name = anon_name_overrides.get(schema_id)
        if existing_name:
            # Already has a proper name
            if not existing_name.startswith("Anonymous"):
                return False
            # Has Anonymous name — can upgrade if we have better context
            if not ctx.parent_name or ctx.parent_name.startswith("Anonymous"):
                return False
            # Remove old name to allow upgrade
            used_type_names.discard(existing_name)

        if not schema:
            return False

        # If schema has a name_hint, its name is already determined
        if schema.get("name_hint"):
            return False

        return True

    # -------------------------------------------------------------------------
    # Phase 1: Unified Naming Traversal
    # -------------------------------------------------------------------------

    def traverse_and_name(
        schema_id: str,
        ctx: NamingContext,
        edge_kind: str | None = None,
        depth: int = 0,
    ) -> str | None:
        """Traverse the schema graph and assign names to anonymous schemas.

        Returns the assigned/resolved name for this schema.
        """
        if not schema_id or is_primitive_schema_id(schema_id):
            return None

        # Cycle detection
        if schema_id in ctx.visited:
            return anon_name_overrides.get(schema_id) or resolve_type_name(schema_id, get_schema(schema_id))
        ctx.visited.add(schema_id)

        schema = get_schema(schema_id)
        if not schema or is_primitive_schema(schema):
            return None

        # Name this schema if anonymous
        is_enum = bool(schema.get("enum_values"))
        if should_name_schema(schema_id, schema, ctx):
            if adapter is not None:
                node = SchemaNode(
                    schema_id=schema_id,
                    schema=schema,
                    edge_kind=edge_kind,
                    depth=depth,
                )
                adapter_name = adapter.name_anonymous(node, ctx)
                if adapter_name is not None:
                    reserve_type_name(schema_id, adapter_name)
                else:
                    name = build_name_from_context(ctx, is_enum)
                    reserve_type_name(schema_id, name)
            else:
                name = build_name_from_context(ctx, is_enum)
                reserve_type_name(schema_id, name)

        # Get the name we have for this schema (for propagating as parent context)
        my_name = anon_name_overrides.get(schema_id) or resolve_type_name(schema_id, schema)
        if my_name:
            used_type_names.add(my_name)

        # Extract all edges uniformly
        edges = extract_all_edges(schema, get_schema)

        # Recurse into all edges.
        # reset_suffix=True on property/composition edges prevents an "Item"
        # suffix accumulated while naming an array-item schema from leaking
        # into the names of that schema's own property children.
        for edge in edges:
            if edge.edge_kind == "array_items":
                child_ctx = ctx.child_context(
                    new_parent=my_name,
                    new_property=edge.property_name,
                    add_suffix="Item",
                    reset_suffix=True,  # Each array level gets exactly one "Item"
                )
            elif edge.edge_kind == "composition_member":
                child_ctx = ctx.child_context(
                    new_parent=my_name,
                    new_property=ctx.property_name,
                    reset_suffix=True,
                )
            else:
                child_ctx = ctx.child_context(
                    new_parent=my_name,
                    new_property=edge.property_name,
                    reset_suffix=True,  # Properties don't inherit array suffixes
                )

            traverse_and_name(edge.target_id, child_ctx, edge_kind=edge.edge_kind, depth=depth + 1)

        return my_name

    # -------------------------------------------------------------------------
    # Phase 2: Type Collection
    # -------------------------------------------------------------------------

    def collect_composition_properties(schema: dict) -> list[dict]:
        """Collect properties from allOf/oneOf/anyOf composition members."""
        composition = schema.get("composition")
        if not composition:
            return []

        members = composition.get("members", [])
        all_props: list[dict] = []
        seen_names: set[str] = set()

        def collect_from_member(member: dict) -> None:
            nonlocal all_props, seen_names

            # If member is an array, descend into items schema
            if member.get("kind") == "array":
                items_id = member.get("items_schema_id")
                if items_id:
                    items_schema = get_schema(items_id)
                    if items_schema:
                        collect_from_member(items_schema)
                return

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

        for member_id in members:
            member = get_schema(member_id)
            if not member:
                continue
            collect_from_member(member)

        return all_props

    def process_schema(
        schema_id: str,
        source: str | None = None,
        edge_kind: str | None = None,
        depth: int = 0,
    ) -> str | None:
        """Process a schema, collecting it and its dependencies.

        Returns the resolved type name, or None for primitives.
        """
        if is_primitive_schema_id(schema_id):
            return None

        if source:
            mark_source(schema_id, source)

        schema = get_schema(schema_id)
        if not schema:
            return None

        if is_primitive_schema(schema):
            return None

        kind = schema.get("kind", "object")

        # Handle arrays — they return item type with []
        if kind == "array":
            items_id = schema.get("items_schema_id")
            if items_id:
                item_type = process_schema(items_id, source=source, edge_kind="array_items", depth=depth + 1)
                if item_type:
                    return f"{item_type}[]"

                items_schema = get_schema(items_id)
                primitive_type = get_primitive_type_name(items_schema)
                if primitive_type:
                    return f"{primitive_type}[]"

                if is_shapeless_schema(items_schema, schemas_by_id):
                    return "JsonElement[]"

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

        # Collect properties: direct + from composition
        properties = list(schema.get("properties", []))
        composition_props = collect_composition_properties(schema)

        # Merge composition properties (avoid duplicates)
        seen_names = {p.get("json_name") for p in properties}
        for prop in composition_props:
            if prop.get("json_name") not in seen_names:
                properties.append(prop)
                seen_names.add(prop.get("json_name"))

        # Process composition members
        composition = schema.get("composition")
        if composition:
            for member_id in composition.get("members", []):
                process_schema(member_id, source="composition", edge_kind="composition_member", depth=depth + 1)

        if not properties and not composition:
            return None

        if not type_name:
            return None

        # Adapter hook: let the adapter override how this node is handled.
        # INLINE   → skip this type entirely (don't collect, don't follow children)
        # COLLAPSE → process children but don't emit a type entry
        # None / NAMED_CLASS → normal collection behaviour
        add_to_collected = True
        if adapter is not None:
            node = SchemaNode(
                schema_id=schema_id,
                schema=schema,
                edge_kind=edge_kind,
                depth=depth,
            )
            tree_ctx = TreeContext(
                parent=None,
                edge_kind=edge_kind,
                depth=depth,
                root_schema_id=root_id,
            )
            classification = adapter.classify_node(node, tree_ctx)
            if classification == NodeClassification.INLINE:
                return None
            if classification == NodeClassification.COLLAPSE:
                add_to_collected = False

        # Collect this type
        if type_name not in collected:
            processed_props = []
            for prop in properties:
                prop_schema_id = prop.get("schema_id", "")
                items_schema_id = prop.get("items_schema_id")

                prop_type_name = None
                if prop_schema_id:
                    prop_type_name = process_schema(prop_schema_id, source="property", edge_kind="property", depth=depth + 1)

                if items_schema_id and not prop_type_name:
                    item_type = process_schema(items_schema_id, source="property", edge_kind="array_items", depth=depth + 1)
                    if item_type:
                        prop_type_name = f"{item_type}[]"

                processed_props.append({
                    **prop,
                    "resolved_type": prop_type_name,
                })

            if add_to_collected:
                entry = _build_type_entry(schema_id, type_name, schema, processed_props)
                sources = sources_by_id.get(schema_id)
                if sources:
                    entry["sources"] = sorted(sources)
                collected[type_name] = entry

        # Handle additionalProperties
        addl_props_id = schema.get("additional_properties_schema_id")
        if addl_props_id:
            process_schema(addl_props_id, source="additionalProperties", edge_kind="additional_properties", depth=depth + 1)

        return type_name

    # -------------------------------------------------------------------------
    # Execute Both Phases
    # -------------------------------------------------------------------------

    # Phase 1: Assign names to all anonymous schemas
    root_name = resolve_type_name(root_id, root_schema)

    # Pre-seed the root's anonymous name so phase 1 doesn't rename it.
    # Without this, traverse_and_name sees initial_ctx.parent_name == root_name
    # and build_name_from_context appends "Nested", producing
    # "Anonymous_<hash>Nested" instead of the correct "Anonymous_<hash>".
    if root_name and "anon/" in root_id and not root_schema.get("name_hint"):
        anon_name_overrides[root_id] = root_name
        used_type_names.add(root_name)

    initial_ctx = NamingContext(
        parent_name=root_name,
        property_name=None,
        suffix_stack=[],
        visited=set(),
    )
    traverse_and_name(root_id, initial_ctx)

    # Phase 2: Collect type definitions
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
    root_schema: dict[str, Any],
    schemas_by_id: dict[str, dict[str, Any]],
    load_schema_detail: Callable[[str], dict[str, Any] | None] | None = None,
    adapter: ApiAdapter | None = None,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Build root type info and list of all nested types.

    This is a convenience function that separates the root type from
    its dependencies for prompt building.

    Args:
        root_schema: The root schema dict (must have an "id" key).
        schemas_by_id: Dict mapping schema IDs to schema data.
        load_schema_detail: Optional callable for lazy-loading full schema
            details by ID.
        adapter: Optional API-specific adapter. Hooks are called at naming
            and classification decision points.

    Returns:
        Tuple of (root_type_info, nested_types_list) where root_type_info is
        the processed root type dict and nested_types_list is all other types
        sorted alphabetically by name.
    """
    all_types = collect_type_closure(root_schema, schemas_by_id, load_schema_detail, adapter)

    root_id = root_schema.get("id", "")
    root_name = resolve_type_name(root_id, root_schema)

    root_type = all_types.pop(root_name, None)
    if root_type is None:
        root_type = _build_type_entry(root_id, root_name or "Root", root_schema)

    # Sort nested types alphabetically for consistent output
    nested_types = sorted(all_types.values(), key=lambda t: t["name"])

    return root_type, nested_types
