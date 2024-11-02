from pathlib import Path
from dotenv import load_dotenv
from pydantic import BaseModel, PostgresDsn, field_validator
import os
import secrets

# 自动加载 .env 文件
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

class Settings(BaseModel):
    # 数据库配置，优先使用单一 `DATABASE_URL`，否则动态生成
    DATABASE_URL: PostgresDsn | None = os.getenv("DATABASE_URL")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "yourpassword")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "yourdatabase")

    # JWT 配置
    SECRET_KEY: str = os.getenv("SECRET_KEY", secrets.token_urlsafe(32))
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    # Redis 配置
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", 6379))

    @field_validator("DATABASE_URL", mode="before")
    def assemble_db_connection(cls, v, values):
        """如果 `DATABASE_URL` 未定义，则动态生成它"""
        return v or PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=values["POSTGRES_USER"],
            password=values["POSTGRES_PASSWORD"],
            host=values["POSTGRES_HOST"],
            port=values["POSTGRES_PORT"],
            path=f"/{values['POSTGRES_DB']}",
        )

    class Config:
        extra = "ignore"  # 忽略未定义的环境变量

settings = Settings()



# import os
# from dotenv import load_dotenv

# load_dotenv()

# class Settings:
#     POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
#     POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "password")
#     POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
#     POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT", 5432))
#     POSTGRES_DB: str = os.getenv("POSTGRES_DB", "yourdatabase")
#     SECRET_KEY: str = os.getenv("SECRET_KEY", "your_secret_key")
#     REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
#     REDIS_PORT: int = int(os.getenv("REDIS_PORT", 6379))

# settings = Settings()
