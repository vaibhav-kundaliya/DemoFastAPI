from pydantic import BaseModel
from typing import Union
from .models import TaskStatus

class UserBase(BaseModel):
    email: str
    
class TaskBase(BaseModel):
    userID: str
    title: str
    description: str

class CreateUser(UserBase):
    password: str

class CreateTask(TaskBase):
    status: TaskStatus
    pass

class ReadUser(UserBase):
    pass
    
class ReadTask(TaskBase):
    id: Union[str, None]
