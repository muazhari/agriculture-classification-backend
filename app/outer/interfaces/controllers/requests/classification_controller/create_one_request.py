from pydantic import BaseModel
from pydantic.types import UUID


class CreateOneRequest(BaseModel):
    image_id: UUID
    type_id: UUID
