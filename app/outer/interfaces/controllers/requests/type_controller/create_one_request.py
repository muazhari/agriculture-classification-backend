from pydantic import BaseModel


class CreateOneRequest(BaseModel):
    name: str
