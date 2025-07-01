import allure
from selenium.webdriver.support import expected_conditions as EC
from locators import Inputs
from pages.base_page import BasePage


class YandexPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ожидаем загрузку страницы Яндекса (по полю поиска)")
    def wait_for_yandex_page(self):
        return self.wait.until(EC.visibility_of_element_located(Inputs.YANDEX_SEARCH_FIELD))
