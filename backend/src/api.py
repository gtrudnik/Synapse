from fastapi import APIRouter, Depends

from src.auth.dependencies import get_current_user
from src.users.router import router as users_router
from src.auth.router import router as auth_router
from src.cards.router import router as card_router
from src.chat.router import router as chat_router
from src.meetings.router import router as meeting_router
from src.matches.router import router as matches_router


api_router = APIRouter()
authenticated_api_router = APIRouter()

api_router.include_router(chat_router, prefix="/chats", tags=["chats"])
api_router.include_router(users_router, prefix="/users", tags=["users"])
api_router.include_router(auth_router, prefix="/auth", tags=["auth"])

authenticated_api_router.include_router(card_router, prefix="/cards", tags=["cards"])
authenticated_api_router.include_router(
    meeting_router, prefix="/meetings", tags=["meetings"]
)
authenticated_api_router.include_router(
    matches_router, prefix="/matches", tags=["matches"]
)


api_router.include_router(
    authenticated_api_router, dependencies=[Depends(get_current_user)]
)


@api_router.get("/healthcheck", include_in_schema=False)
def healthcheck():
    """Simple healthcheck endpoint."""
    return {"status": "ok"}
