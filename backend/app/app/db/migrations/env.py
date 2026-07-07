from logging.config import fileConfig
from alembic import context
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import create_async_engine

from core.config import settings
from db.base import Base

# Alembic Config
config = context.config

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata
target_metadata = Base.metadata

# 🔥 Ustawiamy URL z Pydantic Settings
config.set_main_option("sqlalchemy.url", settings.POSTGRES_URL)


def run_migrations_online():
    """Run migrations in 'online' mode with async engine."""

    # 🔥 Poprawny sposób tworzenia async engine w SQLAlchemy 2.0
    connectable = create_async_engine(
        settings.POSTGRES_URL,
        poolclass=pool.NullPool,
        future=True,
    )

    async def do_migrations(connection: Connection):
        await connection.run_sync(target_metadata.create_all)

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            render_as_batch=True,
        )

        with context.begin_transaction():
            context.run_migrations()

    async def run():
        async with connectable.connect() as connection:
            await do_migrations(connection)

    import asyncio
    asyncio.run(run())


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
