import os

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker
)

from app.config import DATABASE_URL


# создаем папку для SQLite
if DATABASE_URL.startswith("sqlite"):

    os.makedirs(
        "data",
        exist_ok=True
    )



engine = create_async_engine(
    DATABASE_URL,
    echo=False
)



SessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False
)



from app.database.models import Base



async def init_db():

    async with engine.begin() as conn:

        await conn.run_sync(
            Base.metadata.create_all
        )