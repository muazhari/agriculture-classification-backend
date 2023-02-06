from pydantic import BaseModel
from pydantic.types import UUID


class PatchOneRequest(BaseModel):
    file_name: str
    file: bytes
