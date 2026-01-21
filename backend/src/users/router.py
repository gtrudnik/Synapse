from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.database.core import get_db
from .schemas import UserCreate, UserShort, UserLogin
from .service import UserService

router = APIRouter(tags=["users"])

@router.post("/register", response_model=UserShort)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        user = service.register_user(user_in)
        return user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/login", response_model=UserShort)
def login(data: UserLogin, db: Session = Depends(get_db)):
    service = UserService(db)
    user = service.authenticate_user(data.email, data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return user