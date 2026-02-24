"""Semantic naming strategies for DataObject generation.

This module provides configurable naming strategies that extract meaningful,
concise names from API paths instead of concatenating all path segments.

The naming system is designed to be:
- Configurable: Different strategies can be selected via config
- Backward compatible: The 'verbose' strategy produces original behavior
- Extensible: New strategies can be added without changing existing code

Example:
    Path: DELETE /rest/v1.0/bim/model/revision/viewpoints/bulk-delete

    Verbose (original): DeleteRestV10BimModelRevisionViewpointsBulkDeleteResponse200
    Semantic:           DeleteViewpointsBulkResponse200
    Resource-focused:   ViewpointsBulkDeleteResponse200
"""

from __future__ import annotations

import re
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass
class NamingConfig:
    """Configuration for naming strategy behavior.

    Attributes:
        strategy: Name of the strategy to use ('verbose', 'semantic', 'resource')
        strip_version_prefixes: Remove version segments like 'rest', 'v1.0', 'v2.0'
        max_segments: Maximum path segments to include (0 = unlimited)
        preserve_method: Include HTTP method in the name
        resource_depth: How many trailing resource segments to keep (for 'resource' strategy)
        abbreviations: Dict of long terms to abbreviate (e.g., {"Response": "Resp"})
        ignore_operation_id: If True, always derive names from path, ignoring operationId
    """
    strategy: str = "verbose"
    strip_version_prefixes: bool = True
    max_segments: int = 0
    preserve_method: bool = True
    resource_depth: int = 2
    abbreviations: dict[str, str] = field(default_factory=dict)
    ignore_operation_id: bool = False


# Common version-like path segments to strip
VERSION_PATTERNS: list[re.Pattern[str]] = [
    re.compile(r"^rest$", re.IGNORECASE),
    re.compile(r"^api$", re.IGNORECASE),
    re.compile(r"^v\d+(\.\d+)?$", re.IGNORECASE),  # v1, v1.0, v2.0
    re.compile(r"^vapid$", re.IGNORECASE),         # Procore-specific
]

# Path parameter pattern (segments like {id}, {company_id})
PARAM_PATTERN = re.compile(r"^\{[^}]+\}$")


def _pascal_case(value: str) -> str:
    """Convert a string to PascalCase.

    Args:
        value: Input string with any separator (spaces, dashes, underscores)

    Returns:
        PascalCase string

    Example:
        >>> _pascal_case("bulk-delete")
        'BulkDelete'
        >>> _pascal_case("company_id")
        'CompanyId'
    """
    parts = re.split(r"[^A-Za-z0-9]+", value)
    return "".join(p[:1].upper() + p[1:] for p in parts if p)


def _is_version_segment(segment: str) -> bool:
    """Check if a path segment is a version indicator.

    Args:
        segment: Path segment to check

    Returns:
        True if segment matches version patterns
    """
    return any(p.match(segment) for p in VERSION_PATTERNS)


def _is_param_segment(segment: str) -> bool:
    """Check if a path segment is a path parameter.

    Args:
        segment: Path segment to check (e.g., "{id}", "{company_id}")

    Returns:
        True if segment is a path parameter
    """
    return bool(PARAM_PATTERN.match(segment))


def _extract_path_segments(path_template: str) -> list[str]:
    """Extract non-empty segments from a path template.

    Args:
        path_template: URL path template (e.g., "/rest/v1.0/companies/{id}/projects")

    Returns:
        List of path segments without empty strings
    """
    return [seg for seg in path_template.split("/") if seg]


def _strip_param_braces(segment: str) -> str:
    """Remove braces from path parameter segments.

    Args:
        segment: Path segment, possibly with braces

    Returns:
        Segment without braces

    Example:
        >>> _strip_param_braces("{company_id}")
        'company_id'
    """
    return segment.strip("{}")


