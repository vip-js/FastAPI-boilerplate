from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.config import settings

# 创建异步引擎
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,
    future=True,
    pool_size=20,
    max_overflow=0,
)

# 创建异步会话工厂
async_session = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

async def get_db():
    async with async_session() as session:
        yield session

