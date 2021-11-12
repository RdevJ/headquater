from typing import List, Optional

from app.schemas.answer import AnswerBase, AnswerDb
from pydantic import BaseModel


class QuestionBase(BaseModel):
    title: str
    content: str


class QuestionCreate(QuestionBase):
    answers: Optional[List[AnswerBase]] = None


class QuestionDb(QuestionBase):
    id: int
    answers: Optional[List[AnswerDb]] = None

    class Config:
        orm_mode = True


class QuestionsDb(QuestionBase):
    id: int

    class Config:
        orm_mode = True
