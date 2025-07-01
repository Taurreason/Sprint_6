import allure
from selenium.webdriver.support import expected_conditions as EC
from locators import Header, Buttons
from pages.base_page import BasePage


class PopupOrderPlacedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ожидаем оформление заказа и переходим к статусу")
    def view_order_status(self):
        self.wait.until(EC.visibility_of_element_located(Header.PLACED_ORDER))
        self.wait.until(EC.element_to_be_clickable(Buttons.STATUS_BUTTON))
        self.click(Buttons.STATUS_BUTTON)
