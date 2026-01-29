from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime, Text, Integer, UUID
from datetime import datetime, UTC

from src.database.core import Base
import uuid


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=uuid.uuid4, index=True
    )
    chat_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("chats.id"),
        nullable=False,
        name="fk_message_chat_id",
    )
    sender_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), name="fk_message_sender_id"
    )
    receiver_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), name="fk_message_receiver_id"
    )
    content: Mapped[str] = mapped_column(Text)
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(UTC))

    sender = relationship("User", foreign_keys=[sender_id])
    receiver = relationship("User", foreign_keys=[receiver_id])
    chat = relationship("ChatConversation", foreign_keys=[chat_id])


class ChatConversation(Base):
    __tablename__ = "chats"
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=uuid.uuid4, index=True
    )
    match_id = mapped_column(
        Integer, ForeignKey("user_matches.id"), nullable=False, name="fk_conv_match_id"
    )

    messages = relationship(
        ChatMessage, back_populates="chat", cascade="all, delete-orphan"
    )
