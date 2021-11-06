from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table

from app.db.base_class import Base


association_table = Table(
    'article_tag',
    Base.metadata,
    Column('article_id', ForeignKey('article.id'), primary_key=True),
    Column('tag_id', ForeignKey('tag.id'), primary_key=True),
)


class Article(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    title_slug = Column(String, index=True)
    content = Column(String)

    statistics = relationship("Statistics", back_populates="article", uselist=False)
    tags = relationship("Tag", secondary=association_table)
    questions = relationship('Question')
