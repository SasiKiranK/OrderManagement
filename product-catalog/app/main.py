from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from app.routes import product_routes

app = FastAPI(title="Product Catalog API")
app.include_router(product_routes.router, prefix="/products", tags=["Product"])
