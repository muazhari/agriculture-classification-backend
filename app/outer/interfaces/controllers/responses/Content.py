from typing import Generic

from pydantic.generics import GenericModel
from pydantic.types import TypeVar, Any

T = TypeVar("T")


class Content(GenericModel, Generic[T]):
    message: str
    data: T
