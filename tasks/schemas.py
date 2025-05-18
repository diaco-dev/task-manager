from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    completed: bool = False

    class Config:
        from_attributes = True

class DeleteTask(BaseModel):
    detail: str
