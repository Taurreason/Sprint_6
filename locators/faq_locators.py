from selenium.webdriver.common.by import By

class FaqLocators:
    @staticmethod
    def question(index: int):
        return (By.ID, f"accordion__heading-{index}")

    @staticmethod
    def answer(index: int):
        return (By.ID, f"accordion__panel-{index}")
