"""Centralized schema filtering for DataObject generation.

This module loads filters.toml and provides a unified interface for determining
which schemas should be included in generation. All codegen commands use this
module to ensure consistent filtering.

Usage:
    from codegen.filters import get_filters, SchemaFilters

    filters = get_filters()
    for schema in schemas:
        if filters.should_include(schema):
            # Process schema
"""

import re
import tomllib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .schema.filter import is_error_schema, is_primitive_schema, is_variant_schema
from .schema.type_mapping import extract_clean_name


@dataclass
class CategorySettings:
    """Category-level inclusion settings."""

    include_errors: bool = False
    include_anonymous: bool = False
    include_variants: bool = False
    include_primitives: bool = False


@dataclass
class PatternSettings:
    """Regex pattern settings for filtering."""

    exclude: list[str] = field(default_factory=list)
    include: list[str] = field(default_factory=list)

    # Compiled patterns (populated on first use)
    _exclude_compiled: list[re.Pattern] | None = field(default=None, repr=False)
    _include_compiled: list[re.Pattern] | None = field(default=None, repr=False)

    @property
    def exclude_patterns(self) -> list[re.Pattern]:
        """Get compiled exclude patterns."""
        if self._exclude_compiled is None:
            self._exclude_compiled = [re.compile(p) for p in self.exclude]
        return self._exclude_compiled

    @property
    def include_patterns(self) -> list[re.Pattern]:
        """Get compiled include patterns."""
        if self._include_compiled is None:
            self._include_compiled = [re.compile(p) for p in self.include]
        return self._include_compiled


@dataclass
class ExplicitSettings:
    """Explicit name lists for filtering."""

    exclude: list[str] = field(default_factory=list)
    include: list[str] = field(default_factory=list)


