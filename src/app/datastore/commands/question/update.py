from typing import Optional

from app.models.question import Question
from app.schemas.question import QuestionBase
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import update


class UpdateQuestionCommand(object):
    def __init__(self, payload: QuestionBase, question_id: int):
        self.payload = payload
        self.question_id = question_id

    def update_question(self, db: Session) -> Optional[Question]:
        question = (
            db.query(Question).filter(Question.id == self.question_id).first()
        )
        if not question:
            return None

        db.execute(
            update(Question).
            where(Question.id == self.question_id).
            values(self.payload.dict(exclude_none=True))
        )
        db.commit()
        db.refresh(question)
        return question
