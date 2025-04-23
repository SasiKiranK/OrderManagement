from fastapi import APIRouter, Query
from elasticsearch import Elasticsearch
from app.models import Product
from app.config import ELASTIC_INDEX
from app.es import es
import json
from elastic_transport import Transport
from fastapi import APIRouter, Query, HTTPException
from elasticsearch import Elasticsearch
import logging

router = APIRouter()
es = Elasticsearch("http://elasticsearch:9200")  # ES 8+ style

@router.get("/search/")
def search_products(q: str = Query(...)):
    query = {
        "query": {
            "match": {
                "name": q
            }
        }
    }
    try:
        # Check if index exists
        if not es.indices.exists(index="products"):
            raise HTTPException(status_code=404, detail="Index 'products' does not exist.")

        response = es.search(index="products", body=query)
        hits = response.get("hits", {}).get("hits", [])
        return {"results": hits}
    except Exception as e:
        logging.error(f"Elasticsearch query failed: {e}")
        raise HTTPException(status_code=500, detail="Search query failed.")


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