from typing import Annotated

from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, APIRouter
from psycopg2 import IntegrityError

from auth.scheme import TokenOut, CreatedUserMessage, UserRegister
from auth.services import authenticate_user, jwt_code, get_user_by_username, hash_password, create_user
from auth.scheme import UserScheme

from auth.error import get_error_user_not_authenticate, get_error_user_in_db, get_error_user_not_create

auth_router = APIRouter(prefix="/security", tags=["Auth"])


@auth_router.post("/token")
async def new_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> TokenOut:
    user = UserScheme(username=form_data.username, password=form_data.password)
    get_user = await authenticate_user(user=user)
    if not get_user:
        raise get_error_user_not_authenticate()
    return jwt_code(user.username)


@auth_router.post("/register")
async def user_register(
    user: UserRegister
) -> CreatedUserMessage:
    try:
        user.password = hash_password(user.password)
        new_user = await create_user(user)
    except IntegrityError:
        raise get_error_user_not_create()
    if not new_user:
        raise get_error_user_in_db()
    return CreatedUserMessage()
