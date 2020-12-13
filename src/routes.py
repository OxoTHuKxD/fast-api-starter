from fastapi import FastAPI

from src.transport.handlers import dummy


def setup_routes(app: FastAPI) -> None:
    app.include_router(
        dummy.router,
        prefix="/dummy",
    )
