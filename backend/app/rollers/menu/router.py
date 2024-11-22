from fastapi import APIRouter, Depends
from app.database.db import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from .utils import ServicesCategory
from .models import Category


router = APIRouter(prefix='/menu', tags=['MENU'])


@router.get('')
async def get_menu(db: AsyncSession = Depends(get_session)):
    all_categories = ServicesCategory.get_all_categories(db)
    return all_categories


@router.get('/category')
async def get_category(db: AsyncSession = Depends(get_session)):
    pass


@router.get('/category/{id_category}')
async def get_category_by_id(id_category: int, 
                            db: AsyncSession = Depends(get_session)):
    pass


@router.post('/create_product')
async def create_product(new_name_category: str, db: AsyncSession = Depends(get_session)):
    result = await ServicesCategory.create_category(db=db, category_name=new_name_category)
    return result


@router.patch('/product/{id_product}')
async def update_product(id_product: int, 
                         db: AsyncSession = Depends(get_session)):
    pass


@router.delete('/product/{id_product}')
async def delete_product(id_product: int, 
                         db: AsyncSession = Depends(get_session)):
    pass

