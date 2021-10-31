from app.models.tag import Tag
from app.schemas.tags import TagBase
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import update


class UpdateTagCommand(object):
    def __init__(self, payload: TagBase, tag_id: int):
        self.payload = payload
        self.tag_id = tag_id

    def update_tag(self, db: Session) -> Tag:
        tag = (
            db.query(Tag).filter(Tag.id == self.tag_id).first()
        )
        if not tag:
            return None

        db.execute(
            update(Tag).
            where(Tag.id == self.tag_id).
            values(self.payload.dict())
        )
        db.commit()
        db.refresh(tag)
        return tag
