from app.models.answer import Answer
from sqlalchemy.orm.session import Session


class AnswerQuery(object):
    def get_answer(self, answer_id: int, db: Session):
        return db.query(Answer).filter(Answer.id == answer_id).first()
