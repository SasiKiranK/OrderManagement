from pydantic import BaseModel

class Product(BaseModel):
    id: str
    name: str
    description: str
    category: str
    brand: str
    price: float
