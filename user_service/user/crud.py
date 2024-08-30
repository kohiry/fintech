from typing import Optional

from user.scheme import UserOut
from utils import db


async def create_user(username: str, amount: float) -> int:
    async with db.get_connection() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute(
                "INSERT INTO users (username, amount) VALUES (%s, %s) RETURNING id;",
                (username, amount)
            )
            user_id = await cursor.fetchone()
            await conn.commit()
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
                username=user_db.username,
                id=user_db.id,
                hashed_password=user_db.hashed_password,
            )
            return user


async def update_user(user_id: int, username: str, amount: float):
    async with db.get_connection() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute(
                "UPDATE users SET username = %s, amount = %s WHERE id = %s;",
                (username, amount, user_id)
            )
            await conn.commit()


async def delete_user(user_id: int):
    async with db.get_connection() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("DELETE FROM users WHERE id = %s;", (user_id,))
            await conn.commit()
