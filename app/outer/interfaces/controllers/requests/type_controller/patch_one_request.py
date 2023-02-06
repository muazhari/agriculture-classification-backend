from pydantic import BaseModel
from pydantic.types import UUID


class PatchOneRequest(BaseModel):
    name: str
