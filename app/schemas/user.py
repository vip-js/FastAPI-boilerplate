from pydantic import BaseModel, Field
from app.core.base import register_schema

@register_schema
class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)

@register_schema
class UserCreate(UserBase):
    password: str = Field(..., min_length=6)

@register_schema
class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True
        populate_by_name = True
