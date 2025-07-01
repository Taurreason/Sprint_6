import allure
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators import Inputs, Dropdown, Buttons, Header, DynamicLocators
from data import colors_samokat, months
from pages.base_page import BasePage


class OrderRentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Заполняем форму аренды полностью")
    def fill_rent_order_form(self, color_name, comment):
        self.wait.until(EC.visibility_of_element_located(Header.RENT))

        self.click(Inputs.DATE)

        tomorrow = datetime.now() + timedelta(days=1)
        day = tomorrow.day
        month_name = months[tomorrow.month - 1]
        year = tomorrow.year
        date_locator = DynamicLocators.date_picker_by_day_month_year(day, month_name, year)
        self.click(date_locator)

        self.click(Dropdown.DAYS_RENT)
        self.click(Dropdown.DAY_1_RENT)

        self.click(colors_samokat[color_name])
        self.enter_text(Inputs.COMMENT_COURIER, comment)
        self.click(Buttons.ORDER_RENT)
