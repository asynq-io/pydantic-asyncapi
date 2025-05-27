"""Google Pub/Sub bindings.

References: https://github.com/asyncapi/bindings/tree/master/googlepubsub
"""

from typing import Literal, Optional

from pydantic import BaseModel, Field


class MessageStoragePolicy(BaseModel):
    allowedPersistenceRegions: list[str]


class SchemaSettings(BaseModel):
    encoding: Literal["JSON", "BINARY"]
    firstRevisionId: str
    lastRevisionId: str
    name: str


class GooglePubSubChannelBinding(BaseModel):
    labels: Optional[dict[str, str]] = None
    messageRetentionDuration: Optional[str]
    messageStoragePolicy: Optional[MessageStoragePolicy] = None
    schemaSettings: Optional[SchemaSettings] = None
    bindingVersion: str = "0.2.0"


class Schema(BaseModel):
    name: str


class GooglePubSubMessageBinding(BaseModel):
    attributes: Optional[dict[str, str]] = None
    orderingKey: Optional[str] = None
    message_schema: Optional[Schema] = Field(None, alias="schema")
    bindingVersion: str = "0.2.0"
