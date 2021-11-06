from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from app.db.base_class import Base


class Question(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    article_id = Column(Integer, ForeignKey('article.id'))

    answers = relationship('Answer')
