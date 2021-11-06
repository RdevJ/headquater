from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class Statistics(Base):
    id = Column(Integer, primary_key=True, index=True)
    next_repetition = Column(Date)
    knowledge_level = Column(Float)
    last_viewed = Column(Date)
    repetitions = Column(Integer)
    article_id = Column(Integer, ForeignKey('article.id'))

    article = relationship("Article", back_populates="statistics")
