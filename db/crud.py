from sqlalchemy.orm import Session
from . import models, schemas
import datetime
from psycopg2 import errors

def get_users(db: Session):
    return db.query(models.Users).all()


def get_user(db: Session, email: str):
    return db.query(models.Users).filter(models.Users.email == email).first()


def create_user(db: Session, user: schemas.CreateUserDb):
    db_user = models.Users(
        email=user.email,
        lastLoginIP = user.lastLoginIP,
        password=user.password,
        lastLogin=datetime.datetime.now(),
        creationTime=datetime.datetime.now(),
        updationTime=datetime.datetime.now()
    )
    db.add(db_user)
    db.commit()

def update_user_lastLogin(db: Session, user: schemas.LoginUserUpdateDb):
    user_up = db.query(models.Users).filter(models.Users.email==user.email).first()
    if user_up:
        user_up.lastLogin = datetime.datetime.now()
        user_up.is_loggedIn = user.is_loggedIn
        user_up.lastLoginIP = user.lastLoginIP
        db.commit()
    else:
        raise Exception(message="user email is not in db")
    
def update_user_logout(db:Session, user: schemas.CreateUserDb):
    user_up = db.query(models.Users).filter(models.Users.email==user.email).first()
    if user_up:
        user_up.is_loggedIn = user.is_loggedIn
        db.commit()
    else:
        raise Exception(message="user email is not in db")