import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class LikeRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    from_user_id: int
    to_card_id: uuid.UUID
    created_at: datetime


class LikeCreate(BaseModel):
    from_user_id: int
    to_card_id: uuid.UUID


class LikeFilter(LikeCreate):
    pass


class MatchRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user1_id: int
    user2_id: int
    created_at: datetime


class MatchList(BaseModel):
    matches: list[MatchRead]


class MatchCreate(BaseModel):
    user1_id: int
    user2_id: int
