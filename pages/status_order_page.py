import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.status_order_locators import StatusOrderHeader
from pages.base_page import BasePage


class StatusOrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ожидаем загрузку страницы статуса заказа")
    def wait_for_status_page(self):
        return self.wait.until(EC.visibility_of_element_located(StatusOrderHeader.STATUS_PAGE))
