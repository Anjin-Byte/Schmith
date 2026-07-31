"""Tests for llm provider config-shape handling."""

from types import SimpleNamespace

from schmith.generation.llm import DryRunProvider, GenerationResult, OpenAIProvider, get_provider


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


# ---------------------------------------------------------------------------
# GenerationResult
# ---------------------------------------------------------------------------


class TestGenerationResult:
    def test_fields_accessible_by_name(self) -> None:
        r = GenerationResult(text="hello", input_tokens=10, output_tokens=5)
        assert r.text == "hello"
        assert r.input_tokens == 10
        assert r.output_tokens == 5

    def test_unpacks_as_tuple(self) -> None:
        text, inp, out = GenerationResult(text="x", input_tokens=1, output_tokens=2)
        assert text == "x"
        assert inp == 1
        assert out == 2


# ---------------------------------------------------------------------------
# DryRunProvider protocol compliance
# ---------------------------------------------------------------------------


class TestDryRunProviderProtocol:
    def test_model_attribute_is_dry_run(self) -> None:
        assert DryRunProvider().model == "dry_run"

    def test_generate_returns_generation_result(self) -> None:
        result = DryRunProvider().generate("prompt", system="sys")
        assert isinstance(result, GenerationResult)

    def test_generate_text_is_nonempty_string(self) -> None:
        result = DryRunProvider().generate("prompt")
        assert isinstance(result.text, str)
        assert len(result.text) > 0

    def test_generate_token_fields_are_zero(self) -> None:
        # DryRunProvider makes no API call; token counts are always 0.
        result = DryRunProvider().generate("prompt")
        assert result.input_tokens == 0
        assert result.output_tokens == 0

    def test_count_tokens_returns_int(self) -> None:
        n = DryRunProvider().count_tokens("hello world", system="sys")
        assert isinstance(n, int)

    def test_count_tokens_positive_for_nonempty(self) -> None:
        n = DryRunProvider().count_tokens("hello world", system="sys")
        assert n > 0

    def test_count_tokens_zero_for_empty_string_and_no_system(self) -> None:
        n = DryRunProvider().count_tokens("", system=None)
        assert n == 0

    def test_count_tokens_scales_with_length(self) -> None:
        short = DryRunProvider().count_tokens("hi")
        long = DryRunProvider().count_tokens("hi" * 100)
        assert long > short

    def test_count_tokens_none_system_equals_empty_system(self) -> None:
        p = DryRunProvider()
        assert p.count_tokens("abc", system=None) == p.count_tokens("abc", system="")


class TestOpenAIProviderResponsesAPI:
    def test_generate_uses_responses_api(self) -> None:
        provider = OpenAIProvider(api_key="test-key", model="gpt-5.3-codex", max_output_tokens=321)

        captured: dict[str, object] = {}

        class _Responses:
            def create(self, **kwargs):
                captured.update(kwargs)
                return SimpleNamespace(
                    output_text="public class Example {}",
                    usage=SimpleNamespace(input_tokens=123, output_tokens=45),
                )

        provider._client = SimpleNamespace(responses=_Responses())

        result = provider.generate("user prompt", system="system prompt")

        assert result == GenerationResult(
            text="public class Example {}",
            input_tokens=123,
            output_tokens=45,
        )
        assert captured["model"] == "gpt-5.3-codex"
        assert captured["input"] == "user prompt"
        assert captured["instructions"] == "system prompt"
        assert captured["max_output_tokens"] == 321
