from typing import List, Optional

import pytest
from app.models.article import Article
from app.schemas.article import ArticleCreate
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from main import app
from sqlalchemy.orm import Session

CREATE_ARTICLE_URL = 'api/v1/articles'


def _is_created(db: Session, title: str, title_slug: str, content: str, items: Optional[List[int]]):
    return db.query(Article).filter(
        Article.title_slug == title_slug,
        Article.title == title,
        Article.content == content,
    ).first()


@pytest.fixture(scope="function")
def local_db(db: Session):
    article = Article(
        title='foo',
        title_slug='bar',
        content='baz',
    )
    article_1 = Article(
        title='foo1',
        title_slug='bar1',
        content='baz1',
    )
    db.add_all([article, article_1])
    db.commit()
    yield db


def test_create_article_success(client: TestClient, db: Session):
    payload = {
        'title': 'foo',
        'title_slug': 'bar',
        'content': 'baz',
        'items': [],
    }
    response = client.post(app.url_path_for('create_article'), json=payload)

    assert response.status_code == status.HTTP_200_OK
    assert _is_created(
        db=db,
        title='foo',
        title_slug='bar',
        content='baz',
        items=[],
    )


def test_read_articles_success(client: TestClient, local_db: Session):
    response = client.get(app.url_path_for('read_articles'))

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 2


def test_read_article_success(client: TestClient, local_db: Session):
    response = client.get(app.url_path_for('read_article', **{'article_slug': 'bar1'}))

    article = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert article
    assert article['title'] == 'foo1'
    assert article['title_slug'] == 'bar1'
    assert article['content'] == 'baz1'


def test_update_article_success(client: TestClient, local_db: Session):
    payload = ArticleCreate(
        title='abc',
        title_slug='def',
        content='ghi',
        tags=None,
    )
    response = client.put(
        app.url_path_for('update_article', **{'article_slug': 'bar1'}),
        json=jsonable_encoder(payload),
    )

    article = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert article
    assert article['title'] == 'abc'
    assert article['title_slug'] == 'def'
    assert article['content'] == 'ghi'
    assert _is_created(
        db=local_db,
        title='abc',
        title_slug='def',
        content='ghi',
        items=[],
    )


def test_delete_article_success(client: TestClient, local_db: Session):
    response = client.delete(app.url_path_for('delete_article', **{'article_slug': 'bar1'}))

    article = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert article
    assert article['title'] == 'foo1'
    assert article['title_slug'] == 'bar1'
    assert article['content'] == 'baz1'
    assert not _is_created(
        db=local_db,
        title='foo1',
        title_slug='bar1',
        content='baz1',
        items=[],
    )
