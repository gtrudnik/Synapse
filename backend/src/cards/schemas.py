import uuid
from pydantic import BaseModel, ConfigDict


class CardBase(BaseModel):
    description: str

class CardCreate(CardBase):
    pass


class CardRead(CardBase):
    id: uuid.UUID
    user_id: int

    model_config = ConfigDict(from_attributes=True)