from django.urls import path
from shop_service.views import ItemViewSet

app_name = 'shop_service'

urlpatterns = [
    path('items/', ItemViewSet.as_view({'get': 'get_list_items'}), name='get_list_items'),
    path('create_item/', ItemViewSet.as_view({'post': 'create_item'}), name='create_item'),
    path('get_item/<int:pk>/', ItemViewSet.as_view({'get': 'get_item'}), name='get_item'),
    path('update_item/<int:pk>/', ItemViewSet.as_view({'patch': 'update_item'}), name='update_item'),
    path('delete_item/<int:pk>/', ItemViewSet.as_view({'delete': 'delete_item'}), name='delete_item'),
    path('delete_items/', ItemViewSet.as_view({'delete': 'delete_all_items'}), name='delete_all_items'),
]
