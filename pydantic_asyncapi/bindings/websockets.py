"""WebSockets bindings.

References: https://github.com/asyncapi/bindings/tree/master/websockets
"""
from typing import Literal

from pydantic import BaseModel

from pydantic_asyncapi.base import Schema, TypeOrRef


class WebSocketsChannelBinding(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"]
    query: TypeOrRef[Schema]
    headers: TypeOrRef[Schema] = None
    bindingVersion: str = "0.1.0"
