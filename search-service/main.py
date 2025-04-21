from fastapi import FastAPI
from app.routes import router
from app.es import create_index

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_index()

app.include_router(router)
