from typing import List

from pydantic import BaseModel


class QuizSubmitBase(BaseModel):
    article_id: int
    question_id: int
    answers: List[int]
