from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserShort(BaseModel):
    id: int
    email: EmailStr
    name: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: Optional[str]


class UserLogin(BaseModel):
    email: EmailStr
    password: str
