from __future__ import annotations

from typing import Any, Literal

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
    SchemaFormat,
    SecurityScheme,
    ServerVariable,
    StrEnum,
    Tag,
    TypeRefMap,
)


class MultiFormatSchema(ExtendableBaseModel):
    schemaFormat: SchemaFormat = "application/vnd.aai.asyncapi+json;version=3.0.0"
    schema_: Any = Field(alias="schema")


class Server(ExtendableBaseModel):
    host: str
    protocol: str
    protocolVersion: str | None = None
    pathname: str | None = None
    description: str | None = None
    title: str | None = None
    summary: str | None = None
    variables: TypeRefMap[ServerVariable] = None
    security: TypeRefMap[SecurityScheme] = None
    tags: list[Tag] | None = None
    externalDocs: ExternalDocumentation | Reference | None = None
    bindings: TypeRefMap[Bindings] = None


class MessageTrait(BaseMessageTrait):
    pass


class Message(MessageTrait):
    payload: MultiFormatSchema | Schema | Reference
    traits: list[MessageTrait | Reference] | None = None


class Parameter(ExtendableBaseModel):
    enum: StrEnum | None = None
    default: str | None = None
    description: str | None = None
    examples: list[str] | None = None
    location: str | None = None


class Channel(ExtendableBaseModel):
    address: str | None = None
    messages: TypeRefMap[Message] = None
    title: str | None = None
    summary: str | None = None
    description: str | None = None
    servers: list[Reference] | None = None
    parameters: TypeRefMap[Parameter] = None
    tags: list[Tag] | None = None
    externalDocs: ExternalDocumentation | Reference | None = None
    bindings: TypeRefMap[Bindings] = None


class OperationReplyAddress(BaseModel):
    location: str
    description: str | None


class Reply(BaseModel):
    address: OperationReplyAddress | Reference
    channel: Reference
    messages: list[Reference]


class OperationTrait(ExtendableBaseModel):
    title: str | None = None
    summary: str | None = None
    description: str | None = None
    security: list[SecurityScheme | Reference] | None = None
    tags: list[Tag] | None = None
    externalDocs: ExternalDocumentation | Reference | None = None
    bindings: TypeRefMap[Bindings] = None
    reply: Reply | Reference | None = None


class Operation(OperationTrait):
    action: Literal["send", "receive"]
    channel: Reference
    messages: list[Reference] = []
    traits: list[OperationTrait | Reference] | None = None


class Components(BaseComponents):
    schemas: TypeRefMap[MultiFormatSchema | Schema] = None
    servers: TypeRefMap[Server] = None
    channels: TypeRefMap[Channel] = None
    operations: TypeRefMap[Operation] = None
    messages: TypeRefMap[Message] = None
    securitySchemas: TypeRefMap[SecurityScheme] = None
    serverVariables: TypeRefMap[ServerVariable] = None
    parameters: TypeRefMap[Parameter] = None
    replies: TypeRefMap[Reply] = None
    replyAddresses: TypeRefMap[OperationReplyAddress] = None
    operationTraits: TypeRefMap[OperationTrait] = None
    messageTraits: TypeRefMap[MessageTrait] = None


class Info(ExtendableBaseModel):
    title: str
    version: str
    description: str | None = None
    termsOfService: AnyUrl | None = None
    contact: Contact | None = None
    license: License | None = None
    tags: list[Tag] | None = None
    externalDocs: ExternalDocumentation | Reference | None = None


class AsyncAPI(ExtendableBaseModel):
    asyncapi: Literal["3.0.0"] = "3.0.0"
    id: str | None = None
    info: Info
    servers: TypeRefMap[Server] = None
    defaultContentType: str | None = None
    channels: TypeRefMap[Channel] = None
    operations: TypeRefMap[Operation] = None
    components: Components | None = None
