import requests
from config import BASE_URL, HEADERS


class ProjectAPI:

    @staticmethod
    def create_project(data):
        """Создание проекта"""
        url = f"{BASE_URL}/api-v2/projects"
        return requests.post(url, json=data, headers=HEADERS)

    @staticmethod
    def get_project(project_id):
        """Получение проекта по ID"""
        url = f"{BASE_URL}/api-v2/projects/{project_id}"
        return requests.get(url, headers=HEADERS)

    @staticmethod
    def update_project(project_id, data):
        """Обновление проекта"""
        url = f"{BASE_URL}/api-v2/projects/{project_id}"
        return requests.put(url, json=data, headers=HEADERS)

    @staticmethod
    def delete_project(project_id):
        """Удаление проекта"""
        url = f"{BASE_URL}/api-v2/projects/{project_id}"
        return requests.delete(url, headers=HEADERS)
