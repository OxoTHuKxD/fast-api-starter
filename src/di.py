from typing import AsyncGenerator

from src.integrations.db import DBClient


# Dependency
async def get_connection() -> AsyncGenerator:
    database = await DBClient.get_db()
    async with database.connection() as connection:
        yield connection
