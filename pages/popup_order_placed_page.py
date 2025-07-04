import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.popup_order_placed_locators import (
    PopupOrderPlacedHeader,
    PopupOrderPlacedButtons,
)
from pages.base_page import BasePage


class PopupOrderPlacedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ожидаем оформление заказа и переходим к статусу")
    def view_order_status(self):
        self.wait.until(EC.visibility_of_element_located(PopupOrderPlacedHeader.PLACED_ORDER))
        self.wait.until(EC.element_to_be_clickable(PopupOrderPlacedButtons.STATUS_BUTTON))
        self.click(PopupOrderPlacedButtons.STATUS_BUTTON)
