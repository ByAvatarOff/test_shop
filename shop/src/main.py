"""main endpoint"""
from fastapi import FastAPI
from item_app.item_routers import item_router

app = FastAPI(
    title='Shop App',
    description='Shop App for CRUD operations',
    version='3.1.0',
)

app.include_router(item_router)
