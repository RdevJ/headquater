from app.db.session import SessionLocal
from app.models.article import Article


class AddArticleCommand(object):
    def __init__(self, payload):
        self.payload = payload

    def add_article(self):
        session = SessionLocal()
        article = Article(
            title='Pierwszy w bazie',
            title_slug='pierwszy-w-bazie',
            content='I to bedzie koniec na dzis jesli uda sie dziada dodac'
        )
        session.add(article)
        session.commit()
