from fastapi import FastAPI
from routers import tasks, users
from database import engine, Base
from models import user, task

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done.")

app=FastAPI()
app.include_router(tasks.router)
app.include_router(users.router)