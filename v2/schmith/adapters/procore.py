"""Procore API adapter for Schmith v2.

Handles Procore-specific patterns in the OpenAPI spec that would otherwise
cause LLM confusion or generate incorrect code.

Usage in config.yaml:
    api:
      adapter: schmith.adapters.procore.ProcoreAdapter
"""

from __future__ import annotations

from typing import Any

from schmith.adapters.base import ApiAdapter


class ProcoreAdapter(ApiAdapter):
    """Adapter for the Procore OpenAPI specification.

    Procore's spec encodes many response objects as allOf compositions of
    "Normal" and "Extended" named schemas.  For example, ``GET /rest/v1.1/projects``
    returns objects whose type is described as:

        allOf:
          - $ref: '#/components/schemas/ProjectNormal'   # ~47 core fields
          - $ref: '#/components/schemas/ProjectExtended' # ~59 fields (superset)

    The type tree resolver surfaces these allOf members as separate nested types
    named "Normal" and "Extended".  Keeping them causes two problems:

    1. The LLM sees a nested type called "Normal" in the same prompt as the root
       type "Project" and anchors on that name, generating ``public class Normal``
       instead of ``public class Project``.

    2. Fields that belong only to "Extended" are never generated because the LLM
       skips the standalone "Extended" type or generates it with the wrong name.

    This adapter's ``transform_tree`` hook removes those composition-segment types
    and merges any fields they contribute (fields not already on the root) directly
    into the root type.  Real named nested types (ProjectCompany, ProjectType, etc.)
    are left untouched.
    """

    # allOf segment names used by Procore to split object schemas into variants.
    # These carry no semantic meaning as standalone C# classes.
    _COMPOSITION_NAMES: frozenset[str] = frozenset({"Normal", "Extended"})

    # Resolved type names that are not meaningful named object types and should
    # never be promoted to root when unwrapping a data envelope.
    _PRIMITIVE_RESOLVED: frozenset[str] = frozenset(
        {"object", "string", "int", "bool", "double", "JsonElement"}
    )

    def _unwrap_data_envelope(
        self,
        root_type: dict[str, Any],
        nested_types: list[dict[str, Any]],
    ) -> tuple[dict[str, Any], list[dict[str, Any]]]:
        """Promote the item type of a ``{ data: [Item] }`` envelope to root.

        Many Procore list endpoints return a single-key wrapper object::

            { "data": [ { "id": ..., "name": ..., ... } ] }

        The type tree treats the wrapper as the root type, leaving the actual
        payload type as an anonymous nested type named ``Anonymous_*DataNestedItem``.
        This produces a useless envelope class and ugly anonymous class names.

        This method detects that pattern and promotes the item type: the nested
        type is renamed to the envelope's (endpoint-derived) name and returned
        as the new root; the envelope is discarded entirely.

        Match criteria (all must hold):
        - Root is an inline schema (``is_inline=True``).
        - Root has exactly one property, and that property is named ``"data"``.
        - The property's ``resolved_type`` ends with ``"[]"`` (is an array).
        - Stripping ``"[]"`` yields a named type found in ``nested_types``
          (primitive array types like ``object[]`` or ``string[]`` are skipped).
        """
        if not root_type.get("is_inline"):
            return root_type, nested_types

        props: list[dict[str, Any]] = root_type.get("properties") or []
        if len(props) != 1 or props[0].get("json_name") != "data":
            return root_type, nested_types

        resolved: str = props[0].get("resolved_type") or ""
        if not resolved.endswith("[]"):
            return root_type, nested_types

        item_name = resolved[:-2]
        if not item_name or item_name in self._PRIMITIVE_RESOLVED:
            return root_type, nested_types

        item_idx = next(
            (i for i, nt in enumerate(nested_types) if nt.get("name") == item_name),
            None,
        )
        if item_idx is None:
            return root_type, nested_types

        # Promote: rename the item type to the root's endpoint-derived name.
        new_root: dict[str, Any] = {
            **nested_types[item_idx],
            "name": root_type["name"],
            "is_inline": False,
        }
        remaining = [nt for i, nt in enumerate(nested_types) if i != item_idx]
        return new_root, remaining

    def transform_tree(
        self,
        root_type: dict[str, Any],
        nested_types: list[dict[str, Any]],
    ) -> tuple[dict[str, Any], list[dict[str, Any]]]:
        """Transform the Procore type tree.

        Two transforms are applied in order:

        1. **Data envelope unwrap** — promotes the item type of a
           ``{ data: [Item] }`` response wrapper to root, discarding the
           envelope.  Fixes anonymous ``Anonymous_*DataNestedItem`` class names
           and removes the structural wrapper from the generated DataObject.

        2. **Composition segment merge** — finds nested types whose names are
           in ``_COMPOSITION_NAMES`` (``Normal``, ``Extended``), merges any
           properties they contribute that are not already on the root, then
           removes them from the nested types list.

        Fields are deduplicated by ``json_name``; the first occurrence wins:
        root fields take priority, then segment fields in alphabetical name
        order (so ``Extended`` fields come before ``Normal`` fields when
        deduping, as ``"Extended" < "Normal"`` alphabetically).
        """
        # Transform 1: unwrap { data: [Item] } envelope responses.
        root_type, nested_types = self._unwrap_data_envelope(root_type, nested_types)

        # Transform 2: merge allOf composition segments (Normal / Extended).
        segments: list[dict[str, Any]] = []
        keepers: list[dict[str, Any]] = []
        for nt in nested_types:
            if nt.get("name") in self._COMPOSITION_NAMES:
                segments.append(nt)
            else:
                keepers.append(nt)

        if not segments:
            return root_type, nested_types

        # Build the set of json_names already present on the root type.
        seen: set[str] = {
            p["json_name"]
            for p in (root_type.get("properties") or [])
            if p.get("json_name")
        }

        # Collect extra properties from segments not already covered by root.
        # Process segments in sorted name order so "Extended" follows "Normal".
        extra: list[dict[str, Any]] = []
        for segment in sorted(segments, key=lambda t: t.get("name") or ""):
            for prop in segment.get("properties") or []:
                jn = prop.get("json_name")
                if jn and jn not in seen:
                    extra.append(prop)
                    seen.add(jn)

        if extra:
            merged_root: dict[str, Any] = {
                **root_type,
                "properties": list(root_type.get("properties") or []) + extra,
            }
        else:
            merged_root = root_type

        return merged_root, keepers
