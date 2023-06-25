from contextlib import asynccontextmanager
from typing import AsyncIterator, Optional
from sqlalchemy.orm import DeclarativeBase
import asyncpg
import asyncio


class BaseDBModel(DeclarativeBase):
    pass


_pool: Optional[asyncpg.pool.Pool] = None
_pool_lock = None


def init_pool_lock():
    global _pool_lock
    _pool_lock = asyncio.Lock()


async def _connection_init(conn):
    return conn


async def connect():
    global _pool

    async with _pool_lock:
        if not _pool:
            _pool = await asyncpg.create_pool(
                init=_connection_init,
                host='localhost',
                port=5432,
                database='fastapitest',
                user='yudzhum',
                password='charbox',
                min_size=1,
                max_size=4,
            )

    return _pool


async def close():
    global _pool

    if not _pool:
        return

    async with _pool_lock:
        await _pool.close()


@asynccontextmanager
async def get_connection() -> AsyncIterator[asyncpg.connection.Connection]:
    conn_pool = await connect()
    conn = await conn_pool.acquire()
    yield conn
    await conn_pool.release(conn)
