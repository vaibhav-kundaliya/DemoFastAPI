from ast import Try
import sys
from tokenize import Token
sys.path.append("..")
from fastapi import APIRouter, Depends, HTTPException
from db.database import SessionLocal
from db import crud, models, schemas
from sqlalchemy.orm import Session
from utils import password, token
import re
from sqlalchemy.exc import IntegrityError

EMAIL_RE = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

auth_service = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@auth_service.get("/")
def root():
    return {"message":"Service is on"}

@auth_service.post("/createUser")
async def createUser(reqData: schemas.CreateUser, db: Session = Depends(get_db)):
    createUser_dict = dict(reqData)
    if not re.match(EMAIL_RE, createUser_dict['email']):
        raise HTTPException(status_code=403, detail="Enter valid email address")
    hashed_pwd = password.encrypt(createUser_dict['password'])
    reqData = schemas.CreateUser(email=reqData.email, password=hashed_pwd)
    security_token = token.create_access_token(reqData)
    try:
        crud.create_user(db, reqData)
        return {"detail": "User created", "Token":security_token}
    except IntegrityError as exe:
        db.rollback()
        print("-------",exe)
        raise HTTPException(status_code=403, detail='Email already exist')
    except Exception as exe:
        print(exe)
        raise HTTPException(status_code=500, detail='Server Error')

@auth_service.post("/login")
async def login(reqData: schemas.CreateUser, db: Session = Depends(get_db)):
    try:
        user =  crud.get_user(db, reqData.email)
        if password.compare(user.password, dict(reqData)['password']):
            access_token = token.create_access_token(schemas.User.from_orm(user))
            return {"Access-Token" : access_token,"UserInfo":schemas.User.from_orm(user)}
        return {"detail": "user exists"}
    except  Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Server Error")