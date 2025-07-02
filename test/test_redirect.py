# import pytest
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import Main
from pages.order_user_page import OrderUserPage
from pages.yandex_page import YandexPage
from locators.main_locators import Buttons
import time


@allure.epic("Редиректы")
@allure.feature("Редирект по логотипам")
class TestRedirect:

    @allure.title("Редирект на главную страницу по логотипу Самокат")
    @allure.description("Проверяем, что при клике на логотип Самоката происходит переход на главную страницу.")
    def test_redirect_logo_samokat_to_base_page(self, driver):
        wait = WebDriverWait(driver, 10)
        main_page = Main(driver)
        order_user_page = OrderUserPage(driver)

        with allure.step("Открытие главной страницы и принятие cookies"):
            main_page.open_main_page_and_accept_cookies()

        with allure.step("Скролл до нижней кнопки 'Заказать' и клик"):
            wait.until(EC.element_to_be_clickable(Buttons.ORDER_MAIN_DOWN))
            main_page.scroll_to_element(Buttons.ORDER_MAIN_DOWN)
            main_page.click(Buttons.ORDER_MAIN_DOWN)

        with allure.step("Ожидаем редирект на страницу /order"):
            order_user_page.wait_until_redirect_to_order_page()

        with allure.step("Клик по логотипу Самокат"):
            main_page.wait_and_click(Buttons.LOGO_SAMOKAT)

        with allure.step("Проверка редиректа на главную страницу"):
            current_url = main_page.get_current_url()
            assert current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title("Редирект по логотипу Яндекса в новую вкладку")
    @allure.description("Проверяем, что при клике на логотип Яндекса открывается новая вкладка с Яндексом.")
    def test_redirect_logo_yandex_to_yandex(self, driver):
        # wait = WebDriverWait(driver, 10)
        main_page = Main(driver)
        yandex_page = YandexPage(driver)

        with allure.step("Открытие главной страницы и принятие cookies"):
            main_page.open_main_page_and_accept_cookies()

        with allure.step("Сохраняем текущие вкладки браузера"):
            initial_tabs = driver.window_handles

        with allure.step("Клик по логотипу Яндекса"):
            main_page.wait_and_click(Buttons.LOGO_YANDEX)

        with allure.step("Ожидаем появления новой вкладки и переключаемся на неё"):
            main_page.switch_to_new_tab_when_opened(initial_tabs)
            time.sleep(10)

        with allure.step("Проверка, что открылась страница Яндекса"):
            search_field = yandex_page.wait_for_yandex_page()
            current_url = main_page.get_current_url()

            assert (
                ("yandex" in current_url.lower() or "ya.ru" in current_url.lower())
                and search_field.is_displayed()
            )
