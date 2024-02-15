"""Models"""
from datetime import datetime
from decimal import Decimal

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Item(Base):
    """ Model of view table Item"""
    __tablename__ = 'item'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    price: Mapped[Decimal]
    origin_country: Mapped[str]
    date_add: Mapped[datetime] = mapped_column(default=datetime.utcnow())
