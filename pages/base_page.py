import allure
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открываем страницу по ссылке: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Ожидаем переход по ссылке: {url}")
    def is_opened(self, url):
        self.wait.until(EC.url_contains(url))

    @allure.step("Кликаем по элементу")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Вводим текст в поле")
    def enter_text(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    @allure.step("Получаем текст элемента")
    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Скроллим до элемента")
    def scroll_to_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Скроллим в конец страницы")
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    @allure.step("Ожидаем появления новой вкладки и переключаемся на неё")
    def switch_to_new_tab_when_opened(self, initial_handles):
        self.wait.until(lambda d: len(d.window_handles) > len(initial_handles))
        new_tab = [h for h in self.driver.window_handles if h not in initial_handles][0]
        self.driver.switch_to.window(new_tab)


    @allure.step("Получаем текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Скроллим до элемента через JS")
    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
