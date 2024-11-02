import asyncio
from app.database import engine
from app.core.base import Base
from app.core.loader import load_models_and_schemas

async def init_db():
    load_models_and_schemas()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == '__main__':
    asyncio.run(init_db())
