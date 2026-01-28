from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.core import get_db
from src.cards.service import CardService
from src.cards.schemas import CardCreate, CardRead

router = APIRouter()


@router.post("/", response_model=CardRead)
def create_card(
    card_in: CardCreate,
    user_id: int,
    db: Session = Depends(get_db),
):
    service = CardService(db)
    return service.create_card(user_id=user_id, card_in=card_in)


@router.get("/", response_model=list[CardRead])
def get_all_cards(
    db: Session = Depends(get_db),
):
    service = CardService(db)
    return service.get_all_cards()


@router.get("/{user_id}", response_model=list[CardRead])
def get_user_cards(
    user_id: int,
    db: Session = Depends(get_db),
):
    service = CardService(db)
    return service.get_user_cards(user_id)
