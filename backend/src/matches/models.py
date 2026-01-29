import uuid
from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from src.database.core import Base


class CardLike(Base):
    __tablename__ = "card_likes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    from_user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=False
    )

    to_card_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("cards.id"), nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    __table_args__ = (
        UniqueConstraint("from_user_id", "to_card_id", name="uq_card_like"),
    )


class UserMatch(Base):
    __tablename__ = "user_matches"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user1_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user2_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    __table_args__ = (UniqueConstraint("user1_id", "user2_id", name="uq_user_match"),)
