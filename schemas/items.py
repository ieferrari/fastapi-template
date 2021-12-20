from typing import List
from pydantic import BaseModel

class ItemBase(BaseModel):
    label: str


class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
