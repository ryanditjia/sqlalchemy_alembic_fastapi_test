from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from fairphonic_data.db.base_class import Base

if TYPE_CHECKING:
    from .track import Track


class Work(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    iswc = Column(String(15))
    official_lyrics = Column(String)
    composer = Column(String)
    publisher = Column(String)
    lyrics_publisher = Column(String)

    tracks = relationship('Track', back_populates='work')
