from typing import List, Optional

from app.models.article import Article
from fastapi import status
from fastapi.testclient import TestClient
from main import app
from sqlalchemy.orm import Session

CREATE_ARTICLE_URL = 'api/v1/articles'


def _is_created(db: Session, title: str, title_slug: str, content: str, items: Optional[List[int]]):
    # return db.query(Article).filter(
    #     Article.title_slug == title_slug,
    #     Article.title == title,
    #     Article.content == content,
    # ).first()
    return db.query(Article).count()


def test_create_article_success(client: TestClient, db: Session):
    payload = {
        'title': 'foo',
        'title_slug': 'bar',
        'content': 'baz',
        'items': [],
    }
    response = client.post(app.url_path_for('create_article'), json=payload, allow_redirects=True)

    assert response.status_code == status.HTTP_200_OK
    assert _is_created(
        db=db,
        title='foo',
        title_slug='bar',
        content='baz',
        items=[],
    ) == 1
