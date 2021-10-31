from sqlalchemy.orm.session import Session
from app.models.tag import Tag


class DeleteTagCommand(object):
    def __init__(self, tag_id: int):
        self.tag_id = tag_id

    def delete_tag(self, db: Session) -> Tag:
        tag = (
            db.query(Tag).filter(Tag.id == self.tag_id).first()
        )
        if not tag:
            return None

        db.delete(tag)
        db.commit()
        return tag
