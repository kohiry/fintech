import aiopg
from config import settings

dns = (
    f"dbname={settings.P_DB} user={settings.P_USER} password={settings.P_PASS} "
    f"host={settings.P_HOST} port={settings.P_PORT}"
)


async def get_connection():
    async with aiopg.connect(dns=dns) as connection:
        yield connection
