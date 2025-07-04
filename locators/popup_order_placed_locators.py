from selenium.webdriver.common.by import By

class PopupOrderPlacedHeader:
    PLACED_ORDER = (
        By.XPATH,
        "//div[@class='Order_ModalHeader__3FDaJ' and contains(normalize-space(),'Заказ оформлен')]"
    )


class PopupOrderPlacedButtons:
    STATUS_BUTTON = (
        By.XPATH,
        "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and normalize-space()='Посмотреть статус']"
    )
