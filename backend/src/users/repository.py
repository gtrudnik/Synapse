from sqlalchemy.orm import Session

from . import security
from .models import User
from .schemas import UserCreate


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def create(self, user: UserCreate) -> User:
        print(user.password)
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

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return security.verify_password(plain_password, hashed_password)
