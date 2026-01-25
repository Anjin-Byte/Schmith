"""Configuration management for code generation.

This module loads configuration from config.toml and provides
a typed interface for accessing settings.
"""

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import tomllib
except ImportError:
    import tomli as tomllib  # type: ignore


@dataclass
class PathsConfig:
    """Path configuration settings."""

    ir_dir: str = "ir"
    packets_dir: str = "prompt_packets"
    generated_dir: str = "generated"

    def resolve(self, base: Path) -> "ResolvedPaths":
        """Resolve paths relative to a base directory."""
        return ResolvedPaths(
            ir_dir=base / self.ir_dir,
            packets_dir=base / self.packets_dir,
            generated_dir=base / self.generated_dir,
        )


@dataclass
class ResolvedPaths:
    """Resolved absolute paths."""

    ir_dir: Path
    packets_dir: Path
    generated_dir: Path

    def packets_for(self, ir_name: str, grouped: bool = False) -> Path:
        """Get packets directory for a specific IR.

        Structure: packets_dir/flat/<ir>/ or packets_dir/grouped/<ir>/
        """
        subdir = "grouped" if grouped else "flat"
        return self.packets_dir / subdir / ir_name

    def generated_for(self, ir_name: str) -> Path:
        """Get generated code directory for a specific IR."""
        return self.generated_dir / ir_name


@dataclass
class LLMConfig:
    """LLM provider configuration."""

    provider: str = "anthropic"
    model: str = ""
    max_tokens: int = 4096


@dataclass
class GenerationConfig:
    """Code generation settings."""

    include_errors: bool = False
    include_anonymous: bool = False
    grouped: bool = False


@dataclass
class PromptingConfig:
    """Prompt construction settings."""

    max_fields_per_page: int = 10


@dataclass
class FiltersConfig:
    """Schema filtering configuration."""

    exclude_patterns: list[str] = field(default_factory=lambda: [".*Body$", ".*View$"])
    include_patterns: list[str] = field(default_factory=list)

    def should_exclude(self, name: str) -> bool:
        """Check if a schema name should be excluded.

        Args:
            name: Schema name to check

        Returns:
            True if name matches exclude patterns and not include patterns
        """
        # Check include patterns first (they override excludes)
        for pattern in self.include_patterns:
            if re.match(pattern, name):
                return False

        # Check exclude patterns
        for pattern in self.exclude_patterns:
            if re.match(pattern, name):
                return True

        return False


@dataclass
class CodegenConfig:
    """Complete configuration for code generation."""

    paths: PathsConfig = field(default_factory=PathsConfig)
    llm: LLMConfig = field(default_factory=LLMConfig)
    generation: GenerationConfig = field(default_factory=GenerationConfig)
    prompting: PromptingConfig = field(default_factory=PromptingConfig)
    filters: FiltersConfig = field(default_factory=FiltersConfig)

    @classmethod
    def load(cls, config_path: Path | None = None) -> "CodegenConfig":
        """Load configuration from TOML file.

        Args:
            config_path: Path to config.toml. Defaults to codegen/config.toml.

        Returns:
            Loaded configuration
        """
        if config_path is None:
            config_path = Path(__file__).parent / "config.toml"

        if not config_path.exists():
            return cls()

        with open(config_path, "rb") as f:
            data = tomllib.load(f)

        return cls(
            paths=_load_paths(data.get("paths", {})),
            llm=_load_llm(data.get("llm", {})),
            generation=_load_generation(data.get("generation", {})),
            prompting=_load_prompting(data.get("prompting", {})),
            filters=_load_filters(data.get("filters", {})),
        )

    def resolve_paths(self, base: Path | None = None) -> ResolvedPaths:
        """Resolve paths relative to base directory.

        Args:
            base: Base directory. Defaults to project root.

        Returns:
            ResolvedPaths with absolute paths
        """
        if base is None:
            base = Path(__file__).parent.parent
        return self.paths.resolve(base)


def _load_paths(data: dict[str, Any]) -> PathsConfig:
    """Load paths configuration from dict."""
    return PathsConfig(
        ir_dir=data.get("ir_dir", "ir"),
        packets_dir=data.get("packets_dir", "prompt_packets"),
        generated_dir=data.get("generated_dir", "generated"),
    )


def _load_llm(data: dict[str, Any]) -> LLMConfig:
    """Load LLM configuration from dict."""
    return LLMConfig(
        provider=data.get("provider", "anthropic"),
        model=data.get("model", ""),
        max_tokens=data.get("max_tokens", 4096),
    )


def _load_generation(data: dict[str, Any]) -> GenerationConfig:
    """Load generation configuration from dict."""
    return GenerationConfig(
        include_errors=data.get("include_errors", False),
        include_anonymous=data.get("include_anonymous", False),
        grouped=data.get("grouped", False),
    )


def _load_prompting(data: dict[str, Any]) -> PromptingConfig:
    """Load prompt construction configuration from dict."""
    return PromptingConfig(
        max_fields_per_page=data.get("max_fields_per_page", 10),
    )


def _load_filters(data: dict[str, Any]) -> FiltersConfig:
    """Load filters configuration from dict."""
    return FiltersConfig(
        exclude_patterns=data.get("exclude_patterns", [".*Body$", ".*View$"]),
        include_patterns=data.get("include_patterns", []),
    )


# Global config instance (lazy loaded)
_config: CodegenConfig | None = None


def get_config(config_path: Path | None = None) -> CodegenConfig:
    """Get the global configuration instance.

    Args:
        config_path: Optional path to config file. Only used on first call.

    Returns:
        Global CodegenConfig instance
    """
    global _config
    if _config is None:
        _config = CodegenConfig.load(config_path)
    return _config


def reload_config(config_path: Path | None = None) -> CodegenConfig:
    """Reload configuration from file.

    Args:
        config_path: Optional path to config file.

    Returns:
        Reloaded CodegenConfig instance
    """
    global _config
    _config = CodegenConfig.load(config_path)
    return _config
