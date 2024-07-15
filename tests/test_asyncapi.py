import os

import pytest
import yaml

from pydantic_asyncapi import AsyncAPI
from pydantic_asyncapi.v2 import AsyncAPI as AsyncAPIV2
from pydantic_asyncapi.v3 import AsyncAPI as AsyncAPIV3

BASE_DIR = os.path.dirname(__file__)


def yaml_data(path):
    filename = os.path.join(BASE_DIR, "fixtures", path)
    with open(filename) as f:
        return yaml.safe_load(f)


@pytest.mark.parametrize(
    "filename", ["v2/simple.yaml", "v3/simple.yaml", "v3/backend.yaml"]
)
def test_parse(filename):
    cls = AsyncAPIV2 if filename.startswith("v2") else AsyncAPIV3
    data = yaml_data(filename)
    assert isinstance(data, dict)
    model = cls.model_validate(data)
    assert isinstance(model, cls)

    assert (
        model.model_dump(by_alias=True, exclude_none=True, exclude_unset=True) == data
    )


@pytest.mark.parametrize(
    "filename", ["v2/simple.yaml", "v3/simple.yaml", "v3/backend.yaml"]
)
def test_type_adapter(filename):
    data = yaml_data(filename)
    assert isinstance(data, dict)
    validated = AsyncAPI.model_validate(data)
    assert (
        validated.model_dump(by_alias=True, exclude_none=True, exclude_unset=True)
        == data
    )
