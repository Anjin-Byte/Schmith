from typing import Any, Iterator, Protocol

from ingest.spec_adapters import get_adapter
from ingest.model import ResponseSchema


class AdapterProtocol(Protocol):
    name: str

    def load_spec(self, spec_path: str) -> Any:  # pragma: no cover - concrete adapters type this
        ...

    def iter_response_schemas(self, spec: Any) -> Iterator[ResponseSchema]:  # pragma: no cover - concrete adapters type this
        ...


def load_adapter(name: str) -> AdapterProtocol:
    return get_adapter(name)
