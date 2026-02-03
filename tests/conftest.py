import os

import pytest


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("REALTIME_BASE_URL", "https://example-realtime-app.test")


@pytest.fixture(scope="session")
def api_base_url() -> str:
    return os.getenv("REALTIME_API_BASE_URL", "https://api.realtime-app.test")
