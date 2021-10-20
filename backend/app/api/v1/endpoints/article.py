from typing import Any, List

from fastapi import APIRouter, HTTPException

from app.datastore.queries.articles.article import ArticleQuery
from app.datastore.queries.articles.list import ArticlesQuery
from app.schemas.article import Article

router = APIRouter()


@router.get("/", response_model=List[Article])
def read_items() -> Any:
    articles = ArticlesQuery().get_articles()
    return articles


@router.get('/{article_slug}', response_model=Article)
def read_item(article_slug: str) -> Any:
    query = ArticleQuery(article_slug=article_slug)

    article = query.get_article()

    if not article:
        raise HTTPException(status_code=404, detail="Item not found")

    return article
