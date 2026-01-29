import uuid

from sqlalchemy.orm import Session

from src.matches.models import UserMatch
from .models import ChatMessage, ChatConversation
from .schemas import MessageCreate


class ChatRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, id: uuid.UUID) -> ChatMessage | None:
        return self.db.query(ChatMessage).get(id)

    def create(self, message_data: MessageCreate) -> ChatMessage:
        message = ChatMessage(**message_data.model_dump())
        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)
        return message

    def get_all(self, user1_id: int, user2_id: int) -> list[type[ChatMessage]]:
        return (
            self.db.query(ChatMessage)
            .filter(
                (
                    (ChatMessage.sender_id == user1_id)
                    & (ChatMessage.receiver_id == user2_id)
                )
                | (
                    (ChatMessage.sender_id == user2_id)
                    & (ChatMessage.receiver_id == user1_id)
                )
            )
            .order_by(ChatMessage.timestamp)
            .all()
        )

    def get_user_chats(self, user_id: int) -> list[type[ChatConversation]]:
        return (
            self.db.query(ChatConversation)
            .join(UserMatch, ChatConversation.match_id == UserMatch.id)
            .filter((UserMatch.user1_id == user_id) | (UserMatch.user2_id == user_id))
            .all()
        )
