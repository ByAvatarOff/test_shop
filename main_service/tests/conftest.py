import pytest
from django.contrib.auth.models import User
from django.test.client import Client
from rest_framework.test import APIClient


@pytest.fixture
def get_user() -> User:
    user = User.objects.create_user(
        username='test_user',
        email='test_user@mail.ru',
        password='1234'
    )
    return user


@pytest.fixture
def auth_client(client: Client, get_user: User):
    response = client.post('/api/auth/token/', {'username': get_user.username, 'password': 1234})
    auth_client = APIClient()
    auth_client.credentials(HTTP_AUTHORIZATION=f'Bearer {response.data["access"]}')
    return auth_client
