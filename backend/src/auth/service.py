import os
from datetime import datetime, timezone, timedelta

import jwt
from sqlalchemy.orm import Session

from src import security

from src.users.models import User
from src.users.repository import UserRepository

SECRET_KEY = os.getenv("SECRET_KEY", "secret")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = 60


class AuthService:
    def __init__(self, db: Session):
        self.users = UserRepository(db)

    def authenticate(self, email: str, password: str) -> User | None:
        user = self.users.get_by_email(email)
        if not user or not security.verify_password(password, user.hashed_password):
            return None
        return user

    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(
                minutes=ACCESS_TOKEN_EXPIRE_MINUTES
            )
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    def decode_access_token(token: str) -> int | None:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return int(payload.get("sub"))
        except ValueError:
            return None
        except jwt.InvalidSignatureError:
            raise RuntimeError("Invalid signature")
