from sqlalchemy.orm import Session

from .repository import CardRepository
from .schemas import CardCreate
from .models import Card


class CardService:
    def __init__(self, db: Session):
        self.repo = CardRepository(db)

    def create_card(self, user_id: int, card_in: CardCreate) -> Card:
        return self.repo.create(
            description=card_in.description,
            user_id=user_id,
        )

    def get_user_cards(self, user_id: int) -> list[type[Card]]:
        return self.repo.get_by_user(user_id)

    def get_all_cards(self) -> list[type[Card]]:
        return self.repo.get_all()