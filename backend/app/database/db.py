from app.config_backed import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USERNAME
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base, DeclarativeBase


DB_URL = f'postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


Base: DeclarativeBase = declarative_base()

engine = create_async_engine(url=DB_URL)
session_marker = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)


async def get_session():
    async with session_marker() as session:
        try:
            yield session
        except Exception as e:
            raise e