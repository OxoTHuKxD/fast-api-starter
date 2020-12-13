from typing import Optional

from databases import Database

from src import settings


class DBClient:
    """
    Управление подключением к базе данных.
    """

    _database: Optional[Database] = None

    @classmethod
    async def get_db(cls, force_rollback: bool = False) -> Database:
        """
        Получение асинхронного подключения к базе данных.

        :param force_rollback: Принудительный откат изменений
        :return:
        """

        if not cls._database:
            cls._database = Database(settings.DB_DSN, force_rollback=force_rollback)
            await cls._database.connect()
        return cls._database

    @classmethod
    async def close(cls) -> None:
        """
        Закрытие подключения.

        :return:
        """
        if cls._database:
            await cls._database.disconnect()

    @classmethod
    async def select_1(cls) -> None:
        """
        Проверка подключения.

        :return:
        """
        data_base = await cls.get_db()
        await data_base.fetch_one("SELECT 1")
