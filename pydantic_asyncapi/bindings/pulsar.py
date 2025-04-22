"""Pulsar bindings.

References: https://github.com/asyncapi/bindings/tree/master/pulsar
"""

from typing import Literal, Optional

from pydantic import BaseModel, Field


class PulsarServerBinding(BaseModel):
    tenant: str = "public"
    bindingVersion: str = "0.1.0"


class Retention(BaseModel):
    size: int = 0
    time: int = 0


class PulsarChannelBinding(BaseModel):
    namespace: str
    persistence: Literal["persistent", "non-persistent"]
    compaction: Optional[int] = None
    geo_replication: Optional[list[str]] = Field(None, alias="geo-replication")
    retention: Optional[Retention] = None
    ttl: Optional[int] = None
    deduplication: Optional[bool] = None
    bindingVersion: str = "0.1.0"
