import pytest
from django.contrib.auth.models import User
from django.test.client import Client


@pytest.mark.django_db
def test_register_user_success(client: Client) -> None:
    payload = {
        'username': 'test_user',
        'email': 'test_user@mail.ru',
        'password': '1234',
        'repeat_password': '1234',

    }
    response = client.post('/api/auth/register/', payload)
    data = response.data
    assert data['username'] == 'test_user'
    assert data['id'] == 1
    assert isinstance(data['password'], str)


@pytest.mark.django_db
def test_register_user_failed(client: Client) -> None:
    payload = {
        'username': 'test_user',
    }
    response = client.post('/api/auth/register/', payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_login_user_success(client: Client, get_user: User) -> None:
    response = client.post('/api/auth/token/', {'username': get_user.username, 'password': 1234})
    data = response.data
    assert isinstance(data['access'], str)
    assert isinstance(data['refresh'], str)


@pytest.mark.django_db
def test_login_user_failed(client: Client) -> None:
    response = client.post('/api/auth/token/', {'username': 'fake_user', 'password': 1234})
    assert response.status_code == 401


@pytest.mark.django_db
def test_get_user_info_success(auth_client: Client, get_user: User) -> None:
    response = auth_client.get('/api/auth/user/')
    data = response.data
    assert data['username'] == get_user.username
    assert data['email'] == get_user.email


@pytest.mark.django_db
def test_get_user_info_failed(client: Client, get_user: User) -> None:
    response = client.get('/api/auth/user/')
    assert response.status_code == 403
