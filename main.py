from fastapi import FastAPI
from database import engine, Base
from database import client

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done.")

app=FastAPI()
app.include_router(tasks.router)
app.include_router(users.router)

# Optional: Health check endpoint to verify MongoDB connection
@app.get("/health")
async def health_check():
    try:
        # Ping MongoDB to check connection
        await client.admin.command("ping")
        return {"status": "MongoDB connection OK"}
    except Exception as e:
        return {"status": "MongoDB connection failed", "error": str(e)}