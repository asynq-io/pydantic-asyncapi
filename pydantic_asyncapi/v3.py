from typing import Any, Literal, Optional, Union

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
    protocolVersion: Optional[str] = None
    pathname: Optional[str] = None
    description: Optional[str] = None
    title: Optional[str] = None
    summary: Optional[str] = None
    variables: TypeRefMap[ServerVariable]
    security: TypeRefMap[SecurityScheme]
    tags: Optional[list[Tag]] = None
    externalDocs: Union[ExternalDocumentation, Reference, None] = None
    bindings: TypeRefMap[Bindings]


class MessageTrait(BaseMessageTrait):
    pass


class Message(MessageTrait):
    payload: Union[MultiFormatSchema, Schema, Reference]
    traits: Optional[list[Union[MessageTrait, Reference]]] = None


class Parameter(ExtendableBaseModel):
    enum: Optional[StrEnum] = None
    default: Optional[str] = None
    description: Optional[str] = None
    examples: Optional[list[str]] = None
    location: Optional[str] = None


class Channel(ExtendableBaseModel):
    address: Optional[str] = None
    messages: TypeRefMap[Message]
    title: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    servers: Optional[list[Reference]] = None
    parameters: TypeRefMap[Parameter]
    tags: Optional[list[Tag]] = None
    externalDocs: Union[ExternalDocumentation, Reference, None] = None
    bindings: TypeRefMap[Bindings]


class OperationReplyAddress(BaseModel):
    location: str
    description: Optional[str]


class Reply(BaseModel):
    address: Union[OperationReplyAddress, Reference]
    channel: Reference
    messages: list[Reference]


class OperationTrait(ExtendableBaseModel):
    title: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    security: Optional[list[Union[SecurityScheme, Reference]]] = None
    tags: Optional[list[Tag]] = None
    externalDocs: Union[ExternalDocumentation, Reference, None] = None
    bindings: TypeRefMap[Bindings]
    reply: Union[Reply, Reference, None] = None


class Operation(OperationTrait):
    action: Literal["send", "receive"]
    channel: Reference
    messages: list[Reference] = []
    traits: Optional[list[Union[OperationTrait, Reference]]] = None


class Components(BaseComponents):
    schemas: TypeRefMap[Union[MultiFormatSchema, Schema]]
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
    description: Optional[str] = None
    termsOfService: Optional[AnyUrl] = None
    contact: Optional[Contact] = None
    license: Optional[License] = None
    tags: Optional[list[Tag]] = None
    externalDocs: Union[ExternalDocumentation, Reference, None] = None


class AsyncAPI(ExtendableBaseModel):
    asyncapi: Literal["3.0.0"] = "3.0.0"
    id: Optional[str] = None
    info: Info
    servers: TypeRefMap[Server]
    defaultContentType: Optional[str] = None
    channels: TypeRefMap[Channel]
    operations: TypeRefMap[Operation]
    components: Optional[Components] = None
