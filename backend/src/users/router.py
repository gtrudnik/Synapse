from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.database.core import get_db
from src.users.schemas import UserCreate, UserShort
from src.users.service import UserService
from src.auth.dependencies import get_current_user

router = APIRouter(tags=["users"])


@router.post("/register", response_model=UserShort)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        user = service.register_user(user_in)
        return user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/me", response_model=UserShort)
async def read_users_me(
    current_user: Annotated[UserShort, Depends(get_current_user)],
):
    return current_user
