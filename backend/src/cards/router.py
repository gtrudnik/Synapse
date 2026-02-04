from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.auth.dependencies import get_current_user
from src.database.core import get_db
from src.cards.service import CardService
from src.cards.schemas import CardCreate, CardRead
from src.users.schemas import UserRead

router = APIRouter()


@router.post("/", response_model=CardRead)
def create_card(
    card_data: CardCreate,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    service = CardService(db)
    return service.create_card(user_id=current_user.id, card_data=card_data)


@router.get("/all", response_model=list[CardRead])
def get_all_cards(
    db: Session = Depends(get_db),
):
    service = CardService(db)
    return service.get_all_cards()


@router.get("/", response_model=list[CardRead])
def get_user_cards(
    current_user: Annotated[UserRead, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    service = CardService(db)
    return service.get_user_cards(current_user.id)
