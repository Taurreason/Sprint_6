from selenium.webdriver.common.by import By


class Buttons:
    ORDER_MAIN_UP = (By.CSS_SELECTOR, "button.Button_Button__ra12g")
    ORDER_MAIN_DOWN = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and normalize-space()='Заказать']")
    LOGO_SAMOKAT = (By.CSS_SELECTOR, "img[alt='Scooter']")
    LOGO_YANDEX = (By.CSS_SELECTOR, "img[alt='Yandex']")
    COOKIE_ACCEPT = (By.ID, "rcc-confirm-button")