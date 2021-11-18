from typing import List, Optional

from app.schemas.tags import TagDb
from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    title_slug: str
    content: str


class ArticleCreate(ArticleBase):
    tags: Optional[List[int]]
    questions: Optional[List[int]]


class ArticleDb(ArticleBase):
    id: int
    tags: Optional[List[TagDb]]

    class Config:
        orm_mode = True
