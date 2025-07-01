import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators import Inputs, Dropdown, Buttons, Header, DynamicLocators
from pages.base_page import BasePage
from data import ORDER_PAGE_URL

class OrderUserPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Заполняем форму пользователя полностью")
    def fill_order_form(self, name, surname, address, metro_station, phone):
        self.wait.until(EC.visibility_of_element_located(Header.ORDER_DATA))
        self.enter_text(Inputs.NAME, name)
        self.enter_text(Inputs.SURNAME, surname)
        self.enter_text(Inputs.ADDRESS, address)

        self.click(Dropdown.METRO_INPUT)
        option_locator = DynamicLocators.metro_option_by_name(metro_station)
        option = self.wait.until(EC.presence_of_element_located(option_locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option)
        self.wait.until(EC.element_to_be_clickable(option_locator)).click()

        self.enter_text(Inputs.PHONE_NUMBER, phone)
        self.click(Buttons.NEXT)

    @allure.step("Ожидаем редирект на страницу заказа")
    def wait_until_redirect_to_order_page(self):
        self.wait.until(EC.url_to_be(ORDER_PAGE_URL))
        return self.driver.current_url
