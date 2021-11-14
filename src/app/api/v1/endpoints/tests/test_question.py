from typing import List, Optional, Tuple

import pytest
from app.models.question import Question
from app.schemas.question import QuestionBase, QuestionCreate
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from main import app
from sqlalchemy.orm import Session

CREATE_ARTICLE_URL = 'api/v1/articles'


def _is_created(db: Session, title: str, content: str):
    return db.query(Question).filter(
        Question.title == title,
        Question.content == content,
    ).first()


@pytest.fixture(scope="function")
def local_db(db: Session):
    question = Question(
        title='foo',
        content='baz',
    )
    question_1 = Question(
        title='foo1',
        content='baz1',
    )
    db.add_all([question, question_1])
    db.commit()
    db.refresh(question)
    db.refresh(question_1)
    yield db, [question, question_1]

    db.rollback()


def test_create_question_success(client: TestClient, db: Session):
    payload = {
        'title': 'foo',
        'content': 'baz',
    }
    response = client.post(app.url_path_for('create_question'), json=payload)

    assert response.status_code == status.HTTP_200_OK
    assert _is_created(
        db=db,
        title='foo',
        content='baz',
    )


def test_read_questions_success(client: TestClient, local_db: Session):
    response = client.get(app.url_path_for('read_questions'))

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 2


def test_update_question_success(client: TestClient, local_db: Tuple[Session, List[Question]]):
    session, questions_db = local_db
    payload = QuestionBase(
        title='abc',
        content='ghi',
    )
    response = client.put(
        app.url_path_for('update_question', **{'question_id': questions_db[0].id}),
        json=jsonable_encoder(payload),
    )

    question = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert question
    assert question['title'] == 'abc'
    assert question['content'] == 'ghi'
    assert _is_created(
        db=session,
        title='abc',
        content='ghi',
    )


def test_delete_question_success(client: TestClient, local_db: Tuple[Session, List[Question]]):
    session, questions_db = local_db
    response = client.delete(app.url_path_for('delete_question', **{'question_id': questions_db[1].id}))

    question = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert question
    assert question['title'] == 'foo1'
    assert question['content'] == 'baz1'
    assert not _is_created(
        db=session,
        title='foo1',
        content='baz1',
    )
