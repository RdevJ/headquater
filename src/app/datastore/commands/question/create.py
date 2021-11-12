from typing import Any, List, Optional

from app.datastore.commands.answer.create import CreateAnswerCommand
from app.models.question import Question
from app.schemas.answer import AnswerBase
from app.schemas.question import QuestionCreate
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm.session import Session


class CreateQuestionCommand(object):
    model = Question

    def __init__(self, payload: QuestionCreate):
        self.payload = payload

    def create(self, db: Session) -> Any:
        question = Question(**jsonable_encoder(self.payload, exclude={'answers'}))
        self._create_answers(db=db, answers=self.payload.answers, question=question)
        db.add(question)
        db.commit()
        db.refresh(question)
        return question

    def _create_answers(self, db: Session, answers: Optional[List[AnswerBase]], question: Question):
        if not answers:
            return

        for answer in answers:
            answer = CreateAnswerCommand(payload=answer).create(db=db)
            question.answers.append(answer)
