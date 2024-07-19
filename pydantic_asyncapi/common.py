from __future__ import annotations

from typing import Annotated, Any, Literal, Optional, TypeVar, Union

import annotated_types
from pydantic import (
    AnyUrl,
    ConfigDict,
    Field,
    NonNegativeInt,
    PositiveFloat,
)
from pydantic import BaseModel as PydanticBaseModel

T = TypeVar("T")


class BaseModel(PydanticBaseModel):
    """Base model for all AsyncAPI models."""

    model_config = ConfigDict(
        populate_by_name=True,
        use_enum_values=True,
        from_attributes=True,
    )


class ExtendableBaseModel(BaseModel):
    """Base model for all AsyncAPI models that can be extended."""

    model_config = ConfigDict(
        extra="allow",
    )


class Reference(BaseModel):
    ref: str = Field(validation_alias="$ref", serialization_alias="$ref")


TypeRefMap = Annotated[Optional[dict[str, Union[T, Reference]]], ...]

NonEmptyList = Annotated[list[T], annotated_types.MinLen(1)]


class ExternalDocumentation(ExtendableBaseModel):
    url: AnyUrl
    description: str | None = None


SecuritySchemaType = Literal[
    "userPassword",
    "apiKey",
    "X509",
    "symmetricEncryption",
    "asymmetricEncryption",
    "httpApiKey",
    "http",
    "oauth2",
    "openIdConnect",
    "plain",
    "scramSha256",
    "scramSha512",
    "gssapi",
]

SchemaFormat = Literal[
    "application/vnd.aai.asyncapi+json;version=3.0.0",
    "application/schema+json;version=draft-07",
    "application/vnd.aai.asyncapi+yaml;version=3.0.0",
    "application/schema+yaml;version=draft-07",
    "application/vnd.apache.avro;version=1.9.0",
    "application/vnd.apache.avro+json;version=1.9.0",
    "application/vnd.apache.avro+yaml;version=1.9.0",
    "application/vnd.oai.openapi;version=3.0.0",
    "application/vnd.oai.openapi+json;version=3.0.0",
    "application/vnd.oai.openapi+yaml;version=3.0.0",
    "application/raml+yaml;version=1.0",
    "application/vnd.google.protobuf;version=2",
    "application/vnd.google.protobuf;version=3",
]

SimpleTypes = Literal[
    "array", "boolean", "integer", "null", "number", "object", "string"
]


StrEnum = NonEmptyList[str]


class Schema(BaseModel):
    field_id: str | None = Field(None, alias="$id")
    field_schema: AnyUrl | None = Field(None, alias="$schema")
    field_ref: str | None = Field(None, alias="$ref")
    field_comment: str | None = Field(None, alias="$comment")
    title: str | None = None
    description: str | None = None
    default: Any | None = None
    readOnly: bool | None = False
    writeOnly: bool | None = False
    examples: list[Any] | None = None
    multipleOf: PositiveFloat | None = None
    maximum: float | None = None
    exclusiveMaximum: float | None = None
    minimum: float | None = None
    exclusiveMinimum: float | None = None
    maxLength: NonNegativeInt | None = None
    minLength: NonNegativeInt | None = None
    pattern: str | None = None
    additionalItems: Schema | None = None
    items: Schema | SchemaList | None = None
    maxItems: NonNegativeInt | None = None
    minItems: NonNegativeInt | None = None
    uniqueItems: bool | None = False
    contains: Schema | None = None
    maxProperties: NonNegativeInt | None = None
    minProperties: NonNegativeInt | None = None
    required: list[str] | None = None
    additionalProperties: Schema | None = None
    definitions: dict[str, Schema] | None = {}
    properties: dict[str, Schema] | None = {}
    patternProperties: dict[str, Schema] | None = {}
    dependencies: dict[str, Schema | list[str]] | None = None
    propertyNames: Schema | None = None
    const: Any | None = None
    enum: StrEnum | None = None
    type: SimpleTypes | list[SimpleTypes] | None = None
    format: str | None = None
    contentMediaType: str | None = None
    contentEncoding: str | None = None
    if_: Schema | None = Field(None, alias="if")
    then: Schema | None = None
    else_: Schema | None = Field(None, alias="else")
    allOf: SchemaList | None = None
    anyOf: SchemaList | None = None
    oneOf: SchemaList | None = None
    not_: Schema | None = Field(None, alias="not")


SchemaList = NonEmptyList[Schema]


Schema.model_rebuild()


class License(ExtendableBaseModel):
    name: str
    url: AnyUrl


class Tag(ExtendableBaseModel):
    name: str
    description: str | None = None
    externalDocs: ExternalDocumentation | Reference | None = None


class Contact(ExtendableBaseModel):
    name: str
    url: AnyUrl
    email: str


class ServerVariable(ExtendableBaseModel):
    enum: StrEnum | None = None
    default: str | None = None
    description: str | None = None
    examples: list[str] | None = None


class OAuthFlow(ExtendableBaseModel):
    authorizationUrl: str
    tokenUrl: str
    refreshUrl: str | None = None
    availableScopes: dict[str, str] | None = None


class OAuthFlows(ExtendableBaseModel):
    implicit: OAuthFlow | None = None
    password: OAuthFlow | None = None
    clientCredentials: OAuthFlow | None = None
    authorizationCode: OAuthFlow | None = None


class SecurityScheme(ExtendableBaseModel):
    type: SecuritySchemaType
    name: str
    in_: str = Field(alias="in")
    description: str | None = None
    scheme: str
    bearerFormat: str | None = None
    flows: OAuthFlows
    openIdConnectUrl: AnyUrl
    scopes: list[str] | None = None


class CorrelationId(ExtendableBaseModel):
    description: str | None = None
    location: str = Field(
        pattern=r"^\$message\.(header|payload)#(\/(([^\/~])|(~[01]))*)*"
    )


class Binding(ExtendableBaseModel):
    """Base model for any binding. Contains extra fields depending on binding type."""

    bindingVersion: str | None = None


class Bindings(ExtendableBaseModel):
    ws: Binding | None = None
    kafka: Binding | None = None
    anypointmq: Binding | None = None
    amqp: Binding | None = None
    amqp1: Binding | None = None
    mqtt: Binding | None = None
    mqtt5: Binding | None = None
    nats: Binding | None = None
    jms: Binding | None = None
    sns: Binding | None = None
    solace: Binding | None = None
    sqs: Binding | None = None
    stomp: Binding | None = None
    redis: Binding | None = None
    mercure: Binding | None = None
    ibmmq: Binding | None = None
    googlepubsub: Binding | None = None
    pulsar: Binding | None = None


class MessageExample(ExtendableBaseModel):
    headers: dict[str, Any] | None = None
    payload: dict[str, Any]
    name: str | None = None
    summary: str | None = None


class BaseMessageTrait(ExtendableBaseModel):
    headers: Schema | Reference | None = None
    correlationId: CorrelationId | Reference | None = None
    schemaFormat: SchemaFormat | str | None = None
    contentType: str | None = None
    name: str | None = None
    title: str | None = None
    summary: str | None = None
    description: str | None = None
    tags: list[Tag] | None = None
    externalDocs: ExternalDocumentation | Reference | None = None
    bindings: TypeRefMap[Bindings] = None
    examples: list[MessageExample] | None = None


class BaseComponents(ExtendableBaseModel):
    externalDocs: TypeRefMap[ExternalDocumentation] = None
    tags: TypeRefMap[Tag] = None
    correlationIds: TypeRefMap[CorrelationId] = None
    messageBindings: TypeRefMap[Bindings] = None
    serverBindings: TypeRefMap[Bindings] = None
    channelBindings: TypeRefMap[Bindings] = None
    operationBindings: TypeRefMap[Bindings] = None
