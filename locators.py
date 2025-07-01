from selenium.webdriver.common.by import By


class Header:
    FAQ = (By.CLASS_NAME, 'Home_SubHeader__zwi_E')
    ORDER_DATA = (By.CLASS_NAME, 'Order_Header__BZXOb')
    SAMOKAT_2_DAYS = (By.CLASS_NAME, 'Home_Header__iJKdX')
    RENT = (By.CLASS_NAME, 'Order_Header__BZXOb')
    CONFIRM_ORDER = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
    PLACED_ORDER = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and contains(normalize-space(),'Заказ оформлен')]")
    STATUS_PAGE = (By.CLASS_NAME, 'Track_Content__St6Kn')


class FaqLocators:
    FAQ_DROPDOWN = (By.ID, 'accordion__heading-{index}')
    FAQ_TEXT = (By.ID, 'accordion__panel-{index}')


class Buttons:
    ORDER_MAIN_UP = (By.CSS_SELECTOR, "button.Button_Button__ra12g")
    ORDER_MAIN_DOWN = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and normalize-space()='Заказать']")
    ORDER_RENT = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and normalize-space()='Заказать']")
    STATUS_ORDER = (By.CLASS_NAME, 'Header_Link__1TAG7')
    NEXT = (By.XPATH, "//button[normalize-space(text())='Далее']")
    POPUP_PLACE_ORDER_YES = (By.XPATH, "//button[normalize-space()='Да']")
    STATUS_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and normalize-space()='Посмотреть статус']")
    LOGO_SAMOKAT = (By.CSS_SELECTOR, "img[alt='Scooter']")
    LOGO_YANDEX = (By.CSS_SELECTOR, "img[alt='Yandex']")
    COOKIE_ACCEPT = (By.ID, "rcc-confirm-button")


class Inputs:
    NAME = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    SURNAME = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    ADDRESS = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    PHONE_NUMBER = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    DATE = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    DATE_PICKER_OPTION_TEMPLATE = "//div[@aria-label='Choose {}']"
    COMMENT_COURIER = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")
    YANDEX_SEARCH_FIELD = (By.CSS_SELECTOR, "input[name='text']")

class Dropdown:
    METRO_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    DAYS_RENT = (By.XPATH, "//div[@class='Dropdown-control' and @aria-haspopup='listbox']")
    DAY_1_RENT = (By.XPATH, "//div[@class='Dropdown-option' and normalize-space(text())='сутки']")

class CheckBox:
    COLOR_BLACK_PEARL_INPUT = (By.ID, "black")
    COLOR_BLACK_PEARL_LABEL = (By.XPATH, "//label[@for='black']")
    COLOR_GREY_HOPELESSNESS_LABEL = (By.CSS_SELECTOR, "label[for='grey']")
    COLOR_GREY_HOPELESSNESS_INPUT = (By.ID, "grey")

class DynamicLocators:
    @staticmethod
    def metro_option_by_name(station_name):
        return (By.XPATH, f".//div[@class='Order_Text__2broi' and text()='{station_name}']")

    @staticmethod
    def date_picker_by_day_month_year(day, month_name, year):
        return (By.XPATH, f"//div[contains(@aria-label, '{day}-е {month_name} {year} г.')]")
    
    @staticmethod
    def faq_question_by_index(index: int):
        return (By.ID, f"accordion__heading-{index}")
    
    @staticmethod
    def faq_answer_by_index(index: int):
        return (By.ID, f"accordion__panel-{index}")