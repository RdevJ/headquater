from typing import List

from app.models.question import Question
from sqlalchemy.orm.session import Session


class QuestionsQuery(object):
    def get_questions(self, db: Session) -> List[Question]:
        return db.query(Question).all()
