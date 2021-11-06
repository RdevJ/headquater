from app.models.tag import Tag
from sqlalchemy.orm.session import Session


class TagQuery(object):
    def get_tag(self, tag_id: int, db: Session):
        return db.query(Tag).filter(Tag.id == tag_id).first()
