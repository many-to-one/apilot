from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

# Tworzymy async engine
engine = create_async_engine(
    settings.POSTGRES_URL,
    echo=False,           # ustaw na True jeśli chcesz logi SQL
    future=True
)

# Fabryka sesji
async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependency dla FastAPI
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
