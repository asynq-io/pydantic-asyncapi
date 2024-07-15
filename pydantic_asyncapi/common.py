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
    ref: str = Field(alias="$ref")


TypeRefMap = Annotated[Optional[dict[str, Union[T, Reference]]], Field(default=None)]

NonEmptyList = Annotated[list[T], annotated_types.MinLen(1)]


class ExternalDocumentation(ExtendableBaseModel):
    url: AnyUrl
    description: Optional[str] = None


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
    field_id: Optional[str] = Field(None, alias="$id")
    field_schema: Optional[AnyUrl] = Field(None, alias="$schema")
    field_ref: Optional[str] = Field(None, alias="$ref")
    field_comment: Optional[str] = Field(None, alias="$comment")
    title: Optional[str] = None
    description: Optional[str] = None
    default: Optional[Any] = None
    readOnly: Optional[bool] = False
    writeOnly: Optional[bool] = False
    examples: Optional[list[Any]] = None
    multipleOf: Optional[PositiveFloat] = None
    maximum: Optional[float] = None
    exclusiveMaximum: Optional[float] = None
    minimum: Optional[float] = None
    exclusiveMinimum: Optional[float] = None
    maxLength: Optional[NonNegativeInt] = None
    minLength: Optional[NonNegativeInt] = None
    pattern: Optional[str] = None
    additionalItems: Optional["Schema"] = None
    items: Optional[Union["Schema", "SchemaList"]] = None
    maxItems: Optional[NonNegativeInt] = None
    minItems: Optional[NonNegativeInt] = None
    uniqueItems: Optional[bool] = False
    contains: Optional["Schema"] = None
    maxProperties: Optional[NonNegativeInt] = None
    minProperties: Optional[NonNegativeInt] = None
    required: Optional[list[str]] = None
    additionalProperties: Optional["Schema"] = None
    definitions: Optional[dict[str, "Schema"]] = {}
    properties: Optional[dict[str, "Schema"]] = {}
    patternProperties: Optional[dict[str, "Schema"]] = {}
    dependencies: Optional[dict[str, Union["Schema", list[str]]]] = None
    propertyNames: Optional["Schema"] = None
    const: Optional[Any] = None
    enum: Optional[StrEnum] = None
    type: Optional[Union[SimpleTypes, list[SimpleTypes]]] = None
    format: Optional[str] = None
    contentMediaType: Optional[str] = None
    contentEncoding: Optional[str] = None
    if_: Optional["Schema"] = Field(None, alias="if")
    then: Optional["Schema"] = None
    else_: Optional["Schema"] = Field(None, alias="else")
    allOf: Optional["SchemaList"] = None
    anyOf: Optional["SchemaList"] = None
    oneOf: Optional["SchemaList"] = None
    not_: Optional["Schema"] = Field(None, alias="not")


SchemaList = NonEmptyList[Schema]


Schema.model_rebuild()


class License(ExtendableBaseModel):
    name: str
    url: AnyUrl


class Tag(ExtendableBaseModel):
    name: str
    description: Optional[str] = None
    externalDocs: Union[ExternalDocumentation, Reference, None] = None


class Contact(ExtendableBaseModel):
    name: str
    url: AnyUrl
    email: str


class ServerVariable(ExtendableBaseModel):
    enum: Optional[StrEnum] = None
    default: Optional[str] = None
    description: Optional[str] = None
    examples: Optional[list[str]] = None


class OAuthFlow(ExtendableBaseModel):
    authorizationUrl: str
    tokenUrl: str
    refreshUrl: Optional[str] = None
    availableScopes: Optional[dict[str, str]] = None


class OAuthFlows(ExtendableBaseModel):
    implicit: Optional[OAuthFlow] = None
    password: Optional[OAuthFlow] = None
    clientCredentials: Optional[OAuthFlow] = None
    authorizationCode: Optional[OAuthFlow] = None


class SecurityScheme(ExtendableBaseModel):
    type: SecuritySchemaType
    name: str
    in_: str = Field(alias="in")
    description: Optional[str] = None
    scheme: str
    bearerFormat: Optional[str] = None
    flows: OAuthFlows
    openIdConnectUrl: AnyUrl
    scopes: Optional[list[str]] = None


class CorrelationId(ExtendableBaseModel):
    description: Optional[str] = None
    location: str = Field(
        pattern=r"^\$message\.(header|payload)#(\/(([^\/~])|(~[01]))*)*"
    )


class Binding(ExtendableBaseModel):
    """Base model for any binding. Contains extra fields depending on binding type."""

    bindingVersion: Optional[str] = None


class Bindings(ExtendableBaseModel):
    ws: Optional[Binding] = None
    kafka: Optional[Binding] = None
    anypointmq: Optional[Binding] = None
    amqp: Optional[Binding] = None
    amqp1: Optional[Binding] = None
    mqtt: Optional[Binding] = None
    mqtt5: Optional[Binding] = None
    nats: Optional[Binding] = None
    jms: Optional[Binding] = None
    sns: Optional[Binding] = None
    solace: Optional[Binding] = None
    sqs: Optional[Binding] = None
    stomp: Optional[Binding] = None
    redis: Optional[Binding] = None
    mercure: Optional[Binding] = None
    ibmmq: Optional[Binding] = None
    googlepubsub: Optional[Binding] = None
    pulsar: Optional[Binding] = None


class MessageExample(ExtendableBaseModel):
    headers: Optional[dict[str, Any]] = None
    payload: dict[str, Any]
    name: Optional[str] = None
    summary: Optional[str] = None


class BaseMessageTrait(ExtendableBaseModel):
    headers: Optional[Union[Schema, Reference]] = None
    correlationId: Optional[Union[CorrelationId, Reference]] = None
    schemaFormat: Union[SchemaFormat, str, None] = None
    contentType: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[list[Tag]] = None
    externalDocs: Union[ExternalDocumentation, Reference, None] = None
    bindings: TypeRefMap[Bindings]
    examples: Optional[list[MessageExample]] = None


class BaseComponents(ExtendableBaseModel):
    externalDocs: TypeRefMap[ExternalDocumentation]
    tags: TypeRefMap[Tag]
    correlationIds: TypeRefMap[CorrelationId]
    messageBindings: TypeRefMap[Bindings]
    serverBindings: TypeRefMap[Bindings]
    channelBindings: TypeRefMap[Bindings]
    operationBindings: TypeRefMap[Bindings]
