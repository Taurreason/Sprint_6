import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver  # возвращаем драйвер тесту
    driver.quit()