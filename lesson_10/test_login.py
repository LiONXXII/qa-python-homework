import allure
from selenium import webdriver
from pages import LoginPage


@allure.feature("Авторизация")
class TestLogin:
    """Тесты для проверки входа на сайт Saucedemo."""

    def setup_method(self):
        """Запускается перед каждым тестом."""
        self.driver = webdriver.Chrome()
        self.page = LoginPage(self.driver)

    def teardown_method(self):
        """Запускается после каждого теста."""
        self.driver.quit()

    @allure.title("Успешный вход")
    @allure.description(
        "Проверяем, что с правильными данными мы попадаем на страницу товаров"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_success(self):
        with allure.step("Открыть страницу логина"):
            self.page.open("https://www.saucedemo.com/")

        with allure.step("Ввести данные"):
            self.page.enter_username("standard_user")
            self.page.enter_password("secret_sauce")
            self.page.click_login()

        with allure.step("Проверить, что попали на страницу товаров"):
            assert self.page.get_title() == "Swag Labs"

    @allure.title("Неуспешный вход")
    @allure.description("Проверяем, что с неверным паролем вход не происходит")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_failed(self):
        with allure.step("Открыть страницу логина"):
            self.page.open("https://www.saucedemo.com/")

        with allure.step("Ввести неверный пароль"):
            self.page.enter_username("standard_user")
            self.page.enter_password("wrong_password")
            self.page.click_login()

        with allure.step("Проверить, что остались на странице логина"):
            assert "inventory" not in self.driver.current_url
