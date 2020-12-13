import asyncio
import pytest
from _pytest.fixtures import SubRequest
from httpx import AsyncClient

from src import settings
from src.bootstrap import build_app
from src.di import get_connection
from src.integrations.db import DBClient


@pytest.fixture(scope="session")
def event_loop():
    """
    Создание объекта цикла событий по умолчанию для каждого тест-кейса.

    :return:
    """

    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture()
async def connection(request: SubRequest):
    """
    Получение асинхронного подключения к базе данных с откатом всех сделанных изменений.
    :param request:
    :return:
    """
    database = await DBClient.get_db()
    async with database.connection() as connection:
        async with connection.transaction(force_rollback=True) as transaction:
            if request.cls:
                request.cls.connection = connection
            yield connection


@pytest.fixture()
def app(event_loop, connection, request: SubRequest):
    """
    Получение приложения в рамках функциональных тестов с коннекшеном к бд, который откатывает транзакции после каждого
    теста
    :param event_loop:
    :param connection:
    :param request:
    :return:
    """

    def get_test_connection():
        return connection

    app = build_app()
    app.dependency_overrides[get_connection] = get_test_connection
    if request.cls:
        request.cls.app = app
    return app


@pytest.fixture()
def client(event_loop, app):
    """
    Получение асинхронного клиента для запросов в рамках функциональных тестов
    :return:
    """

    yield AsyncClient(app=app, base_url=settings.BASE_URL)
