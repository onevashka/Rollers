from fastapi import FastAPI
from app.rollers.menu.router import router as router_menu
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(router_menu, prefix='/api')


if __name__ == '__main__':
    import uvicorn
    print("Запуск сервера...")
    uvicorn.run('app.main:app', reload=True)