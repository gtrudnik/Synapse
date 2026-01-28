from fastapi import UploadFile
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import current_user

from .repository import UserRepository
from .schemas import UserCreate, UserUpdateSkills
from .models import User
from src import security
from .utils import save_avatar


class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def create_user(self, user: UserCreate) -> User:
        existing = self.repo.get_by_email(user.email)
        if existing:
            raise ValueError("User with this email already exists")

        return self.repo.create(user)

    async def set_avatar(self, user_id: int, file: UploadFile) -> User:
        user = self._get_or_raise(user_id)
        filename = await save_avatar(file)

        return self.repo.update(user, {"avatar_path": filename})

    def update_skills(self, user_id: int, skills_data: UserUpdateSkills) -> User:
        user = self._get_or_raise(user_id)

        return self.repo.update(user, {"skills": skills_data.skills})

    def _get_or_raise(self, user_id: int) -> User | None:
        user = self.repo.get_by_id(user_id)
        if not user:
            raise ValueError(f"User with id {user_id} does not exist")

        return user
