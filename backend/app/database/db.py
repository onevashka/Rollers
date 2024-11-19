from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base, DeclarativeBase
from backend.app.config_backed import DB_URL


Base: DeclarativeBase = declarative_base()

engine = create_async_engine(url=DB_URL)
session_marker = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_session():
    try:
        session = session_marker()
        yield session
    except Exception as e:
        print(f"Error occurred while getting session: {e}")