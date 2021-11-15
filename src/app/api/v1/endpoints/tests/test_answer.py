from typing import List, Optional, Tuple

import pytest
from app.models.answer import Answer
from app.schemas.answer import AnswerBase
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from main import app
from sqlalchemy.orm import Session


def _is_created(db: Session, label: str, is_correct: bool):
    return db.query(Answer).filter(
        Answer.label == label,
        Answer.is_correct == is_correct,
    ).first()


@pytest.fixture(scope="function")
def local_db(db: Session):
    answer = Answer(
        label='foo',
        is_correct=False,
    )
    answer_1 = Answer(
        label='bar',
        is_correct=True,
    )
    db.add_all([answer, answer_1])
    db.commit()
    db.refresh(answer)
    db.refresh(answer_1)
    yield db, [answer, answer_1]

    db.rollback()


def test_create_answer_success(client: TestClient, db: Session):
    payload = {
        'label': 'foo',
        'is_correct': False,
    }
    response = client.post(app.url_path_for('create_answer'), json=payload)

    assert response.status_code == status.HTTP_200_OK
    assert _is_created(
        db=db,
        label='foo',
        is_correct=False,
    )


def test_read_answers_success(client: TestClient, local_db: Session):
    response = client.get(app.url_path_for('read_answers'))

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 2


def test_update_answer_success(client: TestClient, local_db: Tuple[Session, List[Answer]]):
    session, answers_db = local_db
    payload = AnswerBase(
        label='abc',
        is_correct=True,
    )
    response = client.put(
        app.url_path_for('update_answer', **{'answer_id': answers_db[0].id}),
        json=jsonable_encoder(payload),
    )

    question = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert question
    assert question['label'] == 'abc'
    assert question['is_correct'] == True
    assert _is_created(
        db=session,
        label='abc',
        is_correct=True,
    )


def test_delete_answer_success(client: TestClient, local_db: Tuple[Session, List[Answer]]):
    session, answers_db = local_db
    response = client.delete(app.url_path_for('delete_answer', **{'answer_id': answers_db[1].id}))

    question = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert question
    assert question['label'] == 'bar'
    assert question['is_correct'] == True
    assert not _is_created(
        db=session,
        label='bar',
        is_correct=True,
    )
