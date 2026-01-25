"""IR (Intermediate Representation) loading and querying utilities.

This module provides a clean interface for loading and querying IR data,
including schemas, operations, and reference graphs.
"""

import json
from pathlib import Path
from typing import Any, Iterator


class IRLoader:
    """Load and query IR data for an API specification.

    Example:
        loader = IRLoader("servicefusion")
        for schema in loader.schemas():
            print(schema["name_hint"])
    """

    def __init__(self, ir_name: str, ir_base: Path | None = None):
        """Initialize the IR loader.

        Args:
            ir_name: Name of the IR directory (e.g., "servicefusion")
            ir_base: Base path containing IR directories. Defaults to ./ir
        """
        self.ir_name = ir_name
        self.ir_base = ir_base or Path(__file__).parent.parent / "ir"
        self.ir_path = self.ir_base / ir_name

        if not self.ir_path.exists():
            available = self.list_available(self.ir_base)
            raise FileNotFoundError(
                f"IR directory not found: {self.ir_path}\n"
                f"Available: {', '.join(available) if available else '(none)'}"
            )

        self._manifest: dict | None = None
        self._schemas_index: list[dict] | None = None
        self._schemas_by_id: dict[str, dict] | None = None
        self._operations_index: list[dict] | None = None
        self._adjacency: dict | None = None

    @staticmethod
    def list_available(ir_base: Path | None = None) -> list[str]:
        """List available IR names in the base directory."""
        base = ir_base or Path(__file__).parent.parent / "ir"
        if not base.exists():
            return []
        return sorted(
            item.name
            for item in base.iterdir()
            if item.is_dir() and (item / "manifest.json").exists()
        )

    @property
    def manifest(self) -> dict:
        """Load and cache the manifest."""
        if self._manifest is None:
            self._manifest = self._load_json(self.ir_path / "manifest.json")
        return self._manifest

    @property
    def spec_name(self) -> str:
        """Get the spec name from manifest."""
        return self.manifest.get("spec_name", self.ir_name)

    @property
    def counts(self) -> dict[str, int]:
        """Get counts from manifest."""
        return self.manifest.get("counts", {})

    def schemas(self) -> list[dict]:
        """Get the schemas index (list of schema summaries)."""
        if self._schemas_index is None:
            data = self._load_json(self.ir_path / "schemas" / "index.json")
            self._schemas_index = data.get("schemas", [])
        return self._schemas_index

    def schemas_by_id(self) -> dict[str, dict]:
        """Get schemas indexed by schema_id for fast lookup."""
        if self._schemas_by_id is None:
            self._schemas_by_id = {s["schema_id"]: s for s in self.schemas()}
        return self._schemas_by_id

    def operations(self) -> list[dict]:
        """Get the operations index."""
        if self._operations_index is None:
            data = self._load_json(self.ir_path / "operations" / "index.json")
            self._operations_index = data.get("operations", [])
        return self._operations_index

    def adjacency(self) -> dict:
        """Get the reference adjacency graph."""
        if self._adjacency is None:
            path = self.ir_path / "refs" / "adjacency.json"
            self._adjacency = self._load_json(path) if path.exists() else {}
        return self._adjacency

    def load_schema_detail(self, schema_id: str) -> dict | None:
        """Load full schema details from individual file.

        Args:
            schema_id: The schema ID (e.g., "schema:types/typ.Customer")

        Returns:
            Full schema data or None if not found
        """
        filename = self._schema_id_to_filename(schema_id)
        path = self.ir_path / "schemas" / filename
        if path.exists():
            return self._load_json(path)
        return None

    def iter_schema_details(self) -> Iterator[dict]:
        """Iterate over all schema detail files.

        Yields:
            Full schema data for each schema
        """
        schemas_dir = self.ir_path / "schemas"
        for path in sorted(schemas_dir.glob("schema_*.json")):
            if path.name == "index.json":
                continue
            yield self._load_json(path)

    def _load_json(self, path: Path) -> dict:
        """Load JSON from a file."""
        with open(path, encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def _schema_id_to_filename(schema_id: str) -> str:
        """Convert a schema ID to its filename.

        Example:
            "schema:types/typ.Customer" -> "schema_types_typ_Customer.json"
            "schema:anon/abc123" -> "schema_anon_abc123.json"
        """
        return (
            schema_id.replace("schema:", "schema_")
            .replace("/", "_")
            .replace(".", "_")
            + ".json"
        )


def get_loader(ir_name: str) -> IRLoader:
    """Convenience function to get an IR loader.

    Args:
        ir_name: Name of the IR to load

    Returns:
        IRLoader instance

    Raises:
        FileNotFoundError: If IR directory doesn't exist
    """
    return IRLoader(ir_name)
