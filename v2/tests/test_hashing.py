"""Tests for shared/hashing.py."""

from schmith.shared.hashing import canonical_json_hash


class TestCanonicalJsonHash:
    def test_identical_inputs_produce_same_hash(self) -> None:
        assert canonical_json_hash({"a": 1, "b": 2}) == canonical_json_hash({"a": 1, "b": 2})

    def test_key_order_does_not_affect_hash(self) -> None:
        assert canonical_json_hash({"b": 2, "a": 1}) == canonical_json_hash({"a": 1, "b": 2})

    def test_different_values_produce_different_hashes(self) -> None:
        assert canonical_json_hash({"a": 1}) != canonical_json_hash({"a": 2})

    def test_different_keys_produce_different_hashes(self) -> None:
        assert canonical_json_hash({"a": 1}) != canonical_json_hash({"b": 1})

    def test_nested_dicts_are_canonical(self) -> None:
        a = {"outer": {"z": 3, "a": 1}}
        b = {"outer": {"a": 1, "z": 3}}
        assert canonical_json_hash(a) == canonical_json_hash(b)

    def test_returns_40_char_hex_string(self) -> None:
        result = canonical_json_hash({"x": "y"})
        assert isinstance(result, str)
        assert len(result) == 40
        assert all(c in "0123456789abcdef" for c in result)

    def test_list_input(self) -> None:
        assert canonical_json_hash([1, 2, 3]) == canonical_json_hash([1, 2, 3])

    def test_empty_dict(self) -> None:
        result = canonical_json_hash({})
        assert isinstance(result, str)
        assert len(result) == 40
