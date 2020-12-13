import os
from typing import List
from typing import Optional

ENVIRONMENT: Optional[str] = os.getenv("ENVIRONMENT", "dev")
BASE_URL: str = os.getenv("BASE_URL", "http://127.0.0.1:8001")
DB_DSN: str = os.getenv("DB_DSN", "postgresql://exness_test:password@localhost:6432/exness_test")

# Sentry
SENTRY_DSN: Optional[str] = os.getenv("SENTRY_DSN")
IGNORE_ENVIRONMENT_LIST: List[str] = ["test"]
