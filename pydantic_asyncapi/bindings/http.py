"""HTTP bindings.

References: https://github.com/asyncapi/bindings/tree/master/http
"""
from typing import Literal

from pydantic import BaseModel

from pydantic_asyncapi.base import Schema, TypeOrRef


class HTTPOperationBinding(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "TRACE"]
    query: TypeOrRef[Schema]
    bindingVersion: str = "0.3.0"


class HTTPMessageBinding(BaseModel):
    headers: TypeOrRef[Schema]
    statusCode: int
    bindingVersion: str = "0.3.0"
