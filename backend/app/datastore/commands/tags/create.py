from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm.session import Session

from app.schemas.tags import TagCreate
from app.models.tag import Tag


class CreateTagCommand(object):
    def __init__(self, payload: TagCreate):
        self.payload = payload

    def create_tag(self, db: Session) -> Tag:
        data = jsonable_encoder(self.payload)
        tag = Tag(**data)
        db.add(tag)
        db.commit()
        db.refresh(tag)
        return tag
