import uvicorn

from user_db. db import init_pool_lock
from user_db.routes import app


if __name__ == '__main__':
    init_pool_lock()
    uvicorn.run(app)
