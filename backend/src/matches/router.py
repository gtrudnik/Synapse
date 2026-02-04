import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database.core import get_db
from src.auth.dependencies import get_current_user
from src.users.schemas import UserRead
from .service import MatchService, LikeService
from .schemas import LikeCreate, MatchRead, LikeRead, LikeFilter

router = APIRouter()


@router.post("/like", response_model=LikeRead | None)
def like_user(
    card_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: UserRead = Depends(get_current_user),
):
    service = LikeService(db)
    like_data = LikeFilter.model_validate(
        {"from_user_id": current_user.id, "to_card_id": card_id}
    )
    if service.exists(like_data):
        service.dislike_card(like_data)
        return None
    return service.like_card(
        LikeCreate.model_validate(
            {"from_user_id": current_user.id, "to_card_id": card_id}
        )
    )
