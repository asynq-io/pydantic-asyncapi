from typing import Any, Literal, Optional, TypeVar, Union

from pydantic import AnyUrl, Field

from .base import ExtendableBaseModel, Reference, Schema, StrEnum, TypeOrRef, TypeRefMap
from .bindings.amqp import AMQPChannelBinding, AMQPMessageBinding, AMQPOperationBinding
from .bindings.anypointmq import AnypointMQChannelBinding, AnypointMQMessageBinding
from .bindings.googlepubsub import (
    GooglePubSubChannelBinding,
    GooglePubSubMessageBinding,
)
from .bindings.ibmmq import (
    IBMMQChannelBinding,
    IBMMQOperationBinding,
    IBMMQServerBinding,
)
from .bindings.kafka import (
    KafkaChannelBinding,
    KafkaOperationBinding,
    KafkaServerBinding,
)
from .bindings.mqtt import MQTTMessageBinding, MQTTOperationBinding, MQTTServerBinding
from .bindings.nats import NatsOperationBinding
from .bindings.pulsar import (
    PulsarChannelBinding,
    PulsarServerBinding,
)
from .bindings.sns import SNSChannelBinding, SNSOperationBinding
from .bindings.solace import SolaceOperationBinding, SolaceServerBinding
from .bindings.sqs import SQSChannelBinding, SQSOperationBinding
from .bindings.websockets import WebSocketsChannelBinding

T = TypeVar("T")


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


class License(ExtendableBaseModel):
    name: str
    url: AnyUrl


class Tag(ExtendableBaseModel):
    name: str
    description: Optional[str] = None
    externalDocs: Optional[Union[ExternalDocumentation, Reference]] = None


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
    in_: str = Field(..., alias="in")
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


class ServerBindings(ExtendableBaseModel):
    amqp: None = None
    amqp1: None = None
    anypointmq: None = None
    googlepubsub: None = None
    http: None = None
    ibmmq: TypeOrRef[IBMMQServerBinding] = None
    kafka: TypeOrRef[KafkaServerBinding] = None
    mqtt: TypeOrRef[MQTTServerBinding] = None
    nats: None = None
    pulsar: TypeOrRef[PulsarServerBinding] = None
    sns: None = None
    solace: TypeOrRef[SolaceServerBinding] = None
    sqs: None = None
    stomp: None = None
    redis: None = None
    ws: None = None


class ChannelBindings(ExtendableBaseModel):
    amqp: TypeOrRef[AMQPChannelBinding] = None
    amqp1: None = None
    anypointmq: TypeOrRef[AnypointMQChannelBinding] = None
    googlepubsub: TypeOrRef[GooglePubSubChannelBinding] = None
    http: None = None
    ibmmq: TypeOrRef[IBMMQChannelBinding] = None
    kafka: TypeOrRef[KafkaChannelBinding] = None
    mqtt: None = None
    nats: None = None
    pulsar: TypeOrRef[PulsarChannelBinding] = None
    sns: TypeOrRef[SNSChannelBinding] = None
    solace: None = None
    sqs: TypeOrRef[SQSChannelBinding] = None
    stomp: None = None
    redis: None = None
    ws: TypeOrRef[WebSocketsChannelBinding] = None


class OperationBindings(ExtendableBaseModel):
    amqp: TypeOrRef[AMQPOperationBinding] = None
    amqp1: None = None
    anypointmq: None = None
    googlepubsub: None = None
    http: None = None
    ibmmq: TypeOrRef[IBMMQOperationBinding] = None
    kafka: TypeOrRef[KafkaOperationBinding] = None
    mqtt: TypeOrRef[MQTTOperationBinding] = None
    nats: TypeOrRef[NatsOperationBinding] = None
    pulsar: None = None
    sns: TypeOrRef[SNSOperationBinding] = None
    solace: TypeOrRef[SolaceOperationBinding] = None
    sqs: TypeOrRef[SQSOperationBinding] = None
    stomp: None = None
    redis: None = None
    ws: None = None


class MessageBindings(ExtendableBaseModel):
    amqp: Optional[TypeOrRef[AMQPMessageBinding]] = None
    amqp1: None = None
    anypointmq: Optional[TypeOrRef[AnypointMQMessageBinding]] = None
    googlepubsub: Optional[TypeOrRef[GooglePubSubMessageBinding]] = None
    http: None = None
    kafka: None = None
    mqtt: Optional[TypeOrRef[MQTTMessageBinding]] = None
    nats: None = None
    pulsar: None = None
    sns: None = None
    solace: None = None
    sqs: None = None
    redis: None = None
    ws: None = None


class MessageExample(ExtendableBaseModel):
    headers: Optional[dict[str, Any]] = None
    payload: dict[str, Any]
    name: Optional[str] = None
    summary: Optional[str] = None


class BaseMessageTrait(ExtendableBaseModel):
    headers: Optional[Union[Schema, Reference]] = None
    correlationId: Optional[Union[CorrelationId, Reference]] = None
    schemaFormat: Optional[Union[SchemaFormat, str]] = None
    contentType: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[list[Tag]] = None
    externalDocs: Optional[Union[ExternalDocumentation, Reference]] = None
    bindings: Optional[MessageBindings] = None
    examples: Optional[list[MessageExample]] = None


class BaseComponents(ExtendableBaseModel):
    externalDocs: TypeRefMap[ExternalDocumentation] = None
    tags: TypeRefMap[Tag] = None
    correlationIds: TypeRefMap[CorrelationId] = None
    messageBindings: Optional[MessageBindings] = None
    serverBindings: Optional[ServerBindings] = None
    channelBindings: Optional[ChannelBindings] = None
    operationBindings: Optional[OperationBindings] = None
