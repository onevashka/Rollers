from fastapi import APIRouter, Depends
from app.database.db import get_session
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(prefix='cart', tags=['CART'])


@router.get('/')
async def get_cart(db: AsyncSession = Depends(get_session)):
    
