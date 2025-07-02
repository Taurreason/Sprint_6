import allure
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from data import BASE_URL
from locators.main_locators import Buttons


class Main(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открываем главную страницу и принимаем cookies")
    def open_main_page_and_accept_cookies(self):
        self.open(BASE_URL)
        self.click(Buttons.COOKIE_ACCEPT)

    @allure.step("Прокручиваем до элемента и кликаем по кнопке")
    def scroll_and_click_button(self, locator):
        self.scroll_to_element(locator)
        self.click(locator)

    @allure.step("Кликаем по элементу после ожидания кликабельности")
    def wait_and_click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        self.click(locator)
