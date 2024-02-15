from typing import Callable

import httpx
from config import SHOP_SERVICE_URL
from httpx import Client, ConnectError


class HttpxSession:
    """Create httpx client and return json response from url"""

    @staticmethod
    def session_decorator(func: Callable) -> Callable:
        """create httpx sync session decorator"""
        def wrapper(*args, **kwargs):
            with httpx.Client(base_url=SHOP_SERVICE_URL) as client:
                try:
                    return func(*args, client=client, **kwargs)
                except ConnectError:
                    return []
        return wrapper

    @staticmethod
    @session_decorator
    def get(
            client: Client,
            url: str,
    ) -> dict:
        """custom get method use https"""
        return client.get(url).json()

    @staticmethod
    @session_decorator
    def post(
            client: Client,
            url: str,
            payload: dict
    ) -> dict:
        """custom post method use https"""
        return client.post(url, json=payload).json()

    @staticmethod
    @session_decorator
    def patch(
            client: Client,
            url: str,
            payload: dict
    ) -> dict:
        """custom patch method use https"""
        return client.patch(url, json=payload).json()

    @staticmethod
    @session_decorator
    def delete(
            client: Client,
            url: str,
    ) -> dict:
        """custom delete method use https"""
        return client.delete(url).json()
