from typing import Union

from ingest.spec_adapters.openapi import OpenApiAdapter
from ingest.spec_adapters.raml import RamlAdapter


def get_adapter(name: str) -> Union[OpenApiAdapter, RamlAdapter]:
    if name == "raml":
        return RamlAdapter()
    if name == "openapi":
        return OpenApiAdapter()
    raise ValueError(f"Unknown adapter: {name}")
