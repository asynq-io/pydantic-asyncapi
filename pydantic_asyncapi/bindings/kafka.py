"""AsyncAPI Kafka bindings.

References: https://github.com/asyncapi/bindings/tree/master/kafka
"""

from typing import Any, Optional

from pydantic import BaseModel, Field, PositiveInt


class KafkaServerBinding(BaseModel):
    schemaRegistryUrl: Optional[str] = None
    schemaRegistryVendor: Optional[str] = None
    bindingVersion: Optional[str] = "0.5.0"


class TopicConfiguration(BaseModel):
    cleanup_policy: Optional[list[str]] = Field(None, alias="cleanup.policy")
    retention_ms: Optional[int] = Field(None, alias="retention.ms")
    retention_bytes: Optional[int] = Field(None, alias="retention.bytes")
    delete_retention_ms: Optional[int] = Field(None, alias="delete.retention.ms")
    max_message_bytes: Optional[int] = Field(None, alias="max.message.bytes")
    confluent_key_schema_validation: Optional[bool] = Field(
        None, alias="confluent.key.schema.validation"
    )
    confluent_key_subject_name_strategy: Optional[str] = Field(
        None, alias="confluent.key.subject.name.strategy"
    )
    confluent_value_schema_validation: Optional[bool] = Field(
        None, alias="confluent.value.schema.validation"
    )
    confluent_value_subject_name_strategy: Optional[str] = Field(
        None, alias="confluent.value.subject.name.strategy"
    )


class KafkaChannelBinding(BaseModel):
    topic: Optional[str] = None
    partitions: Optional[PositiveInt] = None
    replicas: Optional[PositiveInt] = None
    topicConfiuration: Optional[TopicConfiguration] = None
    bindingVersion: str = "0.4.0"


class KafkaOperationBinding(BaseModel):
    groupId: Optional[dict[str, Any]] = None
    clientId: Optional[dict[str, Any]] = None
    replyTo: Optional[dict[str, Any]] = None
    bindingVersion: str = "0.4.0"
