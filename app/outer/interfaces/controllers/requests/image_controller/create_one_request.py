from pydantic import BaseModel


class CreateOneRequest(BaseModel):
    file_name: str
    file: bytes
