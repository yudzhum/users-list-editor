from fastapi import APIRouter, HTTPException

from user_db.routes.schemas.auth import LoginSchema
from user_db.db import get_connection


router = APIRouter()


@router.post('/login')
async def login(args: LoginSchema):
    query = """
        SELECT password FROM users
        WHERE name=$1
    """
    async with get_connection() as conn:
        user = await conn.fetchrow(query, args.name)
    if not user:
        raise HTTPException(
            404,
            'User not found'
        )
    if user['password'] == args.password:
        return True
    
    return False


