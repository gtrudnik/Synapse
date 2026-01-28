import uuid
from pydantic import BaseModel


class CardBase(BaseModel):
    description: str

class CardCreate(CardBase):
    pass


class CardRead(CardBase):
    id: uuid.UUID
    user_id: uuid.UUID

    model_config = {
        "from_attributes": True
    }