from locators.order_rent_locators import CheckBox
from dataclasses import dataclass

# Базовый адрес
BASE_URL = 'https://qa-scooter.praktikum-services.ru/'

# Пути (эндпоинты)
YANDEX_URL = 'https://ya.ru/'
ORDER_PAGE_PATH = 'order'
ORDER_PAGE_URL = BASE_URL + ORDER_PAGE_PATH

expected_faq_texts = {
0: "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
1: "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
2: "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
3: "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
4: "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
5: "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
6: "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
7: "Да, обязательно. Всем самокатов! И Москве, и Московской области."
}

# Структуры данных
@dataclass
class UserData:
    name: str
    surname: str
    address: str
    metro: str
    phone: str

@dataclass
class RentData:
    color: str
    comment: str

# Набор данных для параметризации тестов
test_user_data = [
    (
        UserData("Иван", "Васильевич", "Москва, улица Тимофеева, дом 2, квартира 20", "Красносельская", "+79991234567"),
        RentData("black", "Оставлю чаевые, если привезете на час раньше")
    ),
    (
        UserData("Петр", "Петров", "Санкт-Петербург, Невский пр. 100", "Лубянка", "+79997654321"),
        RentData("grey", "Не оставлю чаевые, можете не торопиться")
    )
]

colors_samokat = {
        "black": CheckBox.COLOR_BLACK_PEARL_LABEL,
        "grey": CheckBox.COLOR_GREY_HOPELESSNESS_LABEL
    }

months = [
    "января","февраля","марта","апреля","мая","июня",
    "июля","августа","сентября","октября","ноября","декабря"
]