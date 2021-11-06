from sqlalchemy.orm.session import Session
from app.models.article import Article


class ArticlesQuery(object):
    def get_articles(self, db: Session):
        return db.query(Article).all()
