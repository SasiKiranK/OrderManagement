from padantic import BaseModel, Field
from typing import List
from bson import ObjectId
import datetime

class Product(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    name: str
    description: str
    category: str
    price: float
    stock: int
    created_at: Optional[datetime.datetime] = None