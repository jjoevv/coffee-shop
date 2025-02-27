import motor.motor_asyncio
import asyncio

MONGO_URL = "mongodb+srv://hnthaovyadmin:mypassword@cluster0.ay6mkf8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client["coffee_shop_sales"]

async def test_mongo():
    try:
        await client.admin.command("ping")
        print("✅ MongoDB Connected Successfully!")
        collection = db["orders"]
        data = await collection.find_one()
        print("📌 Sample Data:", data)
    except Exception as e:
        print(f"❌ Error: {e}")

asyncio.run(test_mongo())