class NamingStrategy(ABC):
    """Abstract base class for naming strategies.

    Each strategy implements a different approach to generating
    DataObject names from API paths.
    """

    def __init__(self, config: NamingConfig):
        self.config = config

    @abstractmethod
    def generate_operation_name(
        self,
        operation: dict[str, Any],
        method: str,
        path_template: str,
        common_prefix: list[str] | None = None,
    ) -> str:
        """Generate an operation name from API path info.

        Args:
            operation: OpenAPI operation object (may contain operationId)
            method: HTTP method (GET, POST, DELETE, etc.)
            path_template: URL path template
            common_prefix: Common prefix segments to potentially remove

        Returns:
            Generated operation name in PascalCase
        """
        pass

    def generate_response_name(
        self,
        operation: dict[str, Any],
        method: str,
        path_template: str,
        status: str,
        common_prefix: list[str] | None = None,
    ) -> str:
        """Generate a response schema name.

        Args:
            operation: OpenAPI operation object
            method: HTTP method
            path_template: URL path template
            status: HTTP status code (e.g., "200", "404")
            common_prefix: Common prefix segments to potentially remove

        Returns:
            Generated response name (e.g., "GetUsersResponse200")
        """
        op_name = self.generate_operation_name(
            operation, method, path_template, common_prefix
        )
        return f"{op_name}Response{status}"

    def apply_abbreviations(self, name: str) -> str:
        """Apply configured abbreviations to a name.

        Args:
            name: Name to abbreviate

        Returns:
            Name with abbreviations applied
        """
        result = name
        for long_form, short_form in self.config.abbreviations.items():
            result = result.replace(long_form, short_form)
        return result


class VerboseNamingStrategy(NamingStrategy):
    """Original verbose naming strategy (backward compatible).

    This strategy produces the same names as the original implementation,
    concatenating all path segments with the HTTP method.

    Example:
        DELETE /rest/v1.0/bim/model/viewpoints/bulk-delete
        → DeleteRestV10BimModelViewpointsBulkDelete
    """

    def generate_operation_name(
        self,
        operation: dict[str, Any],
        method: str,
        path_template: str,
        common_prefix: list[str] | None = None,
    ) -> str:
        # Check for explicit operationId first (unless ignoring)
        if not self.config.ignore_operation_id:
            op_id = operation.get("operationId")
            if isinstance(op_id, str) and op_id.strip():
                return _pascal_case(op_id)

        # Fallback: Method + all path segments
        segments = [_strip_param_braces(seg) for seg in _extract_path_segments(path_template)]

        # Remove common prefix if provided
        if common_prefix:
            while segments[: len(common_prefix)] == common_prefix:
                segments = segments[len(common_prefix):]

        segments = [method.upper()] + segments
        return _pascal_case(" ".join(segments))


class SemanticNamingStrategy(NamingStrategy):
    """Semantic naming strategy that extracts meaningful resource names.

    This strategy:
    1. Uses operationId if available (unless ignore_operation_id is True)
    2. Strips version prefixes (rest, v1.0, api)
    3. Skips path parameters (keeps resource names only)
    4. Optionally limits segment count

    Example:
        DELETE /rest/v1.0/bim/model/viewpoints/bulk-delete
        → DeleteBimModelViewpointsBulkDelete (with version stripping)
        → DeleteViewpointsBulkDelete (with max_segments=2)
    """

    def generate_operation_name(
        self,
        operation: dict[str, Any],
        method: str,
        path_template: str,
        common_prefix: list[str] | None = None,
    ) -> str:
        # Check for explicit operationId first (unless ignoring)
        if not self.config.ignore_operation_id:
            op_id = operation.get("operationId")
            if isinstance(op_id, str) and op_id.strip():
                name = _pascal_case(op_id)
                return self.apply_abbreviations(name)

        segments = _extract_path_segments(path_template)

        # Filter segments based on config
        meaningful_segments: list[str] = []
        for seg in segments:
            # Skip version prefixes
            if self.config.strip_version_prefixes and _is_version_segment(seg):
                continue

            # Skip path parameters (but could optionally include them)
            if _is_param_segment(seg):
                continue

            meaningful_segments.append(_strip_param_braces(seg))

        # Remove common prefix if provided
        if common_prefix:
            prefix_set = set(common_prefix)
            meaningful_segments = [s for s in meaningful_segments if s not in prefix_set]

        # Limit segments if configured
        if self.config.max_segments > 0 and len(meaningful_segments) > self.config.max_segments:
            meaningful_segments = meaningful_segments[-self.config.max_segments:]

        # Build the name
        if self.config.preserve_method:
            parts = [method.upper()] + meaningful_segments
        else:
            parts = meaningful_segments

        name = _pascal_case(" ".join(parts))
        return self.apply_abbreviations(name)


