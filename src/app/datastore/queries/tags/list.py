from typing import List

from app.models.tag import Tag
from sqlalchemy.orm.session import Session


class TagsQuery(object):
    def get_tags(self, db: Session) -> List[Tag]:
        return db.query(Tag).all()
