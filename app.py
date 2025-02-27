from fastapi import FastAPI
from contextlib import asynccontextmanager
from db import db, check_connection  # Import hàm kiểm tra kết nối
import math 

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🔄 Checking MongoDB connection...")
    await check_connection()  # Kiểm tra MongoDB khi ứng dụng khởi động
    yield
    print("🛑 Shutting down app...")  # Log khi ứng dụng đóng

app = FastAPI(lifespan=lifespan)

@app.get("/data/{collection_name}")
async def get_collection_data(collection_name: str):
    try:
        collection = db[collection_name]
        if collection is None:
            return {"error": f"Collection '{collection_name}' not found"}
        
        data = await collection.find({}, {"_id": 0}).to_list(length=100)
        if not data:
            return {"warning": "No data found in collection"}
        for doc in data:
            for key, value in doc.items():
                if isinstance(value, float) and math.isnan(value):
                    doc[key] = None  # Hoặc có thể thay bằng 0

        return {"data": data}
    except Exception as e:
        import traceback
        error_msg = traceback.format_exc()  # Lấy toàn bộ lỗi chi tiết
        print(f"❌ Error in API: {error_msg}")  # Log lỗi ra terminal
        return {"error": str(e), "details": error_msg}  # Trả về lỗi chi tiết
