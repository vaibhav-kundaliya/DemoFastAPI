from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from enum import Enum
from .database import Base

class TaskStatus(str, Enum):
    InComplete = "InComplete"
    Complete = "Complete"
    InProgress = "InProgress"

class Users(Base):
    __tablename__ = "Users"
    email = Column(String(120), primary_key=True)
    password = Column(String(120), nullable=False)
    is_loggedIn = Column(Boolean, default=True)
    lastLogin = Column(DateTime)
    creationTime = Column(DateTime)
    updationTime = Column(DateTime)
    lastLoginIP = Column(String(20))
    

class Tasks(Base):
    __tablename__ = "Tasks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    userID = Column(String, ForeignKey("Users.email"))
    title = Column(String(80), nullable=False)
    description = Column(String(160), nullable=False)
    status = Column(String(20))
    creationTime = Column(DateTime)
    updationTime = Column(DateTime)
