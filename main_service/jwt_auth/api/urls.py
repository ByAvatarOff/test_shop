from django.urls import path
from jwt_auth.api.views import RegisterAPIView, UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'accounts'

urlpatterns = [
    path('user/', UserViewSet.as_view({'get': 'get_user'}), name='get_user'),
    path('register/', RegisterAPIView.as_view(), name='register_user'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_view'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
