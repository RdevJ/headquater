from app.db.mixins import ReadAllMixin
from app.models.answer import Answer


class AnswersQuery(ReadAllMixin):
    model = Answer
