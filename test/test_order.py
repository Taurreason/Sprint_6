import pytest
import allure
from pages.main_page import Main
from pages.order_user_page import OrderUserPage
from pages.order_rent_page import OrderRentPage
from pages.popup_order_confirm_page import PopupOrderConfirmPage
from pages.popup_order_placed_page import PopupOrderPlacedPage
from pages.status_order_page import StatusOrderPage
from locators import Buttons
from data import test_user_data, UserData, RentData



@allure.epic("Оформление заказа")
class TestOrder:


    @allure.title("Проверка оформления заказа самоката")
    @allure.description("Проверяем, что данные пользователя и аренды заполняются корректно")
    @pytest.mark.parametrize("user, rent", test_user_data)
    def test_input_valid_order_data(
        self, driver, user: UserData, rent: RentData):
        main_page = Main(driver)
        user_form = OrderUserPage(driver)
        rent_form = OrderRentPage(driver)
        popup_confirm = PopupOrderConfirmPage(driver)
        popup_placed = PopupOrderPlacedPage(driver)
        status_page = StatusOrderPage(driver)

        with allure.step("Открываем главную страницу и принимаем cookies"):
            main_page.open_main_page_and_accept_cookies()

        with allure.step("Прокручиваем до кнопки 'Заказать' и кликаем"):
            main_page.scroll_and_click_button(Buttons.ORDER_MAIN_UP)

        with allure.step("Заполняем форму пользователя"):
            user_form.fill_order_form(
                user.name, user.surname, user.address, user.metro, user.phone
            )

        with allure.step("Заполняем форму аренды"):
            rent_form.fill_rent_order_form(rent.color, rent.comment)

        with allure.step("Подтверждаем заказ"):
            popup_confirm.confirm_order()

        with allure.step("Переходим к статусу заказа"):
            popup_placed.view_order_status()

        with allure.step("Проверяем, что страница статуса заказа отображается"):
            assert status_page.wait_for_status_page().is_displayed()
