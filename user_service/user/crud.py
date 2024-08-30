from typing import Optional

from user.scheme import UserOut, UserScheme
from utils import db


async def create_user(user: UserScheme) -> int:
    async with db.get_connection() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute(
                "INSERT INTO users (username, amount, hashed_password) VALUES (%s, %s, %s) RETURNING id;",
                (user.username, user.amount, user.password)
            )
            user_id = await cursor.fetchone()
    return user_id[0]


async def get_user(user_id: int) -> Optional[dict]:
    async with db.get_connection() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * FROM users WHERE id = %s;", (user_id,))
    return await cursor.fetchone()


async def get_user_by_username(username: str) -> UserOut | None:
    async with db.get_connection() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * FROM users WHERE username = %s;", (username,))
            user_db = await cursor.fetchone()
            if not user_db:
                return None
            user = UserOut(
                username=user_db[1],
                id=user_db[0],
                hashed_password=user_db[3],
            )
    return user


async def update_user(user_id: int, username: str, amount: float):
    async with db.get_connection() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute(
                "UPDATE users SET username = %s, amount = %s WHERE id = %s;",
                (username, amount, user_id)
            )


async def delete_user(user_id: int):
    async with db.get_connection() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("DELETE FROM users WHERE id = %s;", (user_id,))
