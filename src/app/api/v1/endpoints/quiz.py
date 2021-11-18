from app.datastore.commands.quiz.submit import SubmitAnswerCommand
from app.db.dependency import get_db
from app.schemas.quiz import QuizSubmitBase
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.post('/')
def submit(answer: QuizSubmitBase, db: Session = Depends(get_db)) -> None:
    return SubmitAnswerCommand(payload=answer, db=db).submit_answer()
