from typing import List, Optional

from app.datastore.queries.tags.tag import TagQuery
from app.models.article import Article
from app.schemas.article import ArticleCreate
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm.session import Session


class AddArticleCommand(object):
    def __init__(self, payload: ArticleCreate):
        self.payload = payload

    def add_article(self, db: Session) -> Article:
        data = jsonable_encoder(self.payload, exclude={'tags'})
        article = Article(**data)
        self._assign_tags(db=db, tags=self.payload.tags, article=article)
        db.add(article)
        db.commit()
        db.refresh(article)
        return article

    def _assign_tags(self, db: Session, tags: Optional[List[int]], article: Article):
        if not tags:
            return

        for tag in tags:
            tag = TagQuery().get_tag(tag_id=tag, db=db)
            article.tags.append(tag)
