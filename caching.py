from fastapi import FastAPI
import redis
import json
import time

app = FastAPI()

# Connect to Redis
cache = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


@app.get("/products")
def get_products():

    # 1. Check cache
    cached_data = cache.get("products")

    if cached_data:
        return {
            "source": "cache",
            "data": json.loads(cached_data)#converts the json string into python object
        }

    # 2. Simulate getting data from database
    time.sleep(3)

    products = [
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Phone"},
        {"id": 3, "name": "Keyboard"}
    ]

    # 3. Store data in Redis for 60 seconds
    cache.set(
        "products",
        json.dumps(products),#converts into a json string 
        ex=60 #time untill the data should remains in the cache 
    )

    return {
        "source": "database",
        "data": products
    }