from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URI)
db = client["task_api"]
collection = db["items"]

users_collection = db["users"]
tasks_collection = db["tasks"]