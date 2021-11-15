from typing import Optional

from app.models.answer import Answer
from app.schemas.answer import AnswerBase
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import update


class UpdateAnswerCommand(object):
    def __init__(self, payload: AnswerBase, answer_id: int):
        self.payload = payload
        self.answer_id = answer_id

    def update_answer(self, db: Session) -> Optional[Answer]:
        answer = (
            db.query(Answer).filter(Answer.id == self.answer_id).first()
        )
        if not answer:
            return None

        db.execute(
            update(Answer).
            where(Answer.id == self.answer_id).
            values(self.payload.dict(exclude_none=True))
        )
        db.commit()
        db.refresh(answer)
        return answer
