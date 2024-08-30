from typing import Annotated

from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, APIRouter

from auth.scheme import TokenOut
from auth.services import authenticate_user, jwt_code
from auth.scheme import UserScheme

from auth.error import get_error_user_not_authenticate

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
