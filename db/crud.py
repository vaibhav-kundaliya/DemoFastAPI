from sqlalchemy.orm import Session
from . import models, schemas
import datetime
from psycopg2 import errors


def get_users(db: Session):
    return db.query(models.Users).all()


def get_user(db: Session, email: str):
    return db.query(models.Users).filter(models.Users.email == email).first()


def get_tasks(db: Session):
    return db.query(models.Tasks).all()


def get_tasks_by_id(db: Session, id: str):
    return db.query(models.Tasks).filter(models.Tasks.id == id).all()


def get_tasks_by_users(db: Session, email: str):
    return db.query(models.Tasks).filter(models.Tasks.userID == email).all()


def create_user(db: Session, user: schemas.CreateUser, lastLoginIP: str):
    db_user = models.Users(
        email=user.email,
        password=user.password,
        lastLogin=datetime.datetime.now(),
        creationTime=datetime.datetime.now(),
        updationTime=datetime.datetime.now(),
        lastLoginIP = lastLoginIP
    )
    db.add(db_user)
    db.commit()


def create_task(db: Session, task: schemas.CreateTask):
    db_task = models.Tasks(
        userID=task.userID,
        title=task.title,
        description=task.get("description"),
        status=models.TaskStatus.InComplete,
    )
    db.add(db_task)
    db.commit()


def update_user_lastLogin(db: Session, user: schemas.ReadUser):
    user_up = db.query(models.Users).filter(models.Users.email==user.email).first()
    if user_up:
        user_up.lastLogin = datetime.datetime.now()
        user_up.is_loggedIn = True
        user_up.lastLoginIP = user.lastLoginIP
        db.commit()
    else:
        raise Exception(message="user email is not in db")
    
def update_user_logout(db:Session, user: schemas.ReadUser):
    user_up = db.query(models.Users).filter(models.Users.email==user.email).first()
    if user_up:
        user_up.is_loggedIn = False
        db.commit()
    else:
        raise Exception(message="user email is not in db")