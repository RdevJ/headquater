from app.db.base_class import Base
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Integer, String


class Answer(Base):
    id = Column(Integer, primary_key=True, index=True)
    label = Column(String(255))
    is_correct = Column(Boolean)
    question_id = Column(Integer, ForeignKey('question.id'))
