import allure
from selenium.webdriver.support import expected_conditions as EC
from locators import Header, Buttons
from pages.base_page import BasePage


class PopupOrderConfirmPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Подтверждаем оформление заказа")
    def confirm_order(self):
        self.wait.until(EC.visibility_of_element_located(Header.CONFIRM_ORDER))
        self.click(Buttons.POPUP_PLACE_ORDER_YES)
