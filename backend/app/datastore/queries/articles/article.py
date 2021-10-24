from sqlalchemy.orm.session import Session
from app.models.article import Article


class ArticleQuery(object):
    def __init__(self, article_slug: str):
        self.article_slug = article_slug

    def get_article(self, db: Session):
        return db.query(Article).filter(
            Article.title_slug == self.article_slug
        ).first()
