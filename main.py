from fastapi import FastAPI
import tasks
import user
from database import client

app=FastAPI()
app.include_router(tasks.routers)
app.include_router(user.routers)

# Optional: Health check endpoint to verify MongoDB connection
@app.get("/health")
async def health_check():
    try:
        # Ping MongoDB to check connection
        await client.admin.command("ping")
        return {"status": "MongoDB connection OK"}
    except Exception as e:
        return {"status": "MongoDB connection failed", "error": str(e)}