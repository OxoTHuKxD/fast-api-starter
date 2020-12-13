from fastapi import FastAPI

from src.integrations.db import DBClient
from src.integrations.sentry.sentry import setup_sentry
from src.routes import setup_routes


def bootstrap(app: FastAPI) -> None:
    @app.on_event("shutdown")
    async def shutdown() -> None:  # pylint: disable=W0612
        await DBClient.close()


def build_app() -> FastAPI:
    app = FastAPI()
    bootstrap(app)
    setup_routes(app)
    setup_sentry()

    return app
