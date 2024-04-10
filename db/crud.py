from sqlalchemy.orm import Session
from . import models, schemas
import datetime
from psycopg2 import errors


def get_users(db: Session):
    return db.query(models.User).all()


def get_user(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_tasks(db: Session):
    return db.query(models.Tasks).all()


def get_tasks_by_id(db: Session, id: str):
    return db.query(models.Tasks).filter(models.Tasks.id == id).all()


def get_tasks_by_users(db: Session, email: str):
    return db.query(models.Tasks).filter(models.Tasks.userID == email).all()


def create_user(db: Session, user: schemas.CreateUser):
    try:
        db_user = models.Users(
            email=user.email,
            password=user.password,
            lastLogin=datetime.datetime.now(),
            creationTime=datetime.datetime.now(),
            updationTime=datetime.datetime.now(),
        )
        db.add(db_user)
        db.commit()
    except errors.UniqueViolation as exe:
        raise exe
    except Exception as exe:
        raise exe

def create_task(db: Session, task: schemas.CreateTask):
    db_task = models.Tasks(
        userID = task.userID,
        title = task.title,
        description = task.get('description'),
        status = models.TaskStatus.InComplete
    )
    db.add(db_task)
    db.commit()