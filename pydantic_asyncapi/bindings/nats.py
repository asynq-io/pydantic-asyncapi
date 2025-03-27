"""AsyncAPI NATS bindings.
References: https://github.com/asyncapi/bindings/tree/master/nats
"""


from pydantic import BaseModel


class NatsOperationBinding(BaseModel):
    queue: str
    bindingVersion: str = "0.1.0"
