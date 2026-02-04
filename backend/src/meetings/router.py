from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.database.core import get_db
from src.auth.dependencies import get_current_user
from .schemas import ZoomMeetingCreate, ZoomMeetingRead
from .service import ZoomMeetingService
from src.users.models import User
from src.chat.service import ChatService  # для отправки ссылки
from ..chat.schemas import MessageCreate

router = APIRouter()


@router.post("/", response_model=ZoomMeetingRead)
def create_meeting(
    meeting_data: ZoomMeetingCreate,
    other_user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ZoomMeetingService(db)
    chat_service = ChatService(db)

    meeting = service.create_zoom_meeting(meeting_data)
    chat_service.send_message(
        message_data=MessageCreate.model_validate(
            {
                "content": f"Вам назначен Zoom митинг: {meeting.join_url}",
                "receiver_id": other_user_id,
                "sender_id": current_user.id,
            }
        ),
    )

    return meeting
