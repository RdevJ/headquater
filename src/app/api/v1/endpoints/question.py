from typing import Any, List

from app.datastore.commands.question.create import CreateQuestionCommand
from app.datastore.queries.questions.list import QuestionsQuery
from app.db.dependency import get_db
from app.schemas.question import QuestionCreate, QuestionDb, QuestionsDb
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[QuestionsDb])
def read_questions(db: Session = Depends(get_db)) -> Any:
    return QuestionsQuery().get_questions(db=db)


@router.post("/", response_model=QuestionDb)
def create_question(question: QuestionCreate, db: Session = Depends(get_db)) -> Any:
    return CreateQuestionCommand(payload=question).create(db=db)
