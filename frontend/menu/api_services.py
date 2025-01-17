import aiohttp
import asyncio
from typing import List

class APIMenu:
    @classmethod
    async def _get_menu_data(cls) -> List:
        async with aiohttp.ClientSession() as session:
            async with session.get('http://127.0.0.1:8000/api/menu') as response:
                data = await response.json()
                return data

    @classmethod
    async def _get_products_data(cls, category_name: str) -> List:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'http://127.0.0.1:8000/api/menu/product/{category_name}') as response:
                data = await response.json()
                print(data)
                return data

    @classmethod
    async def _get_product_data_by_id(cls, product_id: int) -> List:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'http://127.0.0.1:8000/api/menu/product/{product_id}') as response:
                data = await response.json()
                return data
