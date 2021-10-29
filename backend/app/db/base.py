# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.tag import Tag  #noqa
from app.models.article import Article  # noqa
from app.models.statistics import Statistics  # noqa
from app.models.question import Question  # noqa
from app.models.answer import Answer  # noqa
