from sqlalchemy.orm import Session
from .repository import UserRepository
from .schemas import UserCreate
from .models import User
from .. import security


class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def register_user(self, user: UserCreate) -> User:
        existing = self.repo.get_by_email(user.email)
        if existing:
            raise ValueError("User with this email already exists")
        return self.repo.create(user)

    def authenticate_user(self, email: str, password: str) -> User | None:
        user = self.repo.get_by_email(email)
        if not user:
            return None
        if not security.verify_password(password, user.hashed_password):
            return None
        return user
