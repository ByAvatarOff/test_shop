from shop_service.utils import HttpxSession


class ItemService:
    """Item service for get data from shop microservice"""

    @staticmethod
    def get_list_items() -> dict:
        """Get list items"""
        return HttpxSession.get(
            url='api/items',
        )

    @staticmethod
    def get_item(item_id: int) -> dict:
        """Get item by id"""
        return HttpxSession.get(
            url=f'api/item/{item_id}',
        )

    @staticmethod
    def create_item(payload: dict) -> dict:
        """Create item"""
        return HttpxSession.post(
            url='api/item',
            payload=payload
        )

    @staticmethod
    def update_item(item_id: int, payload: dict) -> dict:
        """Update item by id"""
        return HttpxSession.patch(
            url=f'api/item/{item_id}',
            payload=payload
        )

    @staticmethod
    def delete_item(item_id: int) -> dict:
        """Delete item by id"""
        return HttpxSession.delete(
            url=f'api/item/{item_id}',
        )

    @staticmethod
    def delete_all_items() -> dict:
        """Delete all items"""
        return HttpxSession.delete(
            url='api/items',
        )
