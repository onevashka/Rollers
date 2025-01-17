from pydantic import BaseModel


class Cart(BaseModel):
    name: str
    quantity: int
    price: int

    class Config:
        from_attributes = True


class CartProduct(BaseModel):
    pass
