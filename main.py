from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB client
client = AsyncIOMotorClient("mongodb://localhost:27017")


# Initialize FastAPI and Admin
app = FastAPI()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)


# Health check for MongoDB
@app.get("/health")
async def health_check():
    try:
        await client.admin.command("ping")
        return {"status": "MongoDB connection OK"}
    except Exception as e:
        return {"status": "MongoDB connection failed", "error": str(e)}
