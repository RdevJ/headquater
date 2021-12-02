from app.datastore.commands.quiz.finalize import FinalizeCommand
from app.datastore.commands.quiz.submit import SubmitAnswerCommand
from app.db.dependency import get_db
from app.schemas.quiz import QuizFinalize, QuizSubmitBase
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.post('/submit/')
def submit(answer: QuizSubmitBase, db: Session = Depends(get_db)) -> None:
    return SubmitAnswerCommand(payload=answer, db=db).submit_answer()


@router.post('/finalize/')
def finalize(payload: QuizFinalize, db: Session = Depends(get_db)) -> None:
    return FinalizeCommand(payload=payload, db=db).finalize()
