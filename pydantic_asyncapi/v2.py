from __future__ import annotations

from typing import Annotated, Any, Literal, Union

import annotated_types
from pydantic import AnyUrl, Field

from .common import (
    BaseComponents,
    BaseMessageTrait,
    BaseModel,
    Bindings,
    Contact,
    ExtendableBaseModel,
    ExternalDocumentation,
    License,
    Reference,
    Schema,
    SecurityScheme,
    ServerVariable,
    Tag,
    TypeRefMap,
)


class MessageTrait(BaseMessageTrait):
    messageId: str | None = None


class Message(MessageTrait):
    payload: Any
    traits: list[MessageTrait | Reference] | None = None


MessageOrRef = Annotated[list[Union[Message, Reference]], annotated_types.Len(1, None)]


class OneOf(BaseModel):
    oneOf: MessageOrRef


class OperationTrait(ExtendableBaseModel):
    operationId: str | None = None
    summary: str | None = None
    description: str | None = None
    security: list[SecurityScheme] | None = None
    tags: list[Tag] | None = None
    externalDocs: ExternalDocumentation | Reference | None = None
    bindings: TypeRefMap[Bindings] = None


class Operation(OperationTrait):
    traits: list[OperationTrait | Reference] | None = None
    message: Message | Reference | OneOf


class Parameter(BaseModel):
    description: str | None = None
    schema_: Schema | Reference | None = Field(None, alias="schema")
    location: str | None = None


class ChannelItem(ExtendableBaseModel):
    ref: str | None = Field(None, validation_alias="$ref", serialization_alias="$ref")
    description: str | None = None
    servers: list[str] | None = None
    publish: Operation | None = None
    subscribe: Operation | None = None
    parameters: TypeRefMap[Parameter] = None
    bindings: Bindings | None = None


class Server(ExtendableBaseModel):
    url: AnyUrl
    protocol: str
    protocolVersion: str | None = None
    description: str | None = None
    variables: TypeRefMap[ServerVariable]
    security: list[SecurityScheme] | None = None
    tags: list[Tag] | None = None
    bindings: TypeRefMap[Bindings] = None


class Components(BaseComponents):
    schemas: TypeRefMap[Schema] = None
    servers: TypeRefMap[Server] = None
    channels: TypeRefMap[ChannelItem] = None
    operations: TypeRefMap[Operation] = None
    messages: TypeRefMap[Message] = None
    securitySchemas: TypeRefMap[SecurityScheme] = None
    serverVariables: TypeRefMap[ServerVariable] = None
    parameters: TypeRefMap[Parameter] = None
    operationTraits: TypeRefMap[OperationTrait] = None
    messageTraits: TypeRefMap[MessageTrait] = None


class Info(ExtendableBaseModel):
    title: str
    version: str
    description: str | None = None
    termsOfService: str | None = None
    contact: Contact | None = None
    license: License | None = None


class AsyncAPI(ExtendableBaseModel):
    asyncapi: Literal["2.6.0"] = "2.6.0"
    id: str | None = None
    info: Info
    defaultContentType: str | None = None
    servers: TypeRefMap[Server] = None
    channels: dict[str, ChannelItem]
    components: Components | None = None
    tags: list[Tag] | None = None
