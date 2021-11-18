from typing import List, Optional

from app.datastore.queries.tags.tag import TagQuery
from app.models.article import Article
from app.models.question import Question
from app.models.statistics import Statistics
from app.schemas.article import ArticleCreate
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm.session import Session


class AddArticleCommand(object):
    def __init__(self, payload: ArticleCreate, db: Session):
        self.payload = payload
        self.db = db

    def add_article(self) -> Article:
        data = jsonable_encoder(self.payload, exclude={'tags', 'questions'})
        article = Article(**data)
        article.statistics = Statistics()
        self._assign_tags(tags=self.payload.tags, article=article)
        self._assign_questions(questions=self.payload.questions, article=article)
        self.db.add(article)
        self.db.commit()
        self.db.refresh(article)
        return article

    def _assign_tags(self, tags: Optional[List[int]], article: Article):
        if not tags:
            return

        for tag in tags:
            tag = TagQuery().get_tag(tag_id=tag, db=self.db)
            article.tags.append(tag)

    def _assign_questions(self, questions: Optional[List[int]], article: Article):
        if not questions:
            return

        for question_id in questions:
            question = self.db.query(Question).filter(Question.id==question_id).first()
            article.questions.append(question)
