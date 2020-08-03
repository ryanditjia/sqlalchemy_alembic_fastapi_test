# Import all the models, so that Base has them before being
# imported by Alembic
from fairphonic_data.db.base_class import Base
from fairphonic_data.models.country import Country
from fairphonic_data.models.genre import Genre
from fairphonic_data.models.label import Label
from fairphonic_data.models.language import Language
from fairphonic_data.models.track import Track
from fairphonic_data.models.user import User
from fairphonic_data.models.work import Work
