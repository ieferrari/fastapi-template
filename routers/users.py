from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from crud.users import get_users, create_user, get_user_by_email, get_user_by_username
from schemas.users import User, UserCreate
from aux.dependencies import get_db
from aux.security import get_password_hash

router = APIRouter()


@router.get("/ping")
async def ping_users():
    return {"msg": "get_user"}


@router.get("/", response_model=List[User])
def get_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.post("/", response_model = User)
def create_new_user( user_data: UserCreate , db = Depends(get_db) ):


    user_with_same_username = get_user_by_username(db, user_data.username)
    if user_with_same_username:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )

    user_with_same_mail = get_user_by_email(db, user_data.email)
    if user_with_same_username:
        raise HTTPException(
            status_code=400,
            detail="The user with this mail already exists in the system.",
        )
    user_data.password = get_password_hash(user_data.password)

    new_user = create_user(user_data.username,
                           user_data.email,
                           user_data.password,
                           db = db)
    return new_user
