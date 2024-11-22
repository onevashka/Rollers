from fastapi import FastAPI
from app.rollers.menu.router import router as router_menu


app = FastAPI()
app.include_router(router_menu)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('app.main:app', reload=True)