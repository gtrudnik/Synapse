from sqlalchemy.orm import Session

from .repository import ChatRepository
from .schemas import (
    MessageCreate,
    MessageRead,
    MessageList,
    ConversationList,
)


class ChatService:
    def __init__(self, db: Session):
        self.repo = ChatRepository(db)

    def send_message(self, message_data: MessageCreate) -> MessageRead:
        message = self.repo.create(message_data)
        return MessageRead.model_validate(message)

    def get_messages(self, user1_id: int, user2_id: int) -> MessageList:
        messages = self.repo.get_all(user1_id, user2_id)
        return MessageList.model_validate({"messages": messages})

    def get_chats_for_user(self, user_id: int) -> ConversationList:
        return ConversationList.model_validate(
            {"conversations": self.repo.get_user_chats(user_id)}
        )
