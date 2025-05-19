from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

#----ObjectId=Str
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


#--------------base model ----------------------
class TaskBase(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    title: str
    description: Optional[str] = None
    done: bool = False

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


#-------------- create ----------------------
class TaskCreate(TaskBase):
    pass

#-------------- update ----------------------
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    done: Optional[bool] = None


#-------------- response ----------------------
class TaskModel(TaskBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "id": "6630d012fbc6e1b2d85c4d1f",
                "title": "Write documentation",
                "description": "Explain how the API works",
                "done": False
            }
        }