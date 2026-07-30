"""LLM provider implementations for code generation.

This module provides a unified interface for interacting with different
LLM providers (Anthropic Claude, OpenAI GPT) for code generation tasks.

API keys are read at call time from the config dict or from environment
variables. No automatic .env loading occurs — users set keys in their shell
or source a .env file themselves.

Stitching helpers (``stitch_type_pages`` and its internals) live in
``schmith.assembly`` so that assembly logic is co-located with
``assemble_from_pages``.
"""

from __future__ import annotations

import os
import sys
from typing import Any, NamedTuple, Protocol


class GenerationResult(NamedTuple):
    """Output from a single LLM generation call."""

    text: str
    input_tokens: int
    output_tokens: int


class LLMProvider(Protocol):
    """Protocol for LLM providers."""

    model: str
    """The model identifier used by this provider."""

    def generate(self, prompt: str, system: str | None = None) -> GenerationResult:
        """Generate a response from the LLM."""
        ...

    def count_tokens(self, prompt: str, system: str | None = None) -> int:
        """Count the tokens in a prompt without generating a response."""
        ...


class AnthropicProvider:
    """Anthropic Claude provider."""

    DEFAULT_MODEL = "claude-3-5-haiku-20241022"
    DEFAULT_MAX_OUTPUT_TOKENS = 32768

    def __init__(
        self,
        api_key: str | None = None,
        model: str | None = None,
        max_output_tokens: int | None = None,
    ):
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self.model = model or self.DEFAULT_MODEL
        self.max_output_tokens = max_output_tokens or self.DEFAULT_MAX_OUTPUT_TOKENS
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

    def generate(self, prompt: str, system: str | None = None) -> GenerationResult:
        message = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_output_tokens,
            system=system or "You are a C# code generator specializing in Trimble XChange DataObjects.",
            messages=[{"role": "user", "content": prompt}],
        )
        return GenerationResult(
            text=message.content[0].text,
            input_tokens=message.usage.input_tokens,
            output_tokens=message.usage.output_tokens,
        )

    def count_tokens(self, prompt: str, system: str | None = None) -> int:
        result = self.client.messages.count_tokens(
            model=self.model,
            system=system or "",
            messages=[{"role": "user", "content": prompt}],
        )
        return result.input_tokens


class OpenAIProvider:
    """OpenAI GPT provider."""

    DEFAULT_MODEL = "gpt-5-mini-2025-08-07"
    # max_completion_tokens is optional for OpenAI — omitting it lets the model
    # generate until it naturally stops. No default cap is set here.
    DEFAULT_MAX_OUTPUT_TOKENS: int | None = None

    def __init__(
        self,
        api_key: str | None = None,
        model: str | None = None,
        max_output_tokens: int | None = None,
    ):
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        self.model = model or self.DEFAULT_MODEL
        # None means "no cap" — the model runs until natural completion.
        self.max_output_tokens: int | None = (
            max_output_tokens if max_output_tokens is not None else self.DEFAULT_MAX_OUTPUT_TOKENS
        )
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

    def generate(self, prompt: str, system: str | None = None) -> GenerationResult:
        create_kwargs: dict[str, Any] = {
            "model": self.model,
            "input": prompt,
        }
        if system:
            create_kwargs["instructions"] = system
        if self.max_output_tokens is not None:
            create_kwargs["max_output_tokens"] = self.max_output_tokens
        response = self.client.responses.create(**create_kwargs)
        usage = response.usage
        return GenerationResult(
            text=response.output_text or "",
            input_tokens=usage.input_tokens if usage else 0,
            output_tokens=usage.output_tokens if usage else 0,
        )

    def count_tokens(self, prompt: str, system: str | None = None) -> int:
        try:
            import tiktoken
            enc = tiktoken.encoding_for_model(self.model)
            return len(enc.encode((system or "") + prompt))
        except (ImportError, KeyError):
            # Rough heuristic: 1 token ≈ 4 characters
            return len((system or "") + prompt) // 4


class DryRunProvider:
    """Dry-run provider that doesn't call any API."""

    model: str = "dry_run"

    def generate(self, prompt: str, system: str | None = None) -> GenerationResult:
        return GenerationResult(
            text="// Dry run - no code generated",
            input_tokens=0,
            output_tokens=0,
        )

    def count_tokens(self, prompt: str, system: str | None = None) -> int:
        return len((system or "") + prompt) // 4


def get_provider(config: dict[str, Any]) -> LLMProvider:
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
    llm_cfg: dict[str, Any]
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

    max_output_tokens: int | None = llm_cfg.get("max_output_tokens")  # None = use provider default

    if provider_name == "anthropic":
        return AnthropicProvider(api_key=api_key, model=model, max_output_tokens=max_output_tokens)
    elif provider_name == "openai":
        return OpenAIProvider(api_key=api_key, model=model, max_output_tokens=max_output_tokens)
    else:
        raise ValueError(
            f"Unknown LLM provider '{provider_name}'. "
            "Supported providers: anthropic, openai"
        )


def generate_code(prompt: str, system: str, provider: LLMProvider) -> tuple[str, int, int]:
    """Call the LLM and return (extracted C# code, input_tokens, output_tokens).

    Args:
        prompt: The user-facing prompt (schema + field information).
        system: The system prompt (code generation instructions).
        provider: Configured LLM provider.

    Returns:
        Tuple of (code, input_tokens, output_tokens) where code has markdown
        fences stripped.
    """
    result = provider.generate(prompt, system=system)
    max_out = getattr(provider, "max_output_tokens", None)
    if max_out and result.output_tokens >= max_out:
        print(
            f"WARNING: LLM output was truncated at {result.output_tokens} tokens "
            f"(max_output_tokens={max_out}). "
            "Increase llm.max_output_tokens in config.yaml or reduce target_input_tokens "
            "to fit fewer fields per page.",
            file=sys.stderr,
        )
    code = extract_code_from_response(result.text)
    return code, result.input_tokens, result.output_tokens


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
