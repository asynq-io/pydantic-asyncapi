"""Solace bindings.

References: https://github.com/asyncapi/bindings/tree/master/solace
"""

from typing import Literal, Optional, Union

from pydantic import BaseModel

from pydantic_asyncapi.base import Reference, Schema


class SolaceServerBinding(BaseModel):
    msgVpn: Optional[str] = None
    clientName: Optional[str] = None
    bindingVersion: str = "0.4.0"


class Queue(BaseModel):
    name: Optional[str] = None
    topicSubscriptions: Optional[list[str]] = None
    accessType: Optional[Literal["exclusive", "nonexclusive"]] = None
    maxMsgSpoolSize: Optional[str] = None
    maxTtl: Optional[str] = None


class Topic(BaseModel):
    topicSubscriptions: Optional[list[str]] = None


class Destination(BaseModel):
    destinationType: Literal["queue", "topic"]
    deliveryMode: Literal["direct", "persistent"]
    queue: Queue
    topic: Topic
    bindingVersion: str = "0.4.0"


class SolaceOperationBinding(BaseModel):
    destinations: Optional[list[Destination]] = None
    timeToLive: Union[int, Schema, Reference, None] = None
    priority: Union[int, Schema, Reference, None] = None
    dmqEligible: bool = False
    bindingVersion: str = "0.4.0"
