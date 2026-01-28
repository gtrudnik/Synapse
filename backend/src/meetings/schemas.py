from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
import uuid


class ZoomMeetingCreate(BaseModel):
    host_id: int
    topic: str
    start_time: datetime


class ZoomMeetingRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    host_id: int
    topic: str
    start_time: datetime
    join_url: str
