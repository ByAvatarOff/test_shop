"""
Pytest fixtures
"""
from typing import AsyncGenerator

import pytest
from conftest import async_session_maker, engine_test
from httpx import AsyncClient
from item_app.item_models import Base, Item
from item_app.item_schemas import ItemReadSchema
from main import app
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.fixture
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """Get async session use async session maker"""
    async with async_session_maker() as session:
        yield session


@pytest.fixture(autouse=True, scope='session')
async def prepare_database() -> AsyncGenerator:
    """
    Create tables after connect to database
    Drop tables before end tests
    """
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope='session')
async def ac() -> AsyncGenerator[AsyncClient, None]:
    """Return async generator async client"""
    async with AsyncClient(app=app, base_url='http://test') as ac:
        yield ac


@pytest.fixture
async def get_item_instance(
        get_async_session: AsyncSession
):
    """
    Select Item first instance if exists
    Else create item instance
    Return item instance
    """
    stmt = select(Item)
    record = await get_async_session.execute(stmt)
    item = record.scalars().first()
    if item:
        return item
    stmt = (
        insert(Item)
        .values(
            title='item test title',
            description='item test description',
            price=122.67,
            origin_country='Belarus'
        )
        .returning(Item))
    record = await get_async_session.execute(stmt)
    await get_async_session.commit()
    return record.scalars().first()


@pytest.fixture
async def get_item_id(
        get_item_instance: ItemReadSchema
) -> int:
    """Get from item instance item id"""
    return get_item_instance.id
