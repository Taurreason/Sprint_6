import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.yandex_locators import YandexInputs


class YandexPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ожидаем загрузку страницы Яндекса (по полю поиска)")
    def wait_for_yandex_page(self):
        return self.wait.until(EC.visibility_of_element_located(YandexInputs.SEARCH_FIELD))