class ResourceNamingStrategy(NamingStrategy):
    """Resource-focused naming strategy.

    This strategy focuses on the last N resource segments, ignoring
    most of the path hierarchy. Best for APIs with deep nesting.

    Example:
        DELETE /rest/v1.0/companies/{id}/projects/{pid}/tasks/{tid}
        → DeleteProjectsTasks (with resource_depth=2)
        → DeleteTasks (with resource_depth=1)
    """

    def generate_operation_name(
        self,
        operation: dict[str, Any],
        method: str,
        path_template: str,
        common_prefix: list[str] | None = None,
    ) -> str:
        # Check for explicit operationId first (unless ignoring)
        if not self.config.ignore_operation_id:
            op_id = operation.get("operationId")
            if isinstance(op_id, str) and op_id.strip():
                name = _pascal_case(op_id)
                return self.apply_abbreviations(name)

        segments = _extract_path_segments(path_template)

        # Extract only resource segments (non-params, non-versions)
        resource_segments: list[str] = []
        for seg in segments:
            if _is_version_segment(seg):
                continue
            if _is_param_segment(seg):
                continue
            resource_segments.append(seg)

        # Take only the last N segments based on resource_depth
        depth = self.config.resource_depth
        if depth > 0 and len(resource_segments) > depth:
            resource_segments = resource_segments[-depth:]

        # Build the name
        if self.config.preserve_method:
            parts = [method.upper()] + resource_segments
        else:
            parts = resource_segments

        name = _pascal_case(" ".join(parts))
        return self.apply_abbreviations(name)


# Strategy registry
STRATEGIES: dict[str, type[NamingStrategy]] = {
    "verbose": VerboseNamingStrategy,
    "semantic": SemanticNamingStrategy,
    "resource": ResourceNamingStrategy,
}


def get_naming_strategy(config: NamingConfig) -> NamingStrategy:
    """Get a naming strategy instance based on configuration.

    Args:
        config: Naming configuration

    Returns:
        Configured naming strategy instance

    Raises:
        ValueError: If strategy name is not recognized
    """
    strategy_cls = STRATEGIES.get(config.strategy)
    if strategy_cls is None:
        valid = ", ".join(STRATEGIES.keys())
        raise ValueError(f"Unknown naming strategy '{config.strategy}'. Valid: {valid}")
    return strategy_cls(config)


def create_config_from_dict(config_dict: dict[str, Any]) -> NamingConfig:
    """Create a NamingConfig from a dictionary (e.g., from TOML).

    Args:
        config_dict: Dictionary with naming configuration

    Returns:
        NamingConfig instance

    Example:
        >>> config = create_config_from_dict({
        ...     "strategy": "semantic",
        ...     "strip_version_prefixes": True,
        ...     "max_segments": 3,
        ... })
    """
    return NamingConfig(
        strategy=config_dict.get("strategy", "verbose"),
        strip_version_prefixes=config_dict.get("strip_version_prefixes", True),
        max_segments=config_dict.get("max_segments", 0),
        preserve_method=config_dict.get("preserve_method", True),
        resource_depth=config_dict.get("resource_depth", 2),
        abbreviations=config_dict.get("abbreviations", {}),
        ignore_operation_id=config_dict.get("ignore_operation_id", False),
    )


# Convenience functions for direct use


def generate_operation_name(
    operation: dict[str, Any],
    method: str,
    path_template: str,
    common_prefix: list[str] | None = None,
    config: NamingConfig | None = None,
) -> str:
    """Generate an operation name using the configured strategy.

    This is a convenience function that creates a strategy and generates
    a name in one call.

    Args:
        operation: OpenAPI operation object
        method: HTTP method
        path_template: URL path template
        common_prefix: Common prefix segments
        config: Naming configuration (uses default verbose if None)

    Returns:
        Generated operation name
    """
    if config is None:
        config = NamingConfig()
    strategy = get_naming_strategy(config)
    return strategy.generate_operation_name(operation, method, path_template, common_prefix)


def generate_response_name(
    operation: dict[str, Any],
    method: str,
    path_template: str,
    status: str,
    common_prefix: list[str] | None = None,
    config: NamingConfig | None = None,
) -> str:
    """Generate a response schema name using the configured strategy.

    Args:
        operation: OpenAPI operation object
        method: HTTP method
        path_template: URL path template
        status: HTTP status code
        common_prefix: Common prefix segments
        config: Naming configuration (uses default verbose if None)

    Returns:
        Generated response name (e.g., "GetUsersResponse200")
    """
    if config is None:
        config = NamingConfig()
    strategy = get_naming_strategy(config)
    return strategy.generate_response_name(
        operation, method, path_template, status, common_prefix
    )
