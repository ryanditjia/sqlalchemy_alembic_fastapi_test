from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from fairphonic_data.db.base_class import Base

if TYPE_CHECKING:
    from .label import Label


class Country(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    code = Column(String, unique=True)

    labels = relationship('Label', back_populates='country')
