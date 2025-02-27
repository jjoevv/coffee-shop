from fastapi import FastAPI
from db import db  # Import database từ db.py

app = FastAPI()

@app.get("/data/{collection_name}")
async def get_collection_data(collection_name: str):
    collection = db[collection_name]
    data = await collection.find({}, {"_id": 0}).to_list(length=100)
    return data
