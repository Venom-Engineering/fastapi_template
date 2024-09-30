from enum import StrEnum

from pydantic import BaseModel, Field


class ModelName(StrEnum):
    ALEXNET = "alexnet"
    RESNET = "resnet"
    LENET = "lenet"


class Item(BaseModel):
    name: str = Field(examples=["Foo"])
    description: str | None = Field(
        default=None,
        title="The description of the item",
        max_length=300,
        examples=["A very nice Item"],
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None
