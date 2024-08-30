from fastapi import APIRouter

from user.scheme import UserOut

from user.crud import get_user_by_username

user_crud_router = APIRouter(prefix="/user", tags=["User"])


@user_crud_router.get("/")
async def get_user_by_username_route(username: str) -> UserOut | None:
    user = await get_user_by_username(username)
    if not user:
        return None
    return user
