import sys
sys.path.append("..")
from fastapi import APIRouter, Depends, HTTPException, Request, Header
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
async def createUser(reqData: schemas.CreateUserReq, request: Request, db: Session = Depends(get_db)):
    if not re.match(EMAIL_RE, reqData.email):
        raise HTTPException(status_code=403, detail="Enter valid email address")
    hashed_pwd = password.encrypt(reqData.password)
    reqData.password = hashed_pwd
    security_token = token.create_access_token({"email":reqData.email})
    try:
        print(reqData.email, reqData.password)
        crud.create_user(db, schemas.CreateUserDb(email=reqData.email, password=reqData.password, lastLoginIP=request.client.host))
        return {"detail": "User created", "Token":security_token}
    except IntegrityError as exe:
        print(exe)
        raise HTTPException(status_code=403, detail='Email already exist')
    except Exception as exe:
        print(exe)
        raise HTTPException(status_code=500, detail='Server Error')
    
@auth_service.post("/login")
async def loginUser(reqData:schemas.CreateUserReq, request: Request, db: Session = Depends(get_db)):
    try:
        user = crud.get_user(db, reqData.email)
        if password.compare(reqData.password, user.password):
            sec_token = token.create_access_token(dict(reqData))
            crud.update_user_lastLogin(db, schemas.LoginUserUpdateDb(email=reqData.email, lastLoginIP=request.client.host))
            return {"detail":"user is authenticated", "token":sec_token}
        else:
            HTTPException(status_code=403, detail="Wrong password")
    except Exception as exe:
        print(exe)
        raise HTTPException(status_code=500, detail="Server Error")
    
@auth_service.get("/logout")
async def logoutUser(Authorization: str = Header(strict=True), db: Session = Depends(get_db)):
    try:
        email = token.get_email_from_token(Authorization)
        crud.update_user_logout(db,schemas.LoginUserUpdateDb(email=email, is_loggedIn=False))
        return {"detail":"user is logged out"}
    except Exception as exe:
        print(exe)

        raise HTTPException(status_code=500, detail="Server Error")