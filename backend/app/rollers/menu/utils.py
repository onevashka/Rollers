from sqlalchemy import select
from .models import Product, Category
from .schemas import SCategory, SProduct
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from typing import Union


class ServicesCategory:
    @classmethod
    async def _get_all_categories(cls, db: AsyncSession):
        query = await db.execute(select(SCategory))
        if not query:
            raise ValueError('No categories found')  
        all_categories = query.scalars().all()
        return [Category.model_validate(category) for category in all_categories]

    @classmethod
    async def _get_category_by_id(cls, category_id: int, db: AsyncSession):
        if not category_id:
            raise HTTPException(status_code=404, detail='No category')
        category = await db.get(SCategory, category_id)
        return Category(name=category.name)

    @classmethod
    async def _create_category(cls, category_name: int, db: AsyncSession):
        if not category_name:
            raise HTTPException(status_code=404,  detail='No category')
        new_category = SCategory(name=category_name)
        db.add(new_category)
        await db.commit()
        await db.refresh(new_category)
        return {"message": "Task created successfull"}
    
    @classmethod
    async def _update_category(cls, category_id: int, new_name: str, db: AsyncSession):
        if category_id or new_name:
            category = await db.get(SCategory, category_id)
            if not category:
                raise HTTPException(status_code=404, detail='Could not find category')
            category.name = new_name
            await db.commit()
            await db.refresh(category)
            return {"message": "Task updated successfull"}

    @classmethod
    async def _delete_category(cls, category_id: int, db: AsyncSession):
        category = await db.get(SCategory, category_id)
        if not category:
            raise HTTPException(status_code=404, detail='Category not found')
        db.delete(category)
        await db.commit()
        return {"message": "Task deleted successfull"}


class ServicesProduct:
    @classmethod
    async def _get_all_products_by_id(cls, category_name: str, db: AsyncSession):
        query = await db.execute(select(SProduct).where(SProduct.name == category_name))
        print(query)
        all_products_by_category = query.scalars().all()
        print(all_products_by_category)
        return [Product(
                        id=product.id,
                        name=product.name,
                        description=product.description,
                        price=product.price) for product in all_products_by_category]

    @classmethod
    async def _get_product_by_id(cls, product_id: int, db: AsyncSession):
        if not product_id:
            raise HTTPException(status_code=404, detail='Product not found')
        product = await db.get(SProduct, product_id)
        if not product:
            raise HTTPException(status_code=404, detail='Product not found')
        return Product( 
                        id=product.id,
                        name=product.name, 
                        price=product.price, 
                        description=product.description)

    @classmethod
    async def _create_product(
        cls, 
        product_name: str, 
        product_description: str, 
        product_price: Union[float, int], 
        category_id: int, 
        db: AsyncSession):

        if not (product_name or product_description or product_price or category_id):
            raise HTTPException(status_code=404, detail='None found')

        new_product = SProduct(
        name=product_name,
        description=product_description,
        price=product_price,
        category_id=category_id)

        db.add(new_product)
        await db.commit()
        await db.refresh(new_product)
        return {"message": "Task created successfull"}
        

    @classmethod
    async def _update_product(
        cls, 
        db: AsyncSession,
        product_id: int, 
        new_name: str = None, 
        new_description: str = None, 
        new_price: Union[float, int] = None,):

        pass
        
    @classmethod
    async def _delete_product(cls, product_id: int, db: AsyncSession):
        product = db.get(SProduct, product_id)
        if not product:
            raise HTTPException(status_code=404, detail='Product not found')
        db.delete(product)
        await db.commit()
        return {"message": "Task deleted successfull"}

