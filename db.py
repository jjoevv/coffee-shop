import os
import motor.motor_asyncio

# Lấy MONGO_URI từ biến môi trường
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

# Tạo client Motor async
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client["coffee_shop_sales"]
