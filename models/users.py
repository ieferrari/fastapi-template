from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime,\
    Boolean
from sqlalchemy.orm import relationship

from datetime import datetime

#from .items import Item
from db.database import Base

from typing import TYPE_CHECKING  # to avoid circular import
if TYPE_CHECKING:
    from models.items import Item  # noqa: F401

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), index=True, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    items = relationship("Item", back_populates="owner")
