from fastapi import APIRouter

from .schemas.user import User


router = APIRouter()

@router.get('/users')
async def get_users(args: User):
    return []


@router.post('/users/<user_id>')
async def create_user(args: User):
    return {}


@router.post('/users/<user_id>')
async def edit_user(args: User):
    return {}


@router.post('/users/<user_id>')
async def delete_user(args: User):
    return []
