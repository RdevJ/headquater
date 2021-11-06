from app.models.tag import Tag
from app.schemas.tags import TagBase
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm.session import Session


class CreateTagCommand(object):
    def __init__(self, payload: TagBase):
        self.payload = payload

    def create_tag(self, db: Session) -> Tag:
        data = jsonable_encoder(self.payload)
        tag = Tag(**data)
        db.add(tag)
        db.commit()
        db.refresh(tag)
        return tag
