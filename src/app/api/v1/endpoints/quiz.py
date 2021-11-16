from app.db.dependency import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.post('/', response_model=AnswerDb)
def submit_answers(answer: AnswerBase, db: Session = Depends(get_db)) -> Any:
    return CreateAnswerCommand(payload=answer).create(db=db)
