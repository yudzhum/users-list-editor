import uvicorn

from user_db.routes import app


if __name__ == '__main__':
    uvicorn.run(app)
