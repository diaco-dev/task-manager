from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from sqlalchemy import Column


class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username=Column(String, index=True, unique=True)
    password=Column(String, index=True)
    email=Column(String, index=True)
    hashed_password =Column(String, nullable=False)