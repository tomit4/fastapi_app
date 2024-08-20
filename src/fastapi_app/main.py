import os

import uvicorn
from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles

from .dependencies import get_db
from .meta import meta
from .middlewares import cors
from .routers import items, users

app = FastAPI(
    **meta.meta_info,
    dependencies=[Depends(get_db)],
)

cors.add_cors_middleware(app)

app.mount("/public", StaticFiles(directory="public"), name="static")

load_dotenv()
HOST = os.environ.get("HOST") or "::"
PORT = int(str(os.environ.get("PORT"))) or 8000

app.include_router(users.router)
app.include_router(items.router)


def main():
    uvicorn.run(app, host=HOST, port=PORT)


if __name__ == "__main__":
    main()
