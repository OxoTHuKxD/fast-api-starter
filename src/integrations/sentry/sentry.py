import sentry_sdk

from src import settings


def setup_sentry() -> None:
    """
    Настройка логирования в Sentry.

    :return:
    """
    if settings.SENTRY_DSN and settings.ENVIRONMENT not in settings.IGNORE_ENVIRONMENT_LIST:
        sentry_sdk.init(dsn=settings.SENTRY_DSN, environment=settings.ENVIRONMENT, traces_sample_rate=1.0)


def capture_exception(exception: Exception) -> None:
    """
    Обработка сохранения ошибки в сентри

    :param exception:
    :return:
    """
    if settings.SENTRY_DSN and settings.ENVIRONMENT not in settings.IGNORE_ENVIRONMENT_LIST:
        sentry_sdk.capture_exception(exception)
