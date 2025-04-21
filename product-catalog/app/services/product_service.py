from app.db.mongo import product_collection
from bson import ObjectId
from datetime import datetime

def create_product(product):
    product_dict = product.dict()
    product_dict["created_at"] = datetime.utcnow()
    result = product_collection.insert_one(product_dict)
    return str(result.inserted_id)

def get_product(id):
    return product_collection.find_one({"_id": ObjectId(id)})

def list_products(filter: dict = {}):
    return list(product_collection.find(filter))

def update_product(id, updates):
    return product_collection.update_one({"_id": ObjectId(id)}, {"$set": updates})

def delete_product(id):
    return product_collection.delete_one({"_id": ObjectId(id)})
