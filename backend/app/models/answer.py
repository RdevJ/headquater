from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from app.db.base_class import Base


class Answer(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    is_correct = Column(Boolean)
    question_id = Column(Integer, ForeignKey('question.id'))
