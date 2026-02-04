from fastapi import WebSocket
from sqlalchemy.orm import Session
from src.auth.service import AuthService
from src.database.core import SessionLocal
from src.users.repository import UserRepository
from src.users.models import User


async def get_current_user_ws(websocket: WebSocket) -> User:
    token = websocket.query_params.get("token")
    if not token:
        await websocket.close(code=1008)
        raise RuntimeError("Missing token")

    db: Session = SessionLocal()
    try:
        auth_service = AuthService(db)
        user_id = auth_service.decode_access_token(token)
        if not user_id:
            await websocket.close(code=1008)
            raise RuntimeError("Invalid token")

        user = UserRepository(db).get_by_id(user_id)
        if not user:
            await websocket.close(code=1008)
            raise RuntimeError("User not found")

        return user
    except RuntimeError:
        await websocket.close(code=1008)
    finally:
        db.close()
