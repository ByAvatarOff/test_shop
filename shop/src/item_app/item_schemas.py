"""Schemas for model Item"""
from datetime import datetime
from decimal import Decimal, InvalidOperation

from pydantic import BaseModel, ConfigDict, field_serializer, field_validator


class ItemReadSchema(BaseModel):
    """Item read schema"""
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str
    price: Decimal
    origin_country: str
    date_add: datetime

    @field_serializer('price')
    def convert_to_2_decimal_places(self, price):
        """
        Serialize price for input
        Only two decimal_places
        """
        try:
            return f'{Decimal(price):.2f}'
        except InvalidOperation:
            raise ValueError('Invalid type price')


class ItemCreateSchema(BaseModel):
    """Item schema for creating item instance"""
    title: str
    description: str
    price: Decimal
    origin_country: str

    @field_validator('price')
    @classmethod
    def check_if_decimal_price(cls, value):
        """
        Validator check decimal value on field price
        If not raise ValueError
        """
        try:
            assert Decimal(value)
            return value
        except InvalidOperation:
            raise ValueError('You must get float price')
