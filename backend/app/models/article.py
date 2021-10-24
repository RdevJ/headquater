from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Article(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    title_slug = Column(String, index=True)
    content = Column(String)
