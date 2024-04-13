from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from enum import Enum
from .database import Base

class Users(Base):
    __tablename__ = "Users"
    email = Column(String(120), primary_key=True)
    password = Column(String(120), nullable=False)
    is_loggedIn = Column(Boolean, default=True)
    lastLogin = Column(DateTime)
    creationTime = Column(DateTime)
    updationTime = Column(DateTime)
    lastLoginIP = Column(String(20))

