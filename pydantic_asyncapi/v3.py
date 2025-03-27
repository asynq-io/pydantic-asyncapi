from typing import Any, Literal, Optional, Union

from pydantic import AnyUrl, Field

from .common import (
    BaseComponents,
    BaseMessageTrait,
    BaseModel,
    ChannelBindings,
    Contact,
    ExtendableBaseModel,
    ExternalDocumentation,
    License,
    OperationBindings,
    Reference,
    Schema,
    SchemaFormat,
    SecurityScheme,
    ServerBindings,
    ServerVariable,
    StrEnum,
    Tag,
    TypeRefMap,
)


class MultiFormatSchema(ExtendableBaseModel):
    schemaFormat: SchemaFormat = "application/vnd.aai.asyncapi+json;version=3.0.0"
    schema_: Any = Field(..., alias="schema")


class Server(ExtendableBaseModel):
    host: str
    protocol: str
    protocolVersion: Optional[str] = None
    pathname: Optional[str] = None
    description: Optional[str] = None
    title: Optional[str] = None
    summary: Optional[str] = None
    variables: TypeRefMap[ServerVariable] = None
    security: TypeRefMap[SecurityScheme] = None
    tags: Optional[list[Tag]] = None
    externalDocs: Optional[Union[ExternalDocumentation, Reference]] = None
    bindings: Optional[ServerBindings] = None


class MessageTrait(BaseMessageTrait):
    pass


class Message(MessageTrait):
    payload: Union[Schema, Reference, MultiFormatSchema]
    traits: Optional[list[Union[MessageTrait, Reference]]] = None


class Parameter(ExtendableBaseModel):
    enum: Optional[StrEnum] = None
    default: Optional[str] = None
    description: Optional[str] = None
    examples: Optional[list[str]] = None
    location: Optional[str] = None


class Channel(ExtendableBaseModel):
    address: Optional[str] = None
    messages: TypeRefMap[Message] = None
    title: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    servers: Optional[list[Reference]] = None
    parameters: TypeRefMap[Parameter] = None
    tags: Optional[list[Tag]] = None
    externalDocs: Optional[Union[ExternalDocumentation, Reference]] = None
    bindings: Optional[ChannelBindings] = None


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
    externalDocs: Optional[Union[ExternalDocumentation, Reference]] = None
    bindings: Optional[OperationBindings] = None
    reply: Optional[Union[Reply, Reference]] = None


class Operation(OperationTrait):
    action: Literal["send", "receive"]
    channel: Reference
    messages: list[Reference] = []
    traits: Optional[list[Union[OperationTrait, Reference]]] = None


class Components(BaseComponents):
    schemas: TypeRefMap[Union[MultiFormatSchema, Schema]] = None
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
    description: Optional[str] = None
    termsOfService: Optional[AnyUrl] = None
    contact: Optional[Contact] = None
    license: Optional[License] = None
    tags: Optional[list[Tag]] = None
    externalDocs: Optional[Union[ExternalDocumentation, Reference]] = None


class AsyncAPI(ExtendableBaseModel):
    asyncapi: Literal["3.0.0"] = "3.0.0"
    id: Optional[str] = None
    info: Info
    servers: TypeRefMap[Server] = None
    defaultContentType: Optional[str] = None
    channels: TypeRefMap[Channel] = None
    operations: TypeRefMap[Operation] = None
    components: Optional[Components] = None
