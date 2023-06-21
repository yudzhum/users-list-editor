from fastapi import FastAPI, APIRouter

from . import users, auth


app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)

