from typing import List, Optional

from pydantic import BaseModel

from app.schemas.tags import TagDb


class ArticleBase(BaseModel):
    title: str
    title_slug: str
    content: str


class ArticleCreate(ArticleBase):
    tags: Optional[List[int]]


class ArticleDb(ArticleBase):
    id: int
    tags: Optional[List[TagDb]]

    class Config:
        orm_mode = True
