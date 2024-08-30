from contextlib import asynccontextmanager
from typing import Optional

import aiopg
from config import settings


class Database:
    def __init__(self):
        self.dsn = (
            f"dbname={settings.P_DB} user={settings.P_USER} password={settings.P_PASS} "
            f"host={settings.P_HOST} port={settings.P_PORT}"
        )
        self.pool: Optional[aiopg.Pool] = None

    async def init_pool(self):
        self.pool = await aiopg.create_pool(dsn=self.dsn)

    @asynccontextmanager
    async def get_connection(self):
        await self.init_pool()
        async with self.pool.acquire() as conn:
            yield conn


db = Database()
