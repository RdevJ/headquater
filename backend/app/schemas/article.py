from typing import List, Optional

from pydantic import BaseModel

from app.schemas.tags import Tag


class Article(BaseModel):
    title: str
    title_slug: str
    content: str
    tags: Optional[List[Tag]]


class ArticleCreate(BaseModel):
    title: str
    title_slug: str
    content: str


class ArticleDb(BaseModel):
    id: int
    title: str
    title_slug: str
    content: str

    class Config:
        orm_mode = True
