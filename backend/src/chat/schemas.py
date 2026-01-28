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

