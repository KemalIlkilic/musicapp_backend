from sqlmodel import create_engine, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config
from src.db.models import User
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine, SQLModel

async_engine = AsyncEngine(
    create_engine(
        #setting to 3600 means connections will be recycled after one hour.
        pool_pre_ping=True,  # Ensure connections are valid before using #bu cozuyormus doc'a gore
        pool_recycle=3600,
        pool_timeout=30,
        url=Config.DATABASE_URL,
        #enable log output for this element.
        echo=True
    )
)

async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session() -> AsyncSession:
    Session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with Session() as session:
        yield session