from typing import Annotated, Any, Literal, Optional, TypeVar, Union

import annotated_types
from pydantic import AnyUrl, ConfigDict, Field, NonNegativeInt, PositiveFloat
from pydantic import BaseModel as PydanticBaseModel

T = TypeVar("T")

SimpleTypes = Literal[
    "array", "boolean", "integer", "null", "number", "object", "string"
]

NonEmptyList = Annotated[list[T], annotated_types.MinLen(1)]
StrEnum = NonEmptyList[str]


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
TypeOrRef = Annotated[Optional[Union[T, Reference]], ...]


class Schema(BaseModel):
    field_id: Optional[str] = Field(None, alias="$id")
    field_schema: Optional[AnyUrl] = Field(None, alias="$schema")
    field_ref: Optional[str] = Field(None, alias="$ref")
    field_comment: Optional[str] = Field(None, alias="$comment")
    title: Optional[str] = None
    description: Optional[str] = None
    default: Any = None
    readOnly: bool = False
    writeOnly: bool = False
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
    uniqueItems: bool = False
    contains: Optional["Schema"] = None
    maxProperties: Optional[NonNegativeInt] = None
    minProperties: Optional[NonNegativeInt] = None
    required: Optional[list[str]] = None
    additionalProperties: Optional[Union["Schema", bool]] = None
    definitions: Optional[dict[str, "Schema"]] = {}
    properties: Optional[dict[str, "Schema"]] = {}
    patternProperties: Optional[dict[str, "Schema"]] = {}
    dependencies: Optional[dict[str, Union["Schema", list[str]]]] = None
    propertyNames: Optional["Schema"] = None
    const: Any = None
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
