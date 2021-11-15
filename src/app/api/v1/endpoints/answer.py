from typing import Any, List

from app.datastore.commands.answer.create import CreateAnswerCommand
from app.datastore.commands.answer.delete import DeleteAnswerCommand
from app.datastore.commands.answer.update import UpdateAnswerCommand
from app.datastore.queries.answers.list import AnswersQuery
from app.db.dependency import get_db
from app.schemas.answer import AnswerBase, AnswerDb
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[AnswerDb], deprecated=True)
def read_answers(db: Session = Depends(get_db)) -> Any:
    return AnswersQuery().read_all(db=db)


@router.post('/', response_model=AnswerDb)
def create_answer(answer: AnswerBase, db: Session = Depends(get_db)) -> Any:
    return CreateAnswerCommand(payload=answer).create(db=db)


@router.put('/{answer_id}/', response_model=AnswerDb)
def update_answer(answer_id: int, answer: AnswerBase, db: Session = Depends(get_db)) -> Any:
    answer_obj = UpdateAnswerCommand(payload=answer, answer_id=answer_id).update_answer(db=db)

    if not answer_obj:
        raise HTTPException(status_code=404, detail="Answer not found")

    return answer_obj


@router.delete("/{answer_id}/", response_model=AnswerDb)
def delete_answer(answer_id: int, db: Session = Depends(get_db)) -> Any:
    answer = DeleteAnswerCommand(answer_id=answer_id).delete_answer(db=db)

    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")

    return answer
