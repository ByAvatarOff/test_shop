"""Schemas for model Item"""
from datetime import datetime
from decimal import Decimal, InvalidOperation

from pydantic import BaseModel, field_validator


class ItemReadSchema(BaseModel):
    """Item read schema"""
    id: int
    title: str
    description: str
    price: Decimal
    origin_country: str
    date_add: datetime

    class Config:
        from_attributes = True


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
