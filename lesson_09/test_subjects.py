import os

import pytest
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

load_dotenv()
DB_URL = os.getenv("DB_URL")
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)


@pytest.fixture
def session():
    s = Session()
    yield s
    s.close()


# ============ ТЕСТ 1: добавление предмета ============
def test_add_subject(session):
    # 1. Добавляем
    session.execute(
        text(
            "INSERT INTO subject (subject_id, subject_title) "
            "VALUES (:id, :title)"
        ),
        {"id": 9999, "title": "Тестовый предмет"},
    )
    session.commit()

    # 2. Проверяем, что добавилось
    result = session.execute(
        text(
            "SELECT subject_title FROM subject "
            "WHERE subject_id = :id"
        ),
        {"id": 9999},
    ).fetchone()
    assert result[0] == "Тестовый предмет"

    # 3. Удаляем за собой
    session.execute(
        text("DELETE FROM subject WHERE subject_id = :id"),
        {"id": 9999},
    )
    session.commit()


# ============ ТЕСТ 2: изменение предмета ============
def test_update_subject(session):
    # 1. Создаём
    session.execute(
        text(
            "INSERT INTO subject (subject_id, subject_title) "
            "VALUES (:id, :title)"
        ),
        {"id": 9998, "title": "Старое название"},
    )
    session.commit()

    # 2. Изменяем
    session.execute(
        text(
            "UPDATE subject SET subject_title = :new "
            "WHERE subject_id = :id"
        ),
        {"new": "Новое название", "id": 9998},
    )
    session.commit()

    # 3. Проверяем
    result = session.execute(
        text(
            "SELECT subject_title FROM subject "
            "WHERE subject_id = :id"
        ),
        {"id": 9998},
    ).fetchone()
    assert result[0] == "Новое название"

    # 4. Удаляем
    session.execute(
        text("DELETE FROM subject WHERE subject_id = :id"),
        {"id": 9998},
    )
    session.commit()


# ============ ТЕСТ 3: удаление предмета ============
def test_delete_subject(session):
    # 1. Создаём
    session.execute(
        text(
            "INSERT INTO subject (subject_id, subject_title) "
            "VALUES (:id, :title)"
        ),
        {"id": 9997, "title": "Удаляемый предмет"},
    )
    session.commit()

    # 2. Удаляем
    session.execute(
        text("DELETE FROM subject WHERE subject_id = :id"),
        {"id": 9997},
    )
    session.commit()

    # 3. Проверяем, что его нет
    result = session.execute(
        text(
            "SELECT subject_title FROM subject "
            "WHERE subject_id = :id"
        ),
        {"id": 9997},
    ).fetchone()
    assert result is None
