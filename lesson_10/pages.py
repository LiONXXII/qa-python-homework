import allure
from selenium.webdriver.common.by import By


class BasePage:
    """Базовый класс для всех страниц."""

    def __init__(self, driver):
        """
        Инициализация страницы.

        :param driver: Драйвер браузера
        """
        self.driver = driver

    @allure.step("Открыть страницу {url}")
    def open(self, url: str) -> None:
        """
        Открывает указанный URL.

        :param url: Адрес страницы
        :return: None
        """
        self.driver.get(url)


class LoginPage(BasePage):
    """Класс для страницы авторизации Saucedemo."""

    @allure.step("Ввести логин {username}")
    def enter_username(self, username: str) -> None:
        """
        Вводит имя пользователя.

        :param username: Имя пользователя
        :return: None
        """
        username_field = self.driver.find_element(By.ID, "user-name")
        username_field.send_keys(username)

    @allure.step("Ввести пароль")
    def enter_password(self, password: str) -> None:
        """
        Вводит пароль.

        :param password: Пароль
        :return: None
        """
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)

    @allure.step("Нажать кнопку Login")
    def click_login(self) -> None:
        """
        Нажимает кнопку входа.

        :return: None
        """
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

    @allure.step("Получить заголовок страницы")
    def get_title(self) -> str:
        """
        Возвращает заголовок текущей страницы.

        :return: Заголовок страницы
        """
        return self.driver.title
