from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm.session import Session
from app.models.article import Article
from app.schemas.article import ArticleCreate


class AddArticleCommand(object):
    def __init__(self, payload: ArticleCreate):
        self.payload = payload

    def add_article(self, db: Session) -> Article:
        data = jsonable_encoder(self.payload)
        article = Article(**data)
        db.add(article)
        db.commit()
        db.refresh(article)
        return article
