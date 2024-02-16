from rest_framework.response import Response
from shop_service.utils import HttpxSession


class ItemService:
    """Item service for get data from shop microservice"""

    @staticmethod
    def get_list_items() -> Response:
        """Get list items"""
        response = HttpxSession.get(
            url='api/items',
        )
        return Response(status=response.status_code, data=response.json())

    @staticmethod
    def get_item(item_id: int) -> Response:
        """Get item by id"""
        response = HttpxSession.get(
            url=f'api/item/{item_id}',
        )
        return Response(status=response.status_code, data=response.json())

    @staticmethod
    def create_item(payload: dict) -> Response:
        """Create item"""
        response = HttpxSession.post(
            url='api/item',
            payload=payload
        )
        return Response(status=response.status_code, data=response.json())

    @staticmethod
    def update_item(item_id: int, payload: dict) -> Response:
        """Update item by id"""
        response = HttpxSession.patch(
            url=f'api/item/{item_id}',
            payload=payload
        )
        return Response(status=response.status_code, data=response.json())

    @staticmethod
    def delete_item(item_id: int) -> Response:
        """Delete item by id"""
        response = HttpxSession.delete(
            url=f'api/item/{item_id}',
        )
        return Response(status=response.status_code, data=response.json())

    @staticmethod
    def delete_all_items() -> Response:
        """Delete all items"""
        response = HttpxSession.delete(
            url='api/items',
        )
        return Response(status=response.status_code, data=response.json())
