from selenium.webdriver.common.by import By


class Inputs:
    DATE = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    COMMENT_COURIER = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")


class Dropdown:
    DAYS_RENT = (By.XPATH, "//div[@class='Dropdown-control' and @aria-haspopup='listbox']")
    DAY_1_RENT = (By.XPATH, "//div[@class='Dropdown-option' and normalize-space(text())='сутки']")


class Buttons:
    ORDER_RENT = (
        By.XPATH,
        "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and normalize-space()='Заказать']"
    )


class Header:
    RENT = (By.CLASS_NAME, 'Order_Header__BZXOb')


class CheckBox:
    COLOR_BLACK_PEARL_INPUT = (By.ID, "black")
    COLOR_BLACK_PEARL_LABEL = (By.XPATH, "//label[@for='black']")
    COLOR_GREY_HOPELESSNESS_LABEL = (By.CSS_SELECTOR, "label[for='grey']")
    COLOR_GREY_HOPELESSNESS_INPUT = (By.ID, "grey")

    
class DynamicLocators:
    @staticmethod
    def date_picker_by_day_month_year(day, month_name, year):
        return By.XPATH, f"//div[contains(@aria-label, '{day}-е {month_name} {year} г.')]"
