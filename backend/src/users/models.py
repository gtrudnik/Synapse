from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.sql import func
from src.database.core import Base

import uuid
from pydantic import BaseModel


class CardBase(BaseModel):
    description: str
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(
        String, unique=True, index=True, nullable=False
    )

    hashed_password: Mapped[String] = mapped_column(String, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=True)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    cards = relationship(
        "Card",
        back_populates="user",
        cascade="all, delete-orphan",
    )
