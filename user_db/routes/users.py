from fastapi import APIRouter

from .schemas.user import UserCreateOrUpdate
from user_db.db import get_connection

router = APIRouter()

@router.get('/users')
async def get_users():
    query = """
        SELECT * FROM users
    """
    async with get_connection() as conn:
        users = await conn.fetch()


@router.post('/users/')
async def create_user(args: UserCreateOrUpdate):
    return {}


@router.post('/users/{user_id}')
async def edit_user(user_id: int, args: UserCreateOrUpdate):
    return {}


@router.post('/users/{user_id}')
async def delete_user(usser_id: int):
    return []
