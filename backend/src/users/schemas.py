from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional


class UserShort(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    email: EmailStr
    name: Optional[str]
    created_at: datetime


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: Optional[str]


class UserLogin(BaseModel):
    email: EmailStr
    password: str
