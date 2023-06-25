from ast import List
from fastapi import APIRouter

from user_db.lib.hash import generate_password_hash

from .schemas.user import UserCreateOrUpdate, UserOut
from user_db.db import get_connection

router = APIRouter()

@router.get('/users/', response_model=List[UserOut])
async def get_users():
    query = """
        SELECT * FROM users
    """
    async with get_connection() as conn:
        users = await conn.fetch(query)
        return [UserOut(**user) for user in users]


@router.post('/users/')
async def create_user(args: UserCreateOrUpdate):
    query = """
        INSERT INTO users(name, password_hash, salt, "group")
        VALUES ($1, $2, $3)
    """
    password_hash = generate_password_hash(args.password)
    async with get_connection() as conn:
        return await conn.fetch(
            query,
            args.name,
            password_hash,
            args.group
        )


@router.post('/users/{user_id}')
async def edit_user(user_id: int, args: UserCreateOrUpdate):
    query = """
        UPDATE users SET name=$2, password_hash=$3, "group"=$4
        WHERE users.id = $1
    """
    password_hash = generate_password_hash(args.password)
    async with get_connection() as conn:
        return await conn.fetch(
            query,
            user_id,
            args.name,
            password_hash,
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
