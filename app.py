import os
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# Lấy biến môi trường
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")  # Mặc định là localhost nếu không có biến môi trường
client = MongoClient(MONGO_URI)
db = client["coffee_shop_sales"]

@app.route("/")
def home():
    return {"message": "API is running on Render!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
