from typing import List, Optional
from pydantic import BaseModel
from .items import Item

class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str
    email: Optional[str] = None

class User(UserBase):
    id: int
    is_active: bool
    is_superuser: bool
    items: List[Item] = []

    class Config:
        orm_mode = True  # read data even if its not a dict, but an ORM
