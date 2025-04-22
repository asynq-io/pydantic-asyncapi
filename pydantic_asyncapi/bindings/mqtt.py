"""MQTT bindings.

References: https://github.com/asyncapi/bindings/tree/master/mqtt
"""
from typing import Optional, Union

from pydantic import BaseModel

from pydantic_asyncapi.base import Reference, Schema


class LastWill(BaseModel):
    topic: str
    qos: int
    message: str
    retain: bool


class MQTTServerBinding(BaseModel):
    clientId: Optional[str] = None
    cleanSession: Optional[bool] = None
    lastWill: Optional[LastWill] = None
    keepAlive: Optional[int] = None
    sessionExpiryInterval: Union[int, Schema, Reference, None] = None
    maximumPacketSize: Union[int, Schema, Reference, None] = None
    bindingVersion: str = "0.2.0"


class MQTTOperationBinding(BaseModel):
    qos: Optional[int] = None
    retain: Optional[bool] = None
    messageExpiryInterval: Union[int, Schema, Reference, None] = None
    bindingVersion: str = "0.2.0"


class MQTTMessageBinding(BaseModel):
    payloadFormatIndicator: Optional[int] = None
    correlationData: Union[Schema, Reference, None] = None
    contentType: Optional[str] = None
    responseTopic: Union[str, Schema, Reference, None] = None
    bindingVersion: str = "0.2.0"
