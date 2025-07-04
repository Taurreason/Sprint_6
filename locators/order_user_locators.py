from selenium.webdriver.common.by import By


class Inputs:
    NAME = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    SURNAME = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    ADDRESS = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    PHONE_NUMBER = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")


class Dropdown:
    METRO_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")


class Buttons:
    NEXT = (By.XPATH, "//button[normalize-space(text())='Далее']")


class Header:
    ORDER_DATA = (By.CLASS_NAME, 'Order_Header__BZXOb')


class DynamicLocators:
    @staticmethod
    def metro_option_by_name(station_name):
        return (By.XPATH, f".//div[@class='Order_Text__2broi' and text()='{station_name}']")