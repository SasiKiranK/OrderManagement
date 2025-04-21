from fastapi import APIRouter, Query
from elasticsearch import Elasticsearch
from app.models import Product
from app.config import ELASTIC_INDEX
from app.es import es
import json
from elastic_transport import Transport


router = APIRouter()

@router.get("/search/")
def search_products(q: str = Query(..., min_length=1)):
    headers = {
        "Accept": "application/vnd.elasticsearch+json;compatible-with=8",
        "Content-Type": "application/vnd.elasticsearch+json;compatible-with=8"
    }

    body = json.dumps({
        "query": {
            "multi_match": {
                "query": q,
                "fields": ["name", "description", "category", "brand"]
            }
        }
    })

    response = es.transport.perform_request(
        "POST",
        f"/{ELASTIC_INDEX}/_search",
        headers=headers,
        body=body
    )

    hits = response.body["hits"]["hits"]
    return {"results": [hit["_source"] for hit in hits]}



@router.post("/index/")
def index_product(product: Product):
    body = json.dumps(product.dict())
    headers = {
        "Accept": "application/vnd.elasticsearch+json;compatible-with=8",
        "Content-Type": "application/vnd.elasticsearch+json;compatible-with=8"
    }

    response = es.transport.perform_request(
        "POST",
        f"/{ELASTIC_INDEX}/_doc/{product.id}",
        headers=headers,
        body=body
    )

    # ✅ FIX: response.body is the actual dict
    return {"status": "indexed", "result": response.body.get("result", "ok")}