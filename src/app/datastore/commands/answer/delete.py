from typing import Optional

from app.models.answer import Answer
from sqlalchemy.orm.session import Session


class DeleteAnswerCommand(object):
    def __init__(self, answer_id: int):
        self.answer_id = answer_id

    def delete_answer(self, db: Session) -> Optional[Answer]:
        answer = (
            db.query(Answer).filter(Answer.id == self.answer_id).first()
        )
        if not answer:
            return None

        db.delete(answer)
        db.commit()
        return answer
