from selenium.webdriver.common.by import By

class PopupOrderConfirmHeader:
    CONFIRM_ORDER = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')


class PopupOrderConfirmButtons:
    POPUP_PLACE_ORDER_YES = (By.XPATH, "//button[normalize-space()='Да']")
