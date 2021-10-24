from typing import Any, List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.datastore.queries.articles.article import ArticleQuery
from app.datastore.queries.articles.list import ArticlesQuery
from app.schemas.article import Article, ArticleCreate, ArticleDb
from app.datastore.commands.article.add import AddArticleCommand
from app.db.dependency import get_db

router = APIRouter()


@router.get("/", response_model=List[ArticleDb])
def read_items(db: Session = Depends(get_db)) -> Any:
    articles = ArticlesQuery().get_articles(db=db)
    return articles


@router.get('/{article_slug}', response_model=ArticleDb)
def read_item(article_slug: str, db: Session = Depends(get_db)) -> Any:
    query = ArticleQuery(article_slug=article_slug)
    article = query.get_article(db=db)

    if not article:
        raise HTTPException(status_code=404, detail="Item not found")

    return article


@router.post('/', status_code=201)
def create_item(article: ArticleCreate) -> None:
    command = AddArticleCommand(payload=article)

    command.add_article()

    return 'added'