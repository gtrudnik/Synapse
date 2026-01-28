from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session
from src.database.core import get_db
from src.users.consts import AVATAR_DIR
from src.users.schemas import UserCreate, UserRead
from src.users.service import UserService
from src.auth.dependencies import get_current_user
from src.users.utils import save_avatar

router = APIRouter(tags=["users"])


@router.post("/register", response_model=UserRead)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        user = service.register_user(user_in)
        return user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/me", response_model=UserRead)
async def read_users_me(
    current_user: Annotated[UserRead, Depends(get_current_user)],
):
    return current_user


@router.post("/me/avatar", response_model=UserRead)
async def upload_avatar(
    current_user: Annotated[UserRead, Depends(get_current_user)],
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    file_location = await save_avatar(current_user.id, file)

    service = UserService(db)
    user = service.set_avatar(current_user.id, avatar_url=file_location)
    return user
