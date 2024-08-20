import os

import uvicorn
from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles

from .dependencies import get_db
from .meta import meta
from .routers import items, users

app = FastAPI(
    contact={
        "name": "John Doe",
        "url": "https://example.com",
        "email": "johndoe@example.com",
    },
    dependencies=[Depends(get_db)],
    description=meta.description,
    openapi_tags=meta.tags_metadata,
    summary="A Generic App",
    terms_of_service="https://example.com/terms/",
    title="App",
    version="0.0.1",
)

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
