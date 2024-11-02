from contextlib import asynccontextmanager
from app.database import async_session

@asynccontextmanager
async def transaction():
    async with async_session() as session:
        async with session.begin():
            yield session
