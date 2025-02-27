import os
import motor.motor_asyncio

# Lấy MONGO_URI từ biến môi trường
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

# Tạo client Motor async
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client["coffee_shop_sales"]
