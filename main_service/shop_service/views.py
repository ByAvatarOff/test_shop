from rest_framework import permissions, status
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
        list_items = ItemService.get_list_items()
        return Response(status=status.HTTP_200_OK, data=list_items)

    def get_item(self, request: Request, pk: int) -> Response:
        """Get item by id"""
        item = ItemService.get_item(item_id=pk)
        return Response(data=item)

    def create_item(self, request: Request) -> Response:
        """Create item"""
        created_item = ItemService.create_item(request.data)
        return Response(data=created_item)

    def update_item(self, request: Request, pk: int) -> Response:
        """Update item by id"""
        updated_item = ItemService.update_item(item_id=pk, payload=request.data)
        return Response(data=updated_item)

    def delete_item(self, request: Request, pk: int):
        """Delete item by id"""
        response = ItemService.delete_item(item_id=pk)
        return Response(data=response)

    def delete_all_items(self, request: Request):
        """Delete all items"""
        response = ItemService.delete_all_items()
        return Response(data=response)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
