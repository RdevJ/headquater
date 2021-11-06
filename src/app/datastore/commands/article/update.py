from typing import Optional
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import update
from app.models.article import Article
from app.schemas.article import ArticleBase


class UpdateArticleCommand(object):
    def __init__(self, payload: ArticleBase, article_slug: str):
        self.payload = payload
        self.article_slug = article_slug

    def update_article(self, db: Session) -> Optional[Article]:
        article = (
            db.query(Article).filter(Article.title_slug == self.article_slug).first()
        )
        if not article:
            return None

        db.execute(
            update(Article).
            where(Article.title_slug == self.article_slug).
            values(self.payload.dict())
        )
        db.commit()
        db.refresh(article)
        return article
