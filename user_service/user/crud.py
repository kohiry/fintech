from typing import Optional

from user_service.user.scheme import UserOut
from user_service.utils import get_connection


async def create_user(username: str, amount: float) -> int:
    conn = await get_connection()
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(
                "INSERT INTO users (username, amount) VALUES (%s, %s) RETURNING id;",
                (username, amount)
            )
            user_id = await cursor.fetchone()
            await conn.commit()
            return user_id[0]
    finally:
        conn.close()


async def get_user(user_id: int) -> Optional[dict]:
    conn = await get_connection()
    try:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * FROM users WHERE id = %s;", (user_id,))
            return await cursor.fetchone()
    finally:
        conn.close()


async def get_user_by_username(username: str) -> UserOut:
    conn = await get_connection()
    try:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * FROM users WHERE username = %s;", (username,))
            user_db = await cursor.fetchone()
            user = UserOut(
                username=user_db.username,
                id=user_db.id,
                hashed_password=user_db.hashed_password,
            )
            return user
    finally:
        conn.close()

async def update_user(user_id: int, username: str, amount: float):
    conn = await get_connection()
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(
                "UPDATE users SET username = %s, amount = %s WHERE id = %s;",
                (username, amount, user_id)
            )
            await conn.commit()
    finally:
        conn.close()


async def delete_user(user_id: int):
    conn = await get_connection()
    try:
        async with conn.cursor() as cursor:
            await cursor.execute("DELETE FROM users WHERE id = %s;", (user_id,))
            await conn.commit()
    finally:
        conn.close()
