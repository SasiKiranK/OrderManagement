import os
from dotenv import load_dotenv

load_dotenv()

ELASTIC_HOST = os.getenv("ELASTIC_HOST", "elasticsearch")
ELASTIC_PORT = int(os.getenv("ELASTIC_PORT", 9200))  # ✅ convert to int
ELASTIC_INDEX = "products"
