from typing import TYPE_CHECKING

from sqlalchemy import ARRAY, Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from fairphonic_data.db.base_class import Base

if TYPE_CHECKING:
    from .work import Work
    from .label import Label
    from .genre import Genre
    from .language import Language


class Track(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    primary_artist = Column(String)
    featured_artists = Column(ARRAY(String))
    release_date = Column(Date)
    file_url = Column(String)
    artwork_url = Column(String)
    work_id = Column(Integer, ForeignKey('work.id'))
    isrc = Column(String(15))
    record_label = Column(String)
    upc = Column(String(12))
    owner_id = Column(Integer, ForeignKey('label.id'))
    genre_id = Column(Integer, ForeignKey('genre.id'))
    subgenre_id = Column(Integer, ForeignKey('genre.id'))
    language_id = Column(Integer, ForeignKey('language.id'))
    is_explicit = Column(Boolean)
    is_transcribed = Column(Boolean, default=False)

    work = relationship('Work', back_populates='tracks')
    owner = relationship('Label', back_populates='tracks')
    genre = relationship('Genre', back_populates='tracks')
    subgenre = relationship('Genre', back_populates='tracks')
    language = relationship('Language', back_populates='tracks')
