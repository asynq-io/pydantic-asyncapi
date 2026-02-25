from importlib.metadata import version
from typing import Annotated, Union

from pydantic import Field, RootModel

from .v2 import AsyncAPI as AsyncAPIV2
from .v3 import AsyncAPI as AsyncAPIV3

__version__ = version(__name__)

AsyncAPIType = Annotated[Union[AsyncAPIV2, AsyncAPIV3], Field(discriminator="asyncapi")]

AsyncAPI = RootModel[AsyncAPIType]


__all__ = ["AsyncAPI", "AsyncAPIType", "__version__"]
