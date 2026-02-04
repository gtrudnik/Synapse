from sqlalchemy.orm import Session

from src.cards.models import Card


class CardRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, *, description: str, user_id: int) -> Card:
        card = Card(
            description=description,
            user_id=user_id,
        )
        self.db.add(card)
        self.db.commit()
        self.db.refresh(card)
        return card

    def get_by_user(self, user_id: int) -> list[type[Card]]:
        return (
            self.db.query(Card)
            .filter(Card.user_id == user_id)
            .all()
        )

    def get_all(self) -> list[type[Card]]:
        return self.db.query(Card).all()