from datetime import datetime

from pydantic import BaseModel
from pydantic.types import UUID
from sqlmodel import SQLModel, Field


class Image(SQLModel, table=True):
    __tablename__: str = "image"
    id: UUID = Field(primary_key=True)
    file_name: str = Field()
    file: bytes = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
