from sqlalchemy.orm.session import Session
from app.models.tag import Tag


class TagsQuery(object):
    def get_tags(self, db: Session):
        return db.query(Tag).all()
