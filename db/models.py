from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base

class Users(Base):
    id = Column(Integer, autoincrement=True)
    email = Column(String(120), primary_key=True)
    password = Column(String(120), nullable=False)
    is_loggedIn = Column(Boolean, default=False)
    lastLogin = Column(DateTime)
    creationTime = Column(DateTime)
    updationTime = Column(DateTime)
    
    creater = relationship("Tasks", back_populates="owner")

class Tasks(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    userID = Column(Integer, ForeignKey("users.email"))
    title = Column(String(80), nullable=False)
    description = Column(String(160), nullable=False)
    status = Column(String(30)) 
    creationTime = Column(DateTime)
    updationTime = Column(DateTime)

    creater = relationship("Users", back_populates='items')