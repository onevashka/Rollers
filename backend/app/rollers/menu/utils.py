from sqlalchemy import select
from .models import Product, Category
from .schemas import SCategory
from sqlalchemy.ext.asyncio import AsyncSession


class ServicesCategory:
    @classmethod
    async def get_all_categories(cls, db: AsyncSession):
        print('dffdsfsdfdsfdsfdsfsdfdsfdsfdsfds')
        query = await db.execute(select(Category.name))
        all_categories = query.scalars().all()
        return [Category.from_orm(category) for category in all_categories]

    @classmethod
    async def get_category_by_id(cls, category_id: int, db: AsyncSession):
        pass

    @classmethod
    async def create_category(cls, category_name: int, db: AsyncSession):
        if category_name:
            new_category = SCategory(name=category_name)
            db.add(new_category)
            await db.commit()
            await db.refresh(new_category)
            return {"message": "Task created successfull"}
        return {"message": "title is None"}
    
    @classmethod
    async def update_category(cls, category_id: int, new_name: str, db: AsyncSession):
        pass

    @classmethod
    async def delete_category(cls, category_id: int, db: AsyncSession):
        pass


class ServicesProduct:
    @classmethod
    async def get_all_products_by_id(cls, db: AsyncSession):
        pass

    @classmethod
    async def get_product_by_id(cls, product_id: int, db: AsyncSession):
        pass

    @classmethod
    async def create_product(cls, product_name: str, 
                             product_description: str, 
                             product_price: float | int, 
                             category_id: int, 
                             db: AsyncSession):
        pass

    @classmethod
    async def update_product(cls, product_id: int, 
                             new_name: str, 
                             new_description: str, 
                             new_price: float | int,
                             db: AsyncSession):
        pass

    @classmethod
    async def delete_product(cls, product_id: int, db: AsyncSession):
        pass

