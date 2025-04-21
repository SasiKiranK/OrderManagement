from fastapi import APIRouter, HTTPException
from app.schemas.product_schema import ProductCreate, ProductResponse, ProductUpdate
from app.services.product_service import *
from bson.errors import InvalidId

router = APIRouter()

@router.post("/", response_model=ProductResponse)
def create(product: ProductCreate):
    id = create_product(product)
    return {**product.dict(), "id": id}

@router.get("/{id}", response_model=ProductResponse)
def get(id: str):
    try:
        obj_id = ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid product ID format")

    prod = get_product(id)
    if not prod:
        raise HTTPException(status_code=404, detail="Product not found")
    prod["id"] = str(prod["_id"])
    return prod

@router.get("/", response_model=list[ProductResponse])
def list(category: str = None, brand: str = None):
    query = {}
    if category: query["category"] = category
    if brand: query["brand"] = brand
    products = list_products(query)
    return [{**p, "id": str(p["_id"])} for p in products]

@router.put("/{id}")
def update(id: str, updates: ProductUpdate):
    update_product(id, updates.dict(exclude_unset=True))
    return {"message": "Updated"}

@router.delete("/{id}")
def delete(id: str):
    delete_product(id)
    return {"message": "Deleted"}
