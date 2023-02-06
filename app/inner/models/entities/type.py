from datetime import datetime

from pydantic import BaseModel
from pydantic.types import UUID
from sqlmodel import SQLModel, Field


class Type(SQLModel, table=True):
    __tablename__: str = "type"
    id: UUID = Field(primary_key=True)
    name: str = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
