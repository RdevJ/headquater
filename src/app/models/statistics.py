from datetime import datetime

from app.db.base_class import Base
from app.settings import settings
from sqlalchemy import Column, Date, Float, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class Statistics(Base):
    id = Column(Integer, primary_key=True, index=True)
    next_repetition = Column(Date, default=datetime.now().date() + settings.INITIAL_REPETITION_TIMEDELTA)
    knowledge_level = Column(Float, default=1.0)
    last_viewed = Column(Date, default=datetime.now().date())
    repetitions = Column(Integer, default=1)
    article_id = Column(Integer, ForeignKey('article.id'))

    article = relationship("Article", back_populates="statistics")
