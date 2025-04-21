from elasticsearch import Elasticsearch
from elastic_transport import Transport

from .config import ELASTIC_HOST, ELASTIC_PORT, ELASTIC_INDEX

# Construct base URL
ES_URL = f"http://{ELASTIC_HOST}:{ELASTIC_PORT}"

# Compatibility headers (required for ES 8.x strict mode)
compat_headers = {
    "Accept": "application/vnd.elasticsearch+json;compatible-with=8",
    "Content-Type": "application/vnd.elasticsearch+json;compatible-with=8"
}

# Create client in compatibility mode
es = Elasticsearch(
    ES_URL,
    headers=compat_headers,
    request_timeout=30
)


def create_index():
    try:
        # Use raw request instead of helper to avoid 400 bug
        response = es.transport.perform_request("HEAD", f"/{ELASTIC_INDEX}")
        index_exists = response.status == 200
    except Exception:
        index_exists = False

    if not index_exists:
        try:
            es.indices.create(
                index=ELASTIC_INDEX,
                body={
                    "mappings": {
                        "properties": {
                            "id": {"type": "keyword"},
                            "name": {"type": "text"},
                            "description": {"type": "text"},
                            "category": {"type": "keyword"},
                            "brand": {"type": "keyword"},
                            "price": {"type": "float"}
                        }
                    }
                }
            )
            print(f"✅ Index '{ELASTIC_INDEX}' created.")
        except Exception as e:
            print(f"❌ Error creating index: {e}")
