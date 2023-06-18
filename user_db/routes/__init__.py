from fastapi import FastAPI, APIRouter

from . import users


app = FastAPI()

app.include_router(users.router)

