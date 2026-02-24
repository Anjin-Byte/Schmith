"""LLM provider implementations for code generation.

This module provides a unified interface for interacting with different
LLM providers (Anthropic Claude, OpenAI GPT) for code generation tasks.

API keys are read at call time from the config dict or from environment
variables. No automatic .env loading occurs — users set keys in their shell
or source a .env file themselves.
"""

from __future__ import annotations

import os
import sys
from typing import Protocol


class LLMProvider(Protocol):
    """Protocol for LLM providers."""

    def generate(self, prompt: str, system: str | None = None) -> str:
        """Generate a response from the LLM."""
        ...


class AnthropicProvider:
    """Anthropic Claude provider."""

    DEFAULT_MODEL = "claude-3-5-haiku-20241022"

    def __init__(self, api_key: str | None = None, model: str | None = None):
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self.model = model or self.DEFAULT_MODEL
        self._client = None

        if not self.api_key:
            raise ValueError(
                "Anthropic API key required. Set ANTHROPIC_API_KEY environment "
                "variable or pass api_key in the llm config."
            )

    @property
    def client(self):
        if self._client is None:
            try:
                import anthropic
                self._client = anthropic.Anthropic(api_key=self.api_key)
            except ImportError:
                print("Error: anthropic package not installed.", file=sys.stderr)
                print("Install with: pip install 'schmith[anthropic]'", file=sys.stderr)
                sys.exit(1)
        return self._client

    def generate(self, prompt: str, system: str | None = None) -> str:
        message = self.client.messages.create(
            model=self.model,
            max_tokens=4096,
            system=system or "You are a C# code generator specializing in Trimble XChange DataObjects.",
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text


class OpenAIProvider:
    """OpenAI GPT provider."""

    DEFAULT_MODEL = "gpt-5-mini-2025-08-07"

    def __init__(self, api_key: str | None = None, model: str | None = None):
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        self.model = model or self.DEFAULT_MODEL
        self._client = None

        if not self.api_key:
            raise ValueError(
                "OpenAI API key required. Set OPENAI_API_KEY environment "
                "variable or pass api_key in the llm config."
            )

    @property
    def client(self):
        if self._client is None:
            try:
                import openai
                self._client = openai.OpenAI(api_key=self.api_key)
            except ImportError:
                print("Error: openai package not installed.", file=sys.stderr)
                print("Install with: pip install 'schmith[openai]'", file=sys.stderr)
                sys.exit(1)
        return self._client

    def generate(self, prompt: str, system: str | None = None) -> str:
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_completion_tokens=4096,
        )
        return response.choices[0].message.content


class DryRunProvider:
    """Dry-run provider that doesn't call any API."""

    def generate(self, prompt: str, system: str | None = None) -> str:
        return "// Dry run - no code generated"


def get_provider(config: dict) -> LLMProvider:
    """Get an LLM provider from a config dict.

    Accepts either a top-level config dict (with an "llm" block) or
    a direct llm config dict. Reads provider name, model, and api_key
    from the resolved llm config.
    Falls back to ANTHROPIC_API_KEY / OPENAI_API_KEY environment variables
    for api_key if not present in config.

    If dry_run is True (either at top level or in the llm dict), returns
    a DryRunProvider regardless of other settings.

    Args:
        config: Top-level config dict (from config.yaml).

    Returns:
        An LLMProvider instance.

    Raises:
        ValueError: If the provider name is unknown or a required key is missing.
    """
    llm_cfg: dict
    if isinstance(config.get("llm"), dict):
        llm_cfg = config.get("llm") or {}
        # Preserve legacy behavior where dry_run may be provided at top-level.
        if config.get("dry_run") and not llm_cfg.get("dry_run"):
            llm_cfg = {**llm_cfg, "dry_run": True}
    else:
        # Caller already passed the llm block directly.
        llm_cfg = config or {}

    if llm_cfg.get("dry_run"):
        return DryRunProvider()
    provider_name: str = llm_cfg.get("provider", "anthropic")
    model: str | None = llm_cfg.get("model") or None
    api_key: str | None = llm_cfg.get("api_key") or None

    if provider_name == "anthropic":
        return AnthropicProvider(api_key=api_key, model=model)
    elif provider_name == "openai":
        return OpenAIProvider(api_key=api_key, model=model)
    else:
        raise ValueError(
            f"Unknown LLM provider '{provider_name}'. "
            "Supported providers: anthropic, openai"
        )


def generate_code(prompt: str, system: str, provider: LLMProvider) -> str:
    """Call the LLM and return extracted C# code.

    Args:
        prompt: The user-facing prompt (schema + field information).
        system: The system prompt (code generation instructions).
        provider: Configured LLM provider.

    Returns:
        Extracted C# code string (markdown fences stripped).
    """
    response = provider.generate(prompt, system=system)
    return extract_code_from_response(response)


def extract_code_from_response(response: str) -> str:
    """Extract C# code from LLM response, handling markdown code blocks."""
    if "```csharp" in response:
        start = response.find("```csharp") + len("```csharp")
        end = response.find("```", start)
        if end > start:
            return response[start:end].strip()

    if "```cs" in response:
        start = response.find("```cs") + len("```cs")
        end = response.find("```", start)
        if end > start:
            return response[start:end].strip()

    if "```" in response:
        start = response.find("```") + 3
        # Skip language identifier if present
        newline = response.find("\n", start)
        if newline > start and newline - start < 20:
            start = newline + 1
        end = response.find("```", start)
        if end > start:
            return response[start:end].strip()

    return response.strip()
