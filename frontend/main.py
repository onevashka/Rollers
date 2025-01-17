from nicegui import ui, app
from .menu.router import router as router_menu


app.include_router(router=router_menu)


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(port=8080)