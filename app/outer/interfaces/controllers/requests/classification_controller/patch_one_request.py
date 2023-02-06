from pydantic import BaseModel
from pydantic.types import UUID


class PatchOneRequest(BaseModel):
    image_id: UUID
    type_id: UUID
    result: str
