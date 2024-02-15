from django.contrib.auth.models import User
from jwt_auth.api.serializers import RetrieveUserSerializer
from rest_framework.exceptions import NotFound


class UserService:
    """Service for user actions"""

    def get_user(self, user_id: int) -> NotFound | RetrieveUserSerializer:
        """get user by user id"""
        try:
            user = User.objects.get(id=user_id)
            serializer = RetrieveUserSerializer(user)
            return serializer.data
        except User.DoesNotExist:
            raise NotFound(detail='User not found')
