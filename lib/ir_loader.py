#!/usr/bin/env python3
"""
IR Data Loading Utilities

Provides classes for loading and accessing IR data structures.
"""
import json
import os
from typing import Any, Dict, List, Optional


class IRDataLoader:
    """Utility class for loading IR data structures."""

    def __init__(self, root_dir: str, spec_name: str):
        """
        Initialize the data loader.

        Args:
            root_dir: Root directory of the project
            spec_name: Name of the API spec
        """
        self.root_dir = root_dir
        self.spec_name = spec_name
        self.ir_dir = os.path.join(root_dir, "ir", spec_name)

    def load_manifest(self) -> Dict[str, Any]:
        """Load the IR manifest file."""
        manifest_path = os.path.join(self.ir_dir, "manifest.json")
        if not os.path.exists(manifest_path):
            return {}
        with open(manifest_path, "r", encoding="utf-8") as handle:
            return json.load(handle)

    def load_operations(self) -> List[Dict[str, Any]]:
        """Load all operation JSON files from the operations directory."""
        ops_dir = os.path.join(self.ir_dir, "operations")
        operations: List[Dict[str, Any]] = []
        if not os.path.isdir(ops_dir):
            return operations
        for filename in os.listdir(ops_dir):
            if not filename.endswith(".json") or filename == "index.json":
                continue
            path = os.path.join(ops_dir, filename)
            with open(path, "r", encoding="utf-8") as handle:
                operations.append(json.load(handle))
        return operations

    def load_schemas(self) -> Dict[str, Dict[str, Any]]:
        """
        Load all schema JSON files from the schemas directory.

        Returns:
            Dictionary mapping schema_id to schema data
        """
        schema_dir = os.path.join(self.ir_dir, "schemas")
        schemas: Dict[str, Dict[str, Any]] = {}
        if not os.path.isdir(schema_dir):
            return schemas
        for filename in os.listdir(schema_dir):
            if not filename.endswith(".json") or filename == "index.json":
                continue
            path = os.path.join(schema_dir, filename)
            with open(path, "r", encoding="utf-8") as handle:
                schema = json.load(handle)
            schema_id = schema.get("id")
            if schema_id:
                schemas[schema_id] = schema
        return schemas

    def load_schema_index(self) -> Dict[str, Any]:
        """Load the schema index file."""
        index_path = os.path.join(self.ir_dir, "schemas", "index.json")
        if not os.path.exists(index_path):
            return {}
        with open(index_path, "r", encoding="utf-8") as handle:
            return json.load(handle)

    def load_serialization_media_types(self) -> Dict[str, Any]:
        """Load the serialization media_types.json file."""
        media_types_path = os.path.join(self.ir_dir, "serialization", "media_types.json")
        if not os.path.exists(media_types_path):
            return {}
        with open(media_types_path, "r", encoding="utf-8") as handle:
            return json.load(handle)

    def load_serialization_json_paths(self) -> Dict[str, Any]:
        """Load the serialization json_paths.json file."""
        json_paths_path = os.path.join(self.ir_dir, "serialization", "json_paths.json")
        if not os.path.exists(json_paths_path):
            return {}
        with open(json_paths_path, "r", encoding="utf-8") as handle:
            return json.load(handle)

    def load_reference_edges(self) -> Optional[Dict[str, Any]]:
        """Load the reference edges file if it exists."""
        edges_path = os.path.join(self.ir_dir, "refs", "edges.json")
        if not os.path.exists(edges_path):
            return None
        with open(edges_path, "r", encoding="utf-8") as handle:
            return json.load(handle)
