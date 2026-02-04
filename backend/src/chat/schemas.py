from pydantic import BaseModel, ConfigDict
from datetime import datetime
import uuid


class MessageCreate(BaseModel):
    sender_id: int
    receiver_id: int
    content: str


class MessageRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    sender_id: int
    receiver_id: int
    content: str
    timestamp: datetime


class MessageList(BaseModel):
    messages: list[MessageRead] | None


class ConversationCreate(BaseModel):
    match_id: int


class ConversationRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    match_id: int


class ConversationList(BaseModel):
    conversations: list[ConversationRead]
