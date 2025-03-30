"""AsyncAPI SQS bindings.

References: https://github.com/asyncapi/bindings/tree/master/sqs
"""

from typing import Any, Literal, Optional, Union

from pydantic import BaseModel


class Identifier(BaseModel):
    arn: str
    name: str


class Statement(BaseModel):
    effect: Literal["Allow", "Deny"]
    principal: str
    action: Union[str, list[str]]
    resource: Optional[Union[str, list[str]]] = None
    condition: Optional[Union[dict[str, Any], list[dict[str, Any]]]] = None


class Policy(BaseModel):
    Statements: list[Statement]


class RedeliveryPolicy(BaseModel):
    deadLetterQueue: Identifier
    maxReceiveCount: int


class SQSQueue(BaseModel):
    name: str
    fifoQueue: bool
    deduplicationScope: Optional[str] = None
    fifoThroughputLimit: Optional[str] = None
    deliveryDelay: Optional[int] = None
    visibilityTimeout: Optional[int] = None
    receiveMessageWaitTime: Optional[int] = None
    messageRetentionPeriod: Optional[int] = None
    redrivePolicy: Optional[RedeliveryPolicy] = None
    policy: Optional[Policy] = None
    tags: Optional[dict[str, str]] = None


class SQSChannelBinding(BaseModel):
    queue: dict[str, SQSQueue]
    deadLetterQueue: Optional[SQSQueue] = None
    bindingVersion: str = "0.3.0"


class SQSOperationBinding(BaseModel):
    queues: list[SQSQueue]
    bindingVersion: str = "0.3.0"
