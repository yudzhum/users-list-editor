from contextlib import asynccontextmanager
from typing import Optional
from sqlalchemy.orm import DeclarativeBase
import asyncpg


class BaseDBModel(DeclarativeBase):
    pass


def _connection_init(conn):
    return conn


_pool: Optional[asyncpg.pool.Pool] = None


async def connect():
    global _pool

    if not _pool:
        _pool = await asyncpg.create_pool(
            init=_connection_init,
            host = 'localhost',
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

    await _pool.close()


@asynccontextmanager
async def get_connection():
    conn_pool = await connect()
    conn = await conn_pool.acquire()
    yield conn
    await conn_pool.release(conn)
