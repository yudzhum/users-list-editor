from fastapi import APIRouter

from .schemas.user import UserCreateOrUpdate
from user_db.db import get_connection

router = APIRouter()

@router.get('/users/')
async def get_users():
    query = """
        SELECT * FROM users
    """
    async with get_connection() as conn:
        users = await conn.fetch(query)
        # place for serializer, shoud be function
        return map(lambda user: ({
            'id': user['id'],
            'name': user['name'],
            'group': user['group'],
        }), users)


@router.post('/users/')
async def create_user(args: UserCreateOrUpdate):
    query = """
        INSERT INTO users(name, password_hash, salt, "group")
        VALUES ($1, $2, $3)
    """
    async with get_connection() as conn:
        return await conn.fetch(
            query,
            args.name,
            args.password,
            args.group
        )


@router.post('/users/{user_id}')
async def edit_user(user_id: int, args: UserCreateOrUpdate):
    query = """
        UPDATE users SET name=$2, password_hash=$3, "group"=$4
        WHERE users.id = $1
    """
    async with get_connection() as conn:
        return await conn.fetch(
            query,
            user_id,
            args.name,
            args.password,
            args.group
        )


@router.delete('/users/{user_id}')
async def delete_user(user_id: int):
    query = """
        DELETE FROM users
        WHERE users.id = $1
    """
    async with get_connection() as conn:
        return await conn.fetch(
            query,
            user_id,
        )
