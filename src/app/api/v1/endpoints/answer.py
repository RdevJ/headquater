from typing import Any, List

from app.datastore.commands.answer.create import CreateAnswerCommand
from app.datastore.queries.answers.list import AnswersQuery
from app.db.dependency import get_db
from app.schemas.answer import AnswerBase, AnswerDb
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[AnswerDb], deprecated=True)
def read_answers(db: Session = Depends(get_db)) -> Any:
    return AnswersQuery().read_all(db=db)


@router.post('/', response_model=AnswerDb)
def create_answer(answer: AnswerBase, db: Session = Depends(get_db)) -> Any:
    return CreateAnswerCommand(payload=answer).create(db=db)
