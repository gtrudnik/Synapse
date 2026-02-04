from src.database.common import BaseRepository
from src import CardLike, UserMatch
from src.matches.schemas import LikeFilter, MatchCreate, LikeCreate


class LikeRepository(BaseRepository):
    model_cls = CardLike

    def __init__(self, db):
        super().__init__(db)

    def create(self, data: LikeCreate):
        like = self.model_cls(**data.model_dump())
        self.db.add(like)
        self.db.commit()
        return like

    def delete(self, data: LikeFilter):
        like = self.get_by_id(data)
        self.db.delete(like)
        self.db.commit()
        return like

    def get_by_id(self, data: LikeFilter) -> model_cls:
        like = (
            self.db.query(self.model_cls)
            .filter_by(from_user_id=data.from_user_id, to_card_id=data.to_card_id)
            .first()
        )
        return like

    def exists(self, data: LikeFilter) -> bool:
        return self.get_by_id(data) is not None


class MatchRepository(BaseRepository):
    model_cls = UserMatch

    def __init__(self, db):
        super().__init__(db)

    def get_by_id(self, match_id):
        match = self.db.query(self.model_cls).filter_by(id=match_id).first()
        return match

    def create(self, data: MatchCreate):
        match = self.model_cls(**data.model_dump())
        self.db.commit()
        self.db.refresh(match)
        return match

    def delete(self, match_id: int):
        match = self.get_by_id(match_id=match_id)
        self.db.delete(match)
        self.db.commit()
        return match

    def get_user_matches(self, user_id: int) -> list[UserMatch]:
        return (
            self.db.query(UserMatch)
            .filter((UserMatch.user1_id == user_id) | (UserMatch.user2_id == user_id))
            .order_by(UserMatch.created_at.desc())
            .all()
        )

    def exists(self, from_user_id: int, target_user_id: int) -> bool:
        exists = (
            self.db.query(UserMatch)
            .filter(
                UserMatch.user1_id.in_([from_user_id, target_user_id]),
                UserMatch.user2_id.in_([from_user_id, target_user_id]),
            )
            .first()
        )
        return bool(exists)
