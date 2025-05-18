from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str
    pass

class User(UserBase):
    id: int

    class Config:
        from_attributes= True

class DeleteUser(BaseModel):
    detail: str

class ChangePassword(BaseModel):
    current_password: str
    new_password: str

class Message(BaseModel):
    message: str