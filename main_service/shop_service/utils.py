from typing import Callable

import httpx
from config import SHOP_SERVICE_URL
from httpx import Client, ConnectError, Response


class HttpxSession:
    """Create httpx client and return response from url"""

    @staticmethod
    def session_decorator(func: Callable) -> Callable:
        """create httpx sync session decorator"""
        def wrapper(*args, **kwargs):
            with httpx.Client(base_url=f'http://{SHOP_SERVICE_URL}:8001') as client:
                try:
                    return func(*args, client=client, **kwargs)
                except ConnectError:
                    return Response(status_code=400, json={'detail': 'Shop service is unavailable'})
        return wrapper

    @staticmethod
    @session_decorator
    def get(
            client: Client,
            url: str,
    ) -> Response:
        """custom get method use https"""
        return client.get(url)

    @staticmethod
    @session_decorator
    def post(
            client: Client,
            url: str,
            payload: dict
    ) -> Response:
        """custom post method use https"""
        return client.post(url, json=payload)

    @staticmethod
    @session_decorator
    def patch(
            client: Client,
            url: str,
            payload: dict
    ) -> Response:
        """custom patch method use https"""
        return client.patch(url, json=payload)

    @staticmethod
    @session_decorator
    def delete(
            client: Client,
            url: str,
    ) -> Response:
        """custom delete method use https"""
        return client.delete(url)
