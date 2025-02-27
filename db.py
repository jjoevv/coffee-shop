import os
import motor.motor_asyncio
from pymongo import MongoClient
from dotenv import load_dotenv

# Load biến môi trường
load_dotenv()

# Lấy MONGO_URL từ biến môi trường
MONGO_URL = os.getenv("MONGO_URL")

if not MONGO_URL:
    raise ValueError("Cannot find MONGO_URL in env")

# Tạo client Motor async
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)

# Kết nối đến database
db = client["coffee_shop_sales"]

# Kiểm tra kết nối
async def check_connection():
    try:
        await client.admin.command("ping")
        print("✅ Connect successfully!!")
    except Exception as e:
        print(f"❌ Connect failed: {e}")

# Nếu chạy với FastAPI thì dùng event startup để kiểm tra kết nối
