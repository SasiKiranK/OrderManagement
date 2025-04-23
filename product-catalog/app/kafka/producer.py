from confluent_kafka import Producer
import json
import os

producer = Producer({
    'bootstrap.servers': os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
})

def send_product_created_event(product: dict):
    producer.produce(
        topic= "product.created",
        key=str(product["id"]),
        value=json.dumps(product)
    )
    producer.flush()