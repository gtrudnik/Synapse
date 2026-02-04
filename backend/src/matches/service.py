from sqlalchemy.orm import Session

from .repository import MatchRepository, LikeRepository
from .schemas import LikeRead, MatchRead, LikeCreate, MatchCreate, MatchList, LikeFilter


class LikeService:
    def __init__(self, db: Session):
        self.repo = LikeRepository(db)

    def like_card(self, data: LikeCreate) -> LikeRead:
        like = self.repo.create(data)
        return LikeRead.model_validate(like)

    def dislike_card(self, data: LikeFilter) -> LikeRead:
        like = self.repo.delete(data)
        return LikeRead.model_validate(like)

    def exists(self, data: LikeFilter):
        return self.repo.exists(data)


class MatchService:
    def __init__(self, db: Session):
        self.repo = MatchRepository(db)

    def create_match(self, data: MatchCreate) -> MatchRead:
        return self.repo.create(data)

    def get_matches_for_user(self, user_id: int) -> MatchList:
        return MatchList.model_validate(
            {"matches": self.repo.get_user_matches(user_id)}
        )

    def exists(self, from_user_id: int, target_user_id: int) -> bool:
        return self.repo.exists(from_user_id, target_user_id)
