import enum

from pydantic import BaseModel, EmailStr, ConfigDict, field_validator
from datetime import datetime
from typing import Optional

from src.users.consts import SKILLS


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    email: EmailStr
    name: Optional[str]
    created_at: datetime
    avatar_url: Optional[str]
    skills: list[str]


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: Optional[str]


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserUpdateSkills(BaseModel):
    skills: list[str]

    @field_validator("skills")
    @classmethod
    def validate_skills(cls, skills: list[str]):
        unknown_skills = set(skills) - SKILLS
        if unknown_skills:
            raise ValueError(f"Unknown skills: {', '.join(unknown_skills)}")
        return skills
