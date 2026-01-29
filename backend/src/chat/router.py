from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict

from starlette import status

from src.auth.ws_dependencies import get_current_user_ws
from src.chat.schemas import MessageCreate, MessageRead, MessageList, ConversationList
from src.chat.service import ChatService
from src.database.core import get_db
from src.auth.dependencies import get_current_user
from src.users.models import User


router = APIRouter()

active_connections: Dict[int, WebSocket] = {}


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        current_user = await get_current_user_ws(websocket)
    except RuntimeError as e:
        return await websocket.close(code=1008)
    if current_user is None:
        return None
    user_id = current_user.id
    active_connections[user_id] = websocket
    try:
        while True:
            data = MessageCreate(**(await websocket.receive_json()), sender_id=user_id)
            db: Session = next(get_db())
            chat_service = ChatService(db)

            chat_service.send_message(
                message_data=MessageCreate(
                    sender_id=user_id,
                    receiver_id=data.receiver_id,
                    content=data.content,
                ),
            )

            if data.receiver_id in active_connections:
                await active_connections[data.receiver_id].send_json(
                    {"sender_id": user_id, "content": data.content}
                )
    except WebSocketDisconnect:
        del active_connections[user_id]


@router.get("/history/{other_user_id}", response_model=MessageList)
def get_chat_history(
    other_user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ChatService(db)
    messages = service.get_messages(user1_id=current_user.id, user2_id=other_user_id)
    return messages


@router.get("/my", response_model=ConversationList)
def get_user_chats(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    service = ChatService(db)
    chats = service.get_chats_for_user(current_user.id)
    return chats
