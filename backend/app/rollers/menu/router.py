from fastapi import APIRouter, Depends
from app.database.db import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from .utils import ServicesCategory, ServicesProduct
from .models import Category, Product
from typing import List

router = APIRouter(prefix='/menu', tags=['MENU'])


@router.get('', response_model=List[Category])
async def get_menu(db: AsyncSession = Depends(get_session)) -> List[Category]:
    all_categories = await ServicesCategory._get_all_categories(db)
    return all_categories


@router.post('/create_category')
async def create_category(new_name_category: str, db: AsyncSession = Depends(get_session)) -> dict:
    result = await ServicesCategory._create_category(db=db, category_name=new_name_category)
    return result


@router.get('/product/{category_name}', response_model=List[Product])
async def get_product(category_name: str, db: AsyncSession = Depends(get_session)) -> List[Product]:
    all_products = await ServicesProduct._get_all_products_by_id(db=db, category_name=category_name)
    return all_products


@router.get('/product/{category_name}/{product_id}', response_model=Product)
async def get_product_by_id(product_id: int, category_name: str,
                            db: AsyncSession = Depends(get_session)) -> Product:
    product = await ServicesProduct._get_product_by_id(product_id=product_id, db=db)
    return product


@router.post('/create_product')
async def create_product(new_product_name: str, new_product_price: float, 
                         new_product_description: str, category_id: int, 
                         db: AsyncSession = Depends(get_session)) -> dict:
    result = await ServicesProduct._create_product(db=db, 
                                                 product_name=new_product_name, 
                                                 product_price=new_product_price, 
                                                 product_description=new_product_description, 
                                                 category_id=category_id)
    return result


@router.patch('/product/{product_id}')
async def update_product(product_id: int, 
                         db: AsyncSession = Depends(get_session)):
    pass


@router.delete('/product/{product_id}')
async def delete_product(product_id: int, 
                         db: AsyncSession = Depends(get_session)) -> dict:
    result = await ServicesProduct._delete_product(product_id=product_id, db=db)
    return result

