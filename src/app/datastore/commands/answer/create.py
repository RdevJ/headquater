from app.db.mixins import CreateMixin
from app.models.answer import Answer
from app.schemas.answer import AnswerBase
from fastapi.encoders import jsonable_encoder


class CreateAnswerCommand(CreateMixin):
    model = Answer

    def __init__(self, payload: AnswerBase):
        self.payload = jsonable_encoder(payload)
