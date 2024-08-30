from datetime import timezone, datetime, timedelta
from typing import Annotated

import httpx
from fastapi import Depends
from jose import jwt
from sqlalchemy.ext.asyncio import AsyncSession

from auth.scheme import TokenIn, TokenOut
from config import settings
from auth.constants import oauth2_scheme

from auth.scheme import UserOut

from auth.scheme import UserScheme

from auth.constants import pwd_context


def jwt_code(username: str) -> TokenOut:
    dict_present = TokenIn(
        sub=username,
        exp=datetime.now(timezone.utc)
        + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    jwt_token = jwt.encode(
        dict_present.model_dump(), settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return TokenOut(access_token=jwt_token)


def jwt_decode(token: str) -> TokenIn:
    dict_presents = jwt.decode(
        token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
    )
    return TokenIn.model_validate(dict_presents)


async def get_user_by_username(username: str) -> UserOut | None:
    url = "http://localhost:8080/user"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Проверка на ошибки HTTP
        user_data = UserOut.model_validate(response.json())
        print('Данные из UserService', user_data)
        return user_data


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
) -> UserOut:
    decode_token = jwt_decode(token)
    user = await get_user_by_username(decode_token.sub)
    return UserOut(**user.model_dump())


async def authenticate_user(user: UserScheme) -> UserOut | bool:
    get_user = await get_user_by_username(user.username)
    if get_user is None:
        return False
    if not compare_password(user.password, get_user.hashed_password):
        return False
    return get_user


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def compare_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)