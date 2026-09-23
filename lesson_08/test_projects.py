import pytest
import requests
from config import BASE_URL, HEADERS

USER_ID = "7817c003-4325-475b-a80c-9a7389b15408"


@pytest.fixture
def created_project_id():
    """Создаёт проект, возвращает его ID, затем удаляет."""
    data = {
        "title": "Test Project",
        "users": {USER_ID: "admin"}
    }
    response = requests.post(
        f"{BASE_URL}/api-v2/projects",
        json=data,
        headers=HEADERS
    )
    assert response.status_code == 201, response.text
    project_id = response.json()["id"]

    yield project_id

    # Удаляем проект после теста
    requests.delete(
        f"{BASE_URL}/api-v2/projects/{project_id}",
        headers=HEADERS
    )


# ========== ПОЗИТИВНЫЕ ТЕСТЫ ==========

def test_post_project_positive():
    """Позитивный тест: создание проекта"""
    data = {
        "title": "My New Project",
        "users": {USER_ID: "admin"}
    }
    response = requests.post(
        f"{BASE_URL}/api-v2/projects",
        json=data,
        headers=HEADERS
    )
    assert response.status_code == 201, response.text
    assert "id" in response.json()

    # Очистка
    project_id = response.json()["id"]
    requests.delete(
        f"{BASE_URL}/api-v2/projects/{project_id}",
        headers=HEADERS
    )


def test_put_project_positive(created_project_id):
    """Позитивный тест: обновление проекта"""
    project_id = created_project_id
    data = {"title": "Updated Project Name"}
    response = requests.put(
        f"{BASE_URL}/api-v2/projects/{project_id}",
        json=data,
        headers=HEADERS
    )
    assert response.status_code == 200, response.text


def test_get_project_positive(created_project_id):
    """Позитивный тест: получение проекта"""
    project_id = created_project_id
    response = requests.get(
        f"{BASE_URL}/api-v2/projects/{project_id}",
        headers=HEADERS
    )
    assert response.status_code == 200, response.text
    assert response.json().get("id") == project_id


# ========== НЕГАТИВНЫЕ ТЕСТЫ ==========

def test_post_project_negative_missing_title():
    """Негативный тест: создание без обязательного поля title"""
    data = {"users": {USER_ID: "admin"}}  # пропущен title
    response = requests.post(
        f"{BASE_URL}/api-v2/projects",
        json=data,
        headers=HEADERS
    )
    assert response.status_code == 400, response.text
    # Ответ может быть списком или словарём — приводим к строке
    error_text = str(response.json()).lower()
    assert "title" in error_text or "required" in error_text


def test_put_project_negative_invalid_id():
    """Негативный тест: обновление несуществующего проекта"""
    fake_id = "00000000-0000-0000-0000-000000000000"
    data = {"title": "New Name"}
    response = requests.put(
        f"{BASE_URL}/api-v2/projects/{fake_id}",
        json=data,
        headers=HEADERS
    )
    assert response.status_code == 404, response.text


def test_get_project_negative_invalid_id():
    """Негативный тест: получение несуществующего проекта"""
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = requests.get(
        f"{BASE_URL}/api-v2/projects/{fake_id}",
        headers=HEADERS
    )
    assert response.status_code == 404, response.text
