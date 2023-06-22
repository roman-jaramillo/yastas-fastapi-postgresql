import asyncio
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient

from app.db.session import async_session
from app.main import app


@pytest.fixture(scope="session")
async def db(event_loop) -> AsyncGenerator:
    async with async_session() as session:
        yield session


@pytest.fixture(scope="module")
async def client(event_loop) -> AsyncGenerator:
    async with AsyncClient(app=app, base_url="http://test") as c:
        yield c


@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
