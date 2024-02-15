from django.contrib.auth.models import User
from jwt_auth.api.serializers import UserRegisterSerializer
from jwt_auth.api.user_service import UserService
from rest_framework import generics, permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class RegisterAPIView(generics.CreateAPIView):
    """Api View for register user"""
    queryset = User
    serializer_class = UserRegisterSerializer


class UserViewSet(ViewSet):
    """ViewSet for view User entity"""
    permission_classes_by_action = {
        'get_user': [permissions.IsAuthenticated, ],
    }

    def get_user(
            self,
            request: Request,
            user_service: UserService = UserService()
    ) -> Response:
        """Get user by access token"""
        return Response(
            status=status.HTTP_200_OK,
            data=user_service.get_user(request.user.id)
        )

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
