from typing import Any, List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.datastore.queries.articles.article import ArticleQuery
from app.datastore.queries.articles.list import ArticlesQuery
from app.schemas.article import ArticleCreate, ArticleDb
from app.datastore.commands.article.add import AddArticleCommand
from app.datastore.commands.article.delete import DeleteArticleCommand
from app.db.dependency import get_db

router = APIRouter()


@router.get("/", response_model=List[ArticleDb])
def read_articles(db: Session = Depends(get_db)) -> Any:
    articles = ArticlesQuery().get_articles(db=db)
    return articles


@router.get('/{article_slug}', response_model=ArticleDb)
def read_article(article_slug: str, db: Session = Depends(get_db)) -> Any:
    query = ArticleQuery(article_slug=article_slug)
    article = query.get_article(db=db)

    if not article:
        raise HTTPException(status_code=404, detail="Article not found")

    return article


@router.post('/', response_model=ArticleDb)
def create_article(article: ArticleCreate, db: Session = Depends(get_db)) -> Any:
    article = AddArticleCommand(payload=article).add_article(db=db)

    return article


@router.delete('/{article_slug}', response_model=ArticleDb)
def delete_article(article_slug: str, db: Session = Depends(get_db)) -> Any:
    article = DeleteArticleCommand(article_slug=article_slug).delete_article(db=db)

    if not article:
        raise HTTPException(status_code=404, detail="Article not found")

    return article
