from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from shop_service.item_service import ItemService


class ItemViewSet(ViewSet):
    permission_classes_by_action = {
        'get_list_items': [permissions.IsAuthenticated, ],
        'get_item': [permissions.IsAuthenticated, ],
        'create_item': [permissions.IsAuthenticated, ],
        'update_item': [permissions.IsAuthenticated, ],
        'delete_item': [permissions.IsAuthenticated, ],
        'delete_all_items': [permissions.IsAuthenticated, ],
    }

    def get_list_items(self, request: Request) -> Response:
        """Get list items"""
        return ItemService.get_list_items()

    def get_item(self, request: Request, pk: int) -> Response:
        """Get item by id"""
        return ItemService.get_item(item_id=pk)

    def create_item(self, request: Request) -> Response:
        """Create item"""
        return ItemService.create_item(request.data)

    def update_item(self, request: Request, pk: int) -> Response:
        """Update item by id"""
        return ItemService.update_item(item_id=pk, payload=request.data)

    def delete_item(self, request: Request, pk: int):
        """Delete item by id"""
        return ItemService.delete_item(item_id=pk)

    def delete_all_items(self, request: Request):
        """Delete all items"""
        return ItemService.delete_all_items()

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
