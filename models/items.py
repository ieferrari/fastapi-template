from typing import TYPE_CHECKING
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime,\
    Boolean
from sqlalchemy.orm import relationship
from db.database import Base

from typing import TYPE_CHECKING # to avoid circular import
if TYPE_CHECKING:
    from .users import User    # noqa: F401
from models.users import User

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    label = Column(String)
    owner_id = Column(Integer, ForeignKey(User.id))
    owner = relationship("User", back_populates="items")
