from pydantic import BaseModel
from typing import List, Optional

class ProductCreate(BaseModel):
    name: str
    description: str
    category: str
    brand: str
    price: float
    stock: int

class ProductResponse(ProductCreate):
    id: str

class ProductUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    category: Optional[str]
    brand: Optional[str]
    price: Optional[float]
    stock: Optional[int]