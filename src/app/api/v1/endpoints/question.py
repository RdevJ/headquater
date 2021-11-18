from typing import Any, List

from app.datastore.commands.question.create import CreateQuestionCommand
from app.datastore.commands.question.delete import DeleteQuestionCommand
from app.datastore.commands.question.update import UpdateQuestionCommand
from app.datastore.queries.questions.list import QuestionsQuery
from app.db.dependency import get_db
from app.schemas.question import (QuestionBase, QuestionCreate, QuestionDb,
                                  QuestionsDb)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[QuestionDb])
def read_questions(db: Session = Depends(get_db)) -> Any:
    return QuestionsQuery().get_questions(db=db)


@router.post("/", response_model=QuestionDb)
def create_question(question: QuestionCreate, db: Session = Depends(get_db)) -> Any:
    return CreateQuestionCommand(payload=question).create(db=db)


@router.put("/{question_id}/", response_model=QuestionDb)
def update_question(question_id: int, question: QuestionBase, db: Session = Depends(get_db)) -> Any:
    question_obj = UpdateQuestionCommand(payload=question, question_id=question_id).update_question(db=db)

    if not question_obj:
        raise HTTPException(status_code=404, detail="Question not found")

    return question_obj


@router.delete("/{question_id}/", response_model=QuestionDb)
def delete_question(question_id: int, db: Session = Depends(get_db)) -> Any:
    question = DeleteQuestionCommand(question_id=question_id).delete_question(db=db)

    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    return question
