from nicegui import APIRouter, ui
from .api_services import APIMenu

router = APIRouter(prefix='/menu')


@router.page('/', dark=True)
async def get_main_page():
    data = await APIMenu._get_menu_data()
    with ui.card().tight().style('margin-left: auto; margin-right: 0; background-color: #ADD8E6; color: black;'):
        with ui.row():
            with ui.card().style('background-color: #ADD8E6;'):
                with ui.dropdown_button('Menu', auto_close=True, color='#5F9EA0', icon='menu'):
                    for item in data:
                        ui.item(text=item['name'], on_click=lambda name=item['name']: ui.run_javascript(f'window.location.href = "/menu/products/{name}"'))
            
            with ui.card().style('background-color: #ADD8E6;'):
                ui.button('Delivery and payment', on_click=lambda: ui.notify('click'), color='#5F9EA0')
            
            with ui.card().style('background-color: #ADD8E6;'):
                ui.button('About us', on_click=lambda: ui.notify('click'), color='#5F9EA0')
            
            with ui.card().style('background-color: #ADD8E6;'):
                ui.button('Reviews', on_click=lambda: ui.notify('click'), color='#5F9EA0')
            
            with ui.card().style('background-color: #ADD8E6;'):
                ui.button('Contacts', on_click=lambda: ui.notify('click'), color='#5F9EA0')

            with ui.card().style('background-color: #ADD8E6;'):
                ui.button('Log in', on_click=lambda: ui.notify('click'), color='#5F9EA0', icon='logout')

            with ui.card().style('background-color: #ADD8E6;'):
                ui.button('Basket', on_click=lambda: ui.notify('click'), color='#5F9EA0', icon='shopping_cart')


@router.page('/products/{category_name}', dark=True)
async def get_products(category_name: str):
    data = await APIMenu._get_products_data(category_name=category_name)
    for product in data:
        with ui.card():
            with ui.row():
                    ui.label(f'Name -> {product['name']}')
                    ui.label(f'Description -> {product['description']}')
                    ui.label(f'Price -> {product['price']}')
                    ui.button('Details', on_click=lambda id = product['id']: ui.run_javascript(f'window.location.href = "/menu/products/{id}"'))


@router.page('/products/{product_id}')
async def get_products_by_id(product_id: int):
    data = await APIMenu._get_product_data_by_id(product_id=product_id)
    for product in data:
        with ui.card():
            with ui.row():
                ui.label(f'Name -> {product['name']}')
                ui.label(f'Description -> {product['description']}')
                ui.label(f'Price -> {product['price']}')
                ui.button('Back', on_click=lambda: ui.run_javascript('window.history.back()'))        



