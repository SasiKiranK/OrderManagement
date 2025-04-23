from fastapi import FastAPI
from app.routes import router
from app.es import create_index
from app.kafka.consumer import consume_product_events
import threading

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_index()

@app.on_event("startup")
def start_kafka_consumer():
    thread = threading.Thread(target=consume_product_events, daemon=True)
    thread.start()

app.include_router(router)
