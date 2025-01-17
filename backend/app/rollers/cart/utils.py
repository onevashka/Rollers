from app.database.db import get_session
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession'
from .schemas import SCart, SCartProduct
from sqlalchemy import select
from .models import *


class ServicesCart:

    @classmethod
    async def _get_cart(cls, cart_id: int, db: AsyncSession):
        if not cart_id:
            raise HTTPException(status_code=404, detail='Not Found')
        cart = await db.get(SCart, cart_id)
        return [Cart(name=prod.name) for prod in cart.products]

