from pydantic import BaseModel


class AnswerBase(BaseModel):
    label: str
    is_correct: bool


class AnswerDb(AnswerBase):
    id: int

    class Config:
        orm_mode = True
