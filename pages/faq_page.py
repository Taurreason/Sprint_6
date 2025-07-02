import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.faq_locators import FaqLocators


class FaqPage(BasePage):

    def __init__(self, driver):
         super().__init__(driver)


    @allure.step("Получаем текст ответа на вопрос #{index}")
    def get_answer_text(self, index: int) -> str:
        answer_locator = FaqLocators.answer(index)
        return self.wait.until(EC.visibility_of_element_located(answer_locator)).text

    @allure.step("Скроллим и кликаем по вопросу #{index}")
    def scroll_to_element_and_click(self, index):
        locator = FaqLocators.question(index)
        # Ожидание, что элемент видим
        element = self.wait.until(EC.visibility_of_element_located(locator))
        # Прокрутка к элементу
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.wait.until(EC.element_to_be_clickable(locator)).click()