@dataclass
class SchemaFilters:
    """Centralized schema filtering configuration.

    Filters are applied in the following order (first match wins):
    1. Explicit include list - always included
    2. Explicit exclude list - always excluded
    3. Pattern include list - included (overrides category and pattern exclude)
    4. Pattern exclude list - excluded
    5. Category checks (anonymous, primitive, error, variant)
    6. Default: included
    """

    categories: CategorySettings = field(default_factory=CategorySettings)
    patterns: PatternSettings = field(default_factory=PatternSettings)
    explicit: ExplicitSettings = field(default_factory=ExplicitSettings)

    @classmethod
    def load(cls, config_path: Path | None = None) -> "SchemaFilters":
        """Load filters from TOML file.

        Args:
            config_path: Path to filters.toml. Defaults to codegen/filters.toml.

        Returns:
            Loaded SchemaFilters instance
        """
        if config_path is None:
            config_path = Path(__file__).parent / "filters.toml"

        if not config_path.exists():
            return cls()

        with open(config_path, "rb") as f:
            data = tomllib.load(f)

        return cls(
            categories=_load_categories(data.get("categories", {})),
            patterns=_load_patterns(data.get("patterns", {})),
            explicit=_load_explicit(data.get("explicit", {})),
        )

    def should_include(self, schema: dict) -> bool:
        """Determine if a schema should be included in generation.

        Args:
            schema: Schema dictionary from IR

        Returns:
            True if schema should be included, False if filtered out
        """
        schema_id = schema.get("schema_id", "")
        name_hint = schema.get("name_hint", "")
        clean_name = extract_clean_name(schema_id, name_hint)

        # 1. Explicit include - always wins
        if clean_name in self.explicit.include:
            return True

        # 2. Explicit exclude - always excluded
        if clean_name in self.explicit.exclude:
            return False

        # 3. Pattern include - overrides other filters
        for pattern in self.patterns.include_patterns:
            if pattern.match(clean_name):
                return True

        # 4. Pattern exclude
        for pattern in self.patterns.exclude_patterns:
            if pattern.match(clean_name):
                return False

        # 5. Category checks

        # Anonymous schemas (anon/ in ID or is_inline)
        is_anon = "anon/" in schema_id or schema.get("is_inline", False) or not name_hint
        if is_anon and not self.categories.include_anonymous:
            return False

        # Primitive types
        if is_primitive_schema(schema) and not self.categories.include_primitives:
            return False

        # Non-object schemas (must be object kind to be a DataObject)
        kind = schema.get("kind", "")
        if kind != "object":
            return False

        # Error schemas
        if is_error_schema(schema) and not self.categories.include_errors:
            return False

        # Variant schemas (Body/View)
        if is_variant_schema(clean_name) and not self.categories.include_variants:
            return False

        # 6. Default: include
        return True

    def get_exclusion_reason(self, schema: dict) -> str | None:
        """Get the reason a schema would be excluded.

        Args:
            schema: Schema dictionary from IR

        Returns:
            Reason string if excluded, None if included
        """
        schema_id = schema.get("schema_id", "")
        name_hint = schema.get("name_hint", "")
        clean_name = extract_clean_name(schema_id, name_hint)

        # Check in same order as should_include
        if clean_name in self.explicit.include:
            return None

        if clean_name in self.explicit.exclude:
            return "explicit_exclude"

        for pattern in self.patterns.include_patterns:
            if pattern.match(clean_name):
                return None

        for pattern in self.patterns.exclude_patterns:
            if pattern.match(clean_name):
                return "pattern_exclude"

        is_anon = "anon/" in schema_id or schema.get("is_inline", False) or not name_hint
        if is_anon and not self.categories.include_anonymous:
            return "anonymous"

        if is_primitive_schema(schema) and not self.categories.include_primitives:
            return "primitive"

        kind = schema.get("kind", "")
        if kind != "object":
            return "non_object"

        if is_error_schema(schema) and not self.categories.include_errors:
            return "error"

        if is_variant_schema(clean_name) and not self.categories.include_variants:
            return "variant"

        return None

    def filter_schemas(self, schemas: list[dict]) -> list[dict]:
        """Filter a list of schemas.

        Args:
            schemas: List of schema dictionaries from IR

        Returns:
            Filtered list containing only schemas that should be included
        """
        return [s for s in schemas if self.should_include(s)]

    def categorize_schemas(self, schemas: list[dict]) -> dict[str, list[dict]]:
        """Categorize schemas by inclusion/exclusion reason.

        Args:
            schemas: List of schema dictionaries from IR

        Returns:
            Dict mapping category names to lists of schemas
        """
        categories: dict[str, list[dict]] = {
            "generated": [],
            "anonymous": [],
            "primitive": [],
            "non_object": [],
            "error": [],
            "variant": [],
            "pattern_exclude": [],
            "explicit_exclude": [],
        }

        for schema in schemas:
            reason = self.get_exclusion_reason(schema)
            if reason is None:
                categories["generated"].append(schema)
            elif reason in categories:
                categories[reason].append(schema)
            else:
                # Unknown reason, treat as excluded
                categories.setdefault("other", []).append(schema)

        return categories


def _load_categories(data: dict[str, Any]) -> CategorySettings:
    """Load category settings from dict."""
    return CategorySettings(
        include_errors=data.get("include_errors", False),
        include_anonymous=data.get("include_anonymous", False),
        include_variants=data.get("include_variants", False),
        include_primitives=data.get("include_primitives", False),
    )


def _load_patterns(data: dict[str, Any]) -> PatternSettings:
    """Load pattern settings from dict."""
    return PatternSettings(
        exclude=data.get("exclude", []),
        include=data.get("include", []),
    )


def _load_explicit(data: dict[str, Any]) -> ExplicitSettings:
    """Load explicit settings from dict."""
    return ExplicitSettings(
        exclude=data.get("exclude", []),
        include=data.get("include", []),
    )


# Module-level singleton
_filters: SchemaFilters | None = None


def get_filters(config_path: Path | None = None) -> SchemaFilters:
    """Get the global SchemaFilters instance.

    Args:
        config_path: Optional path to filters.toml

    Returns:
        SchemaFilters singleton instance
    """
    global _filters
    if _filters is None:
        _filters = SchemaFilters.load(config_path)
    return _filters


def reload_filters(config_path: Path | None = None) -> SchemaFilters:
    """Reload filters from disk.

    Args:
        config_path: Optional path to filters.toml

    Returns:
        Reloaded SchemaFilters instance
    """
    global _filters
    _filters = SchemaFilters.load(config_path)
    return _filters
