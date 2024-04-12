from pydantic import BaseModel
from typing import Union
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
    email: str
    is_loggedIn: Union[bool, None] = None
    lastLoginIP: Union[str, None] = None


class ReadTask(TaskBase):
    id: Union[str, None]
