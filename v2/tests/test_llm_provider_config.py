"""Tests for llm provider config-shape handling."""

from schmith.generation.llm import DryRunProvider, OpenAIProvider, get_provider


def test_get_provider_accepts_top_level_config_with_llm_block() -> None:
    provider = get_provider({
        "llm": {
            "provider": "openai",
            "api_key": "test-key",
        }
    })
    assert isinstance(provider, OpenAIProvider)


def test_get_provider_accepts_direct_llm_config_block() -> None:
    provider = get_provider({
        "provider": "openai",
        "api_key": "test-key",
    })
    assert isinstance(provider, OpenAIProvider)


def test_get_provider_honors_top_level_dry_run_with_llm_block() -> None:
    provider = get_provider({
        "dry_run": True,
        "llm": {
            "provider": "openai",
            "api_key": "test-key",
        },
    })
    assert isinstance(provider, DryRunProvider)


def test_get_provider_honors_direct_dry_run() -> None:
    provider = get_provider({
        "dry_run": True,
        "provider": "openai",
        "api_key": "test-key",
    })
    assert isinstance(provider, DryRunProvider)
