from sqlalchemy.orm import Session
from schemas.users import UserCreate
from models.users import User
#from db.database import SessionLocal
from fastapi import Depends
from aux.dependencies import get_db






def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()




def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()



def create_user(username: str, email:str, password: str ,db: Session)-> User:
    fake_hashed_password = password+ 'fake_hashed'
    db_user = User(username = username,
                   email = email,
                   hashed_password = password
                   )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
