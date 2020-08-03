from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from fairphonic_data.db.base_class import Base

if TYPE_CHECKING:
    from .country import Country
    from .user import User
    from .track import Track


class Label(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    country_id = Column(Integer, ForeignKey('country.id'))

    country = relationship('Country', back_populates='labels')
    users = relationship('User', back_populates='label')
    tracks = relationship('Track', back_populates='owner')
