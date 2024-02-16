import pytest
from django.contrib.auth.models import User
from django.test.client import Client


@pytest.mark.django_db
def test_get_list_items_success(auth_client: Client, get_user: User) -> None:
    response = auth_client.get('/api/shop/items/')
    data = response.data
    assert isinstance(data, list)


@pytest.mark.django_db
def test_get_list_items_failed(client: Client) -> None:
    response = client.get('/api/shop/items/')
    assert response.status_code == 403
