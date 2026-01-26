"""LLM provider implementations for code generation.

This module provides a unified interface for interacting with different
LLM providers (Anthropic Claude, OpenAI GPT) for code generation tasks.
"""

import os
import sys
from pathlib import Path
from typing import Protocol


def load_dotenv() -> None:
    """Load environment variables from .env file."""
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        with open(env_path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, _, value = line.partition("=")
                    key = key.strip()
                    value = value.strip().strip("\"'")
                    if key and value:
                        os.environ.setdefault(key, value)


# Load .env on module import
load_dotenv()


class LLMProvider(Protocol):
    """Protocol for LLM providers."""

    def generate(self, prompt: str, system: str | None = None) -> str:
        """Generate a response from the LLM.

        Args:
            prompt: The user prompt
            system: Optional system message

        Returns:
            Generated text response
        """
        ...


class AnthropicProvider:
    """Anthropic Claude provider."""

    DEFAULT_MODEL = "claude-3-5-haiku-20241022"

    def __init__(self, api_key: str | None = None, model: str | None = None):
        """Initialize the provider.

        Args:
            api_key: Anthropic API key. Defaults to ANTHROPIC_API_KEY env var.
            model: Model to use. Defaults to claude-3-5-haiku-20241022.
        """
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self.model = model or self.DEFAULT_MODEL
        self._client = None

        if not self.api_key:
            raise ValueError(
                "Anthropic API key required. Set ANTHROPIC_API_KEY environment "
                "variable or pass api_key parameter."
            )

    @property
    def client(self):
        """Lazily initialize the Anthropic client."""
        if self._client is None:
            try:
                import anthropic

                self._client = anthropic.Anthropic(api_key=self.api_key)
            except ImportError:
                print("Error: anthropic package not installed.", file=sys.stderr)
                print("Install with: pip install anthropic", file=sys.stderr)
                sys.exit(1)
        return self._client

    def generate(self, prompt: str, system: str | None = None) -> str:
        """Generate a response using Claude."""
        message = self.client.messages.create(
            model=self.model,
            max_tokens=4096,
            system=system or "You are a C# code generator specializing in Trimble XChange DataObjects.",
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text


class OpenAIProvider:
    """OpenAI GPT provider."""

    DEFAULT_MODEL = "gpt-4o"

    def __init__(self, api_key: str | None = None, model: str | None = None):
        """Initialize the provider.

        Args:
            api_key: OpenAI API key. Defaults to OPENAI_API_KEY env var.
            model: Model to use. Defaults to gpt-4o.
        """
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        self.model = model or self.DEFAULT_MODEL
        self._client = None

        if not self.api_key:
            raise ValueError(
                "OpenAI API key required. Set OPENAI_API_KEY environment "
                "variable or pass api_key parameter."
            )

    @property
    def client(self):
        """Lazily initialize the OpenAI client."""
        if self._client is None:
            try:
                import openai

                self._client = openai.OpenAI(api_key=self.api_key)
            except ImportError:
                print("Error: openai package not installed.", file=sys.stderr)
                print("Install with: pip install openai", file=sys.stderr)
                sys.exit(1)
        return self._client

    def generate(self, prompt: str, system: str | None = None) -> str:
        """Generate a response using GPT."""
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
        """Return placeholder for dry run."""
        return "// Dry run - no code generated"


def get_provider(
    provider_name: str = "anthropic",
    model: str | None = None,
    dry_run: bool = False,
) -> LLMProvider:
    """Get an LLM provider instance.

    Args:
        provider_name: Name of provider ("anthropic", "openai")
        model: Optional model override
        dry_run: If True, return a dry-run provider

    Returns:
        LLMProvider instance

    Raises:
        ValueError: If provider_name is unknown
    """
    if dry_run:
        return DryRunProvider()

    if provider_name == "anthropic":
        return AnthropicProvider(model=model)
    elif provider_name == "openai":
        return OpenAIProvider(model=model)
    else:
        raise ValueError(
            f"Unknown provider '{provider_name}'. "
            "Supported providers: anthropic, openai"
        )


def extract_code_from_response(response: str) -> str:
    """Extract C# code from LLM response, handling markdown code blocks.

    Args:
        response: Raw LLM response text

    Returns:
        Extracted code without markdown formatting
    """
    # Check if response contains markdown code blocks
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

    # No code blocks, return as-is
    return response.strip()
