"""AsyncAPI AMQP bindings.

References: https://github.com/asyncapi/bindings/tree/master/amqp
"""

from typing import Annotated, Literal, Optional, Union

from pydantic import BaseModel, Field, PositiveInt


class Queue(BaseModel):
    """A class to represent a queue.

    Attributes:
        name : name of the queue
        durable : indicates if the queue is durable
        exclusive : indicates if the queue is exclusive
        autoDelete : indicates if the queue should be automatically deleted
        vhost : virtual host of the queue (default is "/")
    """

    name: str
    durable: bool
    exclusive: bool
    autoDelete: bool
    vhost: str = "/"


class Exchange(BaseModel):
    type: Literal[
        "default",
        "direct",
        "topic",
        "fanout",
        "headers",
        "x-delayed-message",
        "x-consistent-hash",
        "x-modulus-hash",
    ]

    name: Optional[str] = None
    durable: Optional[bool] = None
    autoDelete: Optional[bool] = None
    vhost: str = "/"


class QueueBinding(BaseModel):
    is_: Literal["queue"] = Field(..., alias="is")
    queue: Queue
    bindingVersion: str = "0.3.0"


class ExchangeBinding(BaseModel):
    is_: Literal["exchange"] = Field(..., alias="is")
    exchange: Exchange
    bindingVersion: str = "0.3.0"


AMQPChannelBinding = Annotated[
    Union[QueueBinding, ExchangeBinding], Field(discriminator="is_")
]


class AMQPOperationBinding(BaseModel):
    expiration: Optional[PositiveInt] = None
    userId: Optional[str] = None
    cc: Optional[list[str]] = None
    priority: Optional[PositiveInt] = None
    deliveryMode: Optional[int] = None
    mandatory: Optional[bool] = None
    bcc: Optional[list[str]] = None
    timestamp: Optional[bool] = None
    ack: bool = True
    bindingVersion: str = "0.3.0"


class AMQPMessageBinding(BaseModel):
    contentEncoding: str
    messageType: str
    bindingVersion: str = "0.3.0"
