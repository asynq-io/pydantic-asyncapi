from typing import Annotated, Any, Literal, Optional, Union

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
    messageId: Optional[str] = None


class Message(MessageTrait):
    payload: Any
    traits: Optional[list[Union[MessageTrait, Reference]]] = None


MessageOrRef = Annotated[list[Union[Message, Reference]], annotated_types.Len(1, None)]


class OneOf(BaseModel):
    oneOf: MessageOrRef


class OperationTrait(ExtendableBaseModel):
    operationId: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    security: Optional[list[SecurityScheme]] = None
    tags: Optional[list[Tag]] = None
    externalDocs: Union[ExternalDocumentation, Reference, None] = None
    bindings: TypeRefMap[Bindings]


class Operation(OperationTrait):
    traits: Optional[list[Union[OperationTrait, Reference]]] = None
    message: Union[Message, Reference, OneOf]


class Parameter(BaseModel):
    description: Optional[str] = None
    schema_: Optional[Union[Schema, Reference]] = Field(None, alias="schema")
    location: Optional[str] = None


class ChannelItem(ExtendableBaseModel):
    ref: Optional[str] = Field(None, alias="$ref")
    description: Optional[str] = None
    servers: Optional[list[str]] = None
    publish: Optional[Operation] = None
    subscribe: Optional[Operation] = None
    parameters: TypeRefMap[Parameter]
    bindings: Optional[Bindings] = None


class Server(ExtendableBaseModel):
    url: AnyUrl
    protocol: str
    protocolVersion: Optional[str] = None
    description: Optional[str] = None
    variables: TypeRefMap[ServerVariable]
    security: Optional[list[SecurityScheme]] = None
    tags: Optional[list[Tag]] = None
    bindings: TypeRefMap[Bindings]


class Components(BaseComponents):
    schemas: TypeRefMap[Schema]
    servers: TypeRefMap[Server]
    channels: TypeRefMap[ChannelItem]
    operations: TypeRefMap[Operation]
    messages: TypeRefMap[Message]
    securitySchemas: TypeRefMap[SecurityScheme]
    serverVariables: TypeRefMap[ServerVariable]
    parameters: TypeRefMap[Parameter]
    operationTraits: TypeRefMap[OperationTrait]
    messageTraits: TypeRefMap[MessageTrait]


class Info(ExtendableBaseModel):
    title: str
    version: str
    description: Optional[str] = None
    termsOfService: Optional[str] = None
    contact: Optional[Contact] = None
    license: Optional[License] = None


class AsyncAPI(ExtendableBaseModel):
    asyncapi: Literal["2.6.0"] = "2.6.0"
    id: Optional[str] = None
    info: Info
    defaultContentType: Optional[str] = None
    servers: TypeRefMap[Server]
    channels: dict[str, ChannelItem]
    components: Optional[Components] = None
    tags: Optional[list[Tag]] = None
