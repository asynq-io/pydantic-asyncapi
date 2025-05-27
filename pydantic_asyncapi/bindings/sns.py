"""AsyncAPI SNS bindings.

References: https://github.com/asyncapi/bindings/tree/master/sns/3.0.0
"""

from typing import Any, Literal, Optional, Union

from pydantic import BaseModel
from pydantic.types import NonNegativeInt

Protocol = Literal[
    "http",
    "https",
    "email",
    "email-json",
    "sms",
    "sqs",
    "application",
    "lambda",
    "firehose",
]


class Ordering(BaseModel):
    type: str
    contentBasedDeduplication: bool = False


class Identifier(BaseModel):
    url: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    arn: Optional[str] = None
    name: Optional[str] = None


class Statement(BaseModel):
    effect: Literal["Allow", "Deny"]
    principal: Union[str, list[str]]
    action: Union[str, list[str], None] = None
    resource: Union[str, list[str], None] = None
    condition: Any = None


class Policy(BaseModel):
    statements: list[Statement]


class SNSChannelBinding(BaseModel):
    name: str
    ordering: Optional[Ordering] = None
    policy: Optional[str] = None
    tags: Optional[dict[str, str]] = None
    bindingVersion: str = "1.0.0"


class DeliveryPolicy(BaseModel):
    minDelayTarget: Optional[NonNegativeInt] = None
    maxDelayTarget: Optional[NonNegativeInt] = None
    numRetries: Optional[NonNegativeInt] = None
    numNoDelayRetries: Optional[NonNegativeInt] = None
    numMinDelayRetries: Optional[NonNegativeInt] = None
    numMaxDelayRetries: Optional[NonNegativeInt] = None
    backoffFunction: Optional[
        Literal["arithmetic", "exponential", "geometric", "linear"]
    ] = None
    maxReceivesPerSecond: Optional[NonNegativeInt] = None


class RedrivePolicy(BaseModel):
    deadLetterQueue: Identifier
    maxReceiveCount: NonNegativeInt = 10


class Consumer(BaseModel):
    protocol: Protocol
    endpoint: Identifier
    filterPolicy: Any = None
    filterPolicyScope: Any = None
    rawMessageDelivery: bool
    redrivePolicy: Optional[RedrivePolicy] = None
    deliveryPolicy: Optional[DeliveryPolicy] = None
    displayName: Optional[str] = None


class SNSOperationBinding(BaseModel):
    topic: Optional[Identifier] = None
    consumers: list[Consumer]
    deliveryPolicy: Optional[DeliveryPolicy] = None
    bindingVersion: str = "1.0.0"
