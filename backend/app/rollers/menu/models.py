from datetime import datetime
from pydantic import BaseModel, Field


class Category(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float

    class Config:
        from_attributes = True
    

class CreateProduct(Product):
    id: int
    id_category: int

    class Config:
        from_attributes = True


