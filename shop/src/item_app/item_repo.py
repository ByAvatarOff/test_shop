"""item Repository"""
from typing import Sequence

from db.db_config import get_async_session
from fastapi import Depends, HTTPException, status
from fastapi.responses import JSONResponse
from item_app.item_models import Item
from item_app.item_schemas import ItemCreateSchema, ItemReadSchema
from sqlalchemy import Row, delete, insert, select, update
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession


class ItemRepository:
    """Repository for item queries"""

    def __init__(
            self,
            session: AsyncSession = Depends(get_async_session),

    ) -> None:
        self.session = session

    async def if_item_exists(self, item_id: int) -> Row:
        """Check if item exists with get item_id"""
        record: Result = await self.session.execute(
            select(Item).where(Item.id == item_id)
        )
        result = record.scalars().first()
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='item not found'
            )
        return result

    async def get_all_menus(
            self
    ) -> Sequence[Row]:
        """List items"""
        return (
            await self.session.execute(
                select(Item).order_by(Item.id)
            )
        ).scalars().all()

    async def create_item(
            self,
            item_payload: ItemCreateSchema
    ) -> ItemCreateSchema:
        """Create new item"""
        result: Result = await self.session.execute(
            insert(Item)
            .values(
                item_payload.model_dump()
            )
            .returning(Item)
        )
        await self.session.commit()
        return result.scalars().first()

    async def get_item(
            self,
            item_id: int
    ) -> Row:
        """Get item by id"""
        return await self.if_item_exists(
            item_id=item_id
        )

    async def update_item(
            self,
            item_id: int,
            item_payload: ItemCreateSchema
    ) -> ItemReadSchema:
        """Update item bu id"""
        await self.if_item_exists(item_id=item_id)

        result: Result = await self.session.execute(
            update(Item)
            .where(
                Item.id == item_id
            )
            .values(item_payload.model_dump())
            .returning(Item)
        )
        await self.session.commit()
        return result.scalars().first()

    async def delete_item(
            self,
            item_id: int
    ) -> JSONResponse:
        """Delete item by id"""
        await self.if_item_exists(item_id=item_id)

        await self.session.execute(
            delete(Item)
            .where(
                Item.id == item_id
            )
        )
        await self.session.commit()
        return JSONResponse(
            content={'message': 'Success item delete'}
        )

    async def delete_all_item(
            self,
    ) -> JSONResponse:
        """Delete all items"""
        await self.session.execute(delete(Item))
        await self.session.commit()
        return JSONResponse(
            content={'message': 'Success all items delete'}
        )
