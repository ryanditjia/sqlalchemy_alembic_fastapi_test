from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from fairphonic_data.db.base_class import Base

if TYPE_CHECKING:
    from .item import Item


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    label_id = Column(Integer, ForeignKey('label.id'))

    label = relationship('Label', back_populates='users')
