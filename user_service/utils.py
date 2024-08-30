import aiopg
from config import settings


async def get_connection():
    dns = f"dbname={settings.P_DB} user={settings.P_USER} password={settings.P_PASS} host={settings.P_HOST} port={settings.P_PORT}"
    async with aiopg.connect(dns=dns) as connection:
        yield connection
