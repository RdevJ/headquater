from typing import Optional
from sqlalchemy.orm.session import Session
from app.models.article import Article


class DeleteArticleCommand(object):
    def __init__(self, article_slug: str):
        self.article_slug = article_slug

    def delete_article(self, db: Session) -> Optional[Article]:
        article = (
            db.query(Article).filter(Article.title_slug == self.article_slug).first()
        )
        if not article:
            return None

        db.delete(article)
        db.commit()
        return article
