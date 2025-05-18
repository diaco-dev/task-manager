from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username=Column(String, index=True, unique=True)
    password=Column(String, index=True)
    email=Column(String, index=True)
    hashed_password = Column(String, nullable=False)