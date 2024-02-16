from httpx import AsyncClient
from item_app.item_models import Item
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession


async def test_list_items_success(
        ac: AsyncClient,
) -> None:
    response = await ac.get('api/items')
    assert response.status_code == 200
    assert isinstance(response.json(), list)


async def test_create_item_success(
        ac: AsyncClient,
        get_async_session: AsyncSession
) -> None:
    response = await ac.post('api/item', json={
        'title': 'item title',
        'description': 'item description',
        'price': '12.67',
        'origin_country': 'Belarus'
    })
    assert response.status_code == 201
    data = response.json()
    assert data['title'] == 'item title'
    assert data['description'] == 'item description'
    assert data['price'] == '12.67'
    assert data['origin_country'] == 'Belarus'

    stmt = delete(Item).where(Item.id == data['id'])
    await get_async_session.execute(stmt)
    await get_async_session.commit()


async def test_create_item_failed(
        ac: AsyncClient,
) -> None:
    response = await ac.post('api/item', json={
        'title': 'item title',
        'price': 12.67,
    })
    assert response.status_code == 422


async def test_get_item_success(
        ac: AsyncClient,
        get_item_id: int
) -> None:
    response = await ac.get(f'api/item/{get_item_id}')
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == get_item_id
    assert data['title'] == 'item test title'
    assert data['description'] == 'item test description'
    assert data['price'] == '122.67'


async def test_get_item_failed(
        ac: AsyncClient,
) -> None:
    response = await ac.get('api/item/0')
    assert response.status_code == 404


async def test_update_item_success(
        ac: AsyncClient,
        get_item_id: int
) -> None:
    response = await ac.patch(f'api/item/{get_item_id}', json={
        'title': 'new item title',
        'description': 'new item description',
        'price': '14.67',
        'origin_country': 'Belarus'

    })
    assert response.status_code == 200
    data = response.json()
    assert data['title'] == 'new item title'
    assert data['description'] == 'new item description'
    assert data['price'] == '14.67'
    assert data['origin_country'] == 'Belarus'


async def test_update_item_failed(
        ac: AsyncClient,
        get_item_id: int
) -> None:
    response = await ac.patch(f'api/item/{get_item_id}', json={
        'title': 'new item title',
        'price': '14.6fsd7',

    })
    assert response.status_code == 422


async def test_delete_item_failed(
        ac: AsyncClient,
) -> None:
    response = await ac.delete('api/item/0')
    assert response.status_code == 404


async def test_delete_item_success(
        ac: AsyncClient,
        get_item_id: int
) -> None:
    response = await ac.delete(f'api/item/{get_item_id}')
    assert response.status_code == 200


async def test_delete_list_items_success(
        ac: AsyncClient,
        get_item_instance,
        get_async_session: AsyncSession
) -> None:
    stmt = select(Item)
    records = await get_async_session.execute(stmt)
    assert len(records.scalars().all()) == 1

    response = await ac.delete('api/items')
    assert response.status_code == 200

    stmt = select(Item)
    records = await get_async_session.execute(stmt)
    assert len(records.scalars().all()) == 0
