from typing import Annotated, Union

from pydantic import Field, RootModel

from .__about__ import __version__
from .v2 import AsyncAPI as AsyncAPIV2
from .v3 import AsyncAPI as AsyncAPIV3

T = Annotated[Union[AsyncAPIV2, AsyncAPIV3], Field(discriminator="asyncapi")]

AsyncAPI = RootModel[T]


__all__ = ["__version__"]
