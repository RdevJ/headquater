from typing import Optional

from app.models.question import Question
from sqlalchemy.orm.session import Session


class DeleteQuestionCommand(object):
    def __init__(self, question_id: int):
        self.question_id = question_id

    def delete_question(self, db: Session) -> Optional[Question]:
        question = (
            db.query(Question).filter(Question.id == self.question_id).first()
        )
        if not question:
            return None

        db.delete(question)
        db.commit()
        return question
