"""Shop api routers"""

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from item_app.item_schemas import ItemCreateSchema, ItemReadSchema
from item_app.item_service import ItemService
from starlette import status

item_router = APIRouter(
    prefix='/api',
    tags=['Shop CRUD']
)


@item_router.get(
    '/items',
    status_code=status.HTTP_200_OK,
    response_model=list[ItemReadSchema],
)
async def list_items(
        item_service: ItemService = Depends()
) -> list[ItemReadSchema]:
    """List items"""
    return await item_service.get_all_items()


@item_router.post(
    '/item',
    status_code=status.HTTP_201_CREATED,
    response_model=ItemReadSchema,
)
async def create_item(
        payload: ItemCreateSchema,
        item_service: ItemService = Depends()
) -> ItemReadSchema:
    """Create item"""
    return await item_service.create_item(
        item_payload=payload,
    )


@item_router.get(
    '/item/{item_id}',
    status_code=status.HTTP_200_OK,
    response_model=ItemReadSchema,
)
async def get_item(
        item_id: int,
        item_service: ItemService = Depends()
) -> ItemReadSchema:
    """Get item by id"""
    return await item_service.get_item(
        item_id=item_id
    )


@item_router.patch(
    '/item/{item_id}',
    status_code=status.HTTP_200_OK,
    response_model=ItemReadSchema,
)
async def update_item(
        item_id: int,
        payload: ItemCreateSchema,
        item_service: ItemService = Depends()
) -> ItemReadSchema:
    """Update item by id"""
    return await item_service.update_item(
        item_id=item_id,
        item_payload=payload
    )


@item_router.delete(
    '/item/{item_id}',
    status_code=status.HTTP_200_OK,
)
async def delete_item(
        item_id: int,
        item_service: ItemService = Depends()
) -> JSONResponse:
    """Delete item by id"""
    return await item_service.delete_item(
        item_id=item_id,
    )


@item_router.delete(
    '/items',
    status_code=status.HTTP_200_OK,
)
async def delete_all_items(
        item_service: ItemService = Depends()
) -> JSONResponse:
    """Delete all items"""
    return await item_service.delete_all_items()
