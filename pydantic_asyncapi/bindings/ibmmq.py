"""AsyncAPI IBM MQ Bindings.
References: https://github.com/asyncapi/bindings/tree/master/ibmmq
"""

from typing import Literal, Optional

from pydantic import BaseModel, NonNegativeInt, PositiveInt


class IBMMQServerBinding(BaseModel):
    groupId: Optional[str] = None
    ccdtQueueManagerName: Optional[str] = None
    cipherSpec: Optional[str] = None
    multiEndpointServer: bool = False
    heartBeatInterval: PositiveInt = 300
    bindingVersion: str = "0.1.0"


class Queue(BaseModel):
    objectName: str
    isPartitioned: bool = False
    exclusive: bool = False


class Topic(BaseModel):
    string: Optional[str] = None
    objectName: Optional[str] = None
    durablePermitted: bool = True
    lastMsgRetained: bool = False
    maxMsgLength: Optional[PositiveInt] = None


class IBMMQChannelBinding(BaseModel):
    destinationType: Literal["queue", "topic"]
    queue: Optional[Queue] = None
    topic: Optional[Topic] = None
    bindingVersion: str = "0.1.0"


class IBMMQOperationBinding(BaseModel):
    type: Optional[Literal["string", "jms", "binary"]] = None
    headers: Optional[str] = None
    description: Optional[str] = None
    expiry: Optional[NonNegativeInt] = None
    bindingVersion: str = "0.1.0"
