"""AnypointMQ bindings.

References: https://github.com/asyncapi/bindings/tree/master/anypointmq
"""

from typing import Literal, Optional

from pydantic import BaseModel

from pydantic_asyncapi.base import Schema, TypeOrRef


class AnypointMQChannelBinding(BaseModel):
    destination: Optional[str] = None
    destinationType: Literal["queue", "exchange", "fifo-queue"] = "queue"
    bindingVersion: str = "0.1.0"


class AnypointMQMessageBinding(BaseModel):
    headers: Optional[TypeOrRef[Schema]] = None
    bindingVersion: str = "0.1.0"
