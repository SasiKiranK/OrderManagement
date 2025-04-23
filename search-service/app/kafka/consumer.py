from confluent_kafka import Consumer
from elasticsearch import Elasticsearch
import json
import os

consumer = Consumer({
    'bootstrap.servers': os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092"),
    'group.id': 'search-group',
    'auto.offset.reset': 'earliest'
})

host = os.getenv("ELASTIC_HOST", "elasticsearch")
port = os.getenv("ELASTIC_PORT", "9200")
es = Elasticsearch(f"http://{host}:{port}")
consumer.subscribe(['product.created'])

def consume_product_events():
    while True:
        msg = consumer.poll(1.0)
        if msg is None or msg.error():
            continue
        product = json.loads(msg.value().decode('utf-8'))
        
        body = json.dumps(product)
        headers = {
            "Accept": "application/vnd.elasticsearch+json;compatible-with=8",
            "Content-Type": "application/vnd.elasticsearch+json;compatible-with=8"
        }
        es.index(index="products", id=product["id"], body=product)  # ✅ v7 style


        # response = es.transport.perform_request(
        #     "POST",
        #     f"/products/_doc/{product.id}",
        #     headers=headers,
        #     body=body
        # )

        # # ✅ FIX: response.body is the actual dict
        # return {"status": "indexed", "result": response.body.get("result", "ok")}
        # es.index(index="products", id=product["id"], document=product)
