from sqlalchemy.orm import Session
from . import models, schemas

def get_users(db: Session):
    return db.query(models.User).all()

def get_user(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()