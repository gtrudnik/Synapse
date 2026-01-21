from fastapi import APIRouter, Depends

from src.users.router import router as users_router


api_router = APIRouter()
authenticated_api_router = APIRouter()

api_router.include_router(users_router, prefix="/users", tags=["users"])


@api_router.get("/healthcheck", include_in_schema=False)
def healthcheck():
    """Simple healthcheck endpoint."""
    return {"status": "ok"}

