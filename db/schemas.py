from pydentic import BaseModel
from typing import Union

class UserBase(BaseModel):
    email: str
    
class TaskBase(BaseModel):
    title: str
    description: str

class CreateUser(UserBase):
    password: str

class CreateTask(TaskBase):
    pass

class ReadUser(UserBase):
    pass
    
class ReadTask(TaskBase):
    id: Union[str, None]
    userID: Union[str, None]
