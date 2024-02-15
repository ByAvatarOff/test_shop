from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('jwt_auth.api.urls')),
    path('api/shop/', include('shop_service.urls')),
]
