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
    variables: TypeRefMap[ServerVariable]
    security: TypeRefMap[SecurityScheme]
    tags: list[Tag] | None = None
    externalDocs: ExternalDocumentation | Reference | None = None
    bindings: TypeRefMap[Bindings]


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
    messages: TypeRefMap[Message]
    title: str | None = None
    summary: str | None = None
    description: str | None = None
    servers: list[Reference] | None = None
    parameters: TypeRefMap[Parameter]
    tags: list[Tag] | None = None
    externalDocs: ExternalDocumentation | Reference | None = None
    bindings: TypeRefMap[Bindings]


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
    bindings: TypeRefMap[Bindings]
    reply: Reply | Reference | None = None


class Operation(OperationTrait):
    action: Literal["send", "receive"]
    channel: Reference
    messages: list[Reference] = []
    traits: list[OperationTrait | Reference] | None = None


class Components(BaseComponents):
    schemas: TypeRefMap[MultiFormatSchema | Schema]
    servers: TypeRefMap[Server]
    channels: TypeRefMap[Channel]
    operations: TypeRefMap[Operation]
    messages: TypeRefMap[Message]
    securitySchemas: TypeRefMap[SecurityScheme]
    serverVariables: TypeRefMap[ServerVariable]
    parameters: TypeRefMap[Parameter]
    replies: TypeRefMap[Reply]
    replyAddresses: TypeRefMap[OperationReplyAddress]
    operationTraits: TypeRefMap[OperationTrait]
    messageTraits: TypeRefMap[MessageTrait]


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
    servers: TypeRefMap[Server]
    defaultContentType: str | None = None
    channels: TypeRefMap[Channel]
    operations: TypeRefMap[Operation]
    components: Components | None = None
