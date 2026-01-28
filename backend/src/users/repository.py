from sqlalchemy.orm import Session

from src import security
from .models import User
from .schemas import UserCreate


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def get_by_id(self, id: int) -> User | None:
        return self.db.query(User).get(id)

    def create(self, user: UserCreate) -> User:
        hashed_password = security.hash_password(user.password)
        db_user = User(
            email=user.email,
            hashed_password=hashed_password,
            name=user.name,
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
