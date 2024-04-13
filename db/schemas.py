from db.database import Base
from pydantic import BaseModel
from typing import Union

class ReadUser(BaseModel):
    email: str

class CreateUserReq(ReadUser): 
    password: str

class CreateUserDb(CreateUserReq):
    lastLoginIP: str
    is_loggedIn: bool = True
    
class LoginUserUpdateDb(ReadUser):
    lastLoginIP: Union[str, None] = None
    is_loggedIn: bool = True