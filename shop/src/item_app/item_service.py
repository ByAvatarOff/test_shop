"""Item service layer"""
from fastapi import Depends
from item_app.item_repo import ItemRepository
from item_app.item_schemas import ItemCreateSchema, ItemReadSchema
from starlette.responses import JSONResponse


class ItemService:
    """Service for item"""

    def __init__(
            self,
            item_repo: ItemRepository = Depends(),
    ) -> None:
        self.item_repo = item_repo

    async def get_all_items(
            self
    ) -> list[ItemReadSchema]:
        """Get list menu"""
        list_items = await self.item_repo.get_all_menus()
        return [
            ItemReadSchema.model_validate(item)
            for item in list_items
        ]

    async def create_item(
            self,
            item_payload: ItemCreateSchema,
    ) -> ItemReadSchema:
        """Create menu"""
        return ItemReadSchema.model_validate(
            await self.item_repo.create_item(
                item_payload=item_payload
            )
        )

    async def get_item(
            self,
            item_id: int
    ) -> ItemReadSchema:
        """Get item by id"""
        return ItemReadSchema.model_validate(
            await self.item_repo.get_item(
                item_id=item_id
            )
        )

    async def update_item(
            self,
            item_id: int,
            item_payload: ItemCreateSchema,
    ) -> ItemReadSchema:
        """Update menu by id"""
        return ItemReadSchema.model_validate(
            await self.item_repo.update_item(
                item_id=item_id,
                item_payload=item_payload
            )
        )

    async def delete_item(
            self,
            item_id: int,
    ) -> JSONResponse:
        """Delete item by id"""
        return await self.item_repo.delete_item(
            item_id=item_id
        )

    async def delete_all_items(
            self,
    ) -> JSONResponse:
        """Delete all items"""
        return await self.item_repo.delete_all_item()
