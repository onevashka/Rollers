from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, DateTime
from backend.app.database.db import Base
from typing import List
from datetime import datetime
from backend.app.rollers.menu.schemas import SProduct


class SCart(Base):

    __tablename__ = 'cart'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    products: Mapped[List['SCartProduct']] = relationship('CartProduct', back_populates='cart', cascade='all, delete-orphan')
    create_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow)
    update_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class SCartProduct(Base):
    __tablename__ = 'cart_product'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    cart_id: Mapped[int] = mapped_column(Integer, ForeignKey('cart.id'))
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('product.id'))

    cart: Mapped['SCart'] = relationship('Cart', back_populates='products')
    product: Mapped['SProduct'] = relationship('SProduct')
