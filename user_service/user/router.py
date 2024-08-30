from typing import Annotated

from fastapi import APIRouter, Body

from user.scheme import UserOut, UserScheme

from user.crud import get_user_by_username, create_user

user_crud_router = APIRouter(prefix="/user", tags=["User"])


@user_crud_router.get("/")
async def get_user_by_username_route(username: str) -> UserOut | None:
    user = await get_user_by_username(username)
    if not user:
        return None
    return user


@user_crud_router.post("/")
async def create_user_route(user: Annotated[UserScheme, Body]) -> int | None:
    if not await get_user_by_username(user.username):
        user_id = await create_user(user)
        return user_id
    return None
