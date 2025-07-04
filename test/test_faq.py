import pytest
import allure
from pages.faq_page import FaqPage
from pages.main_page import Main
from data import expected_faq_texts


@allure.epic("Вопросы о важном")
@allure.feature("Раскрытие ответов по вопросам")
class TestFaq:

    @allure.title("Проверка раскрытия вопроса в секции Вопросы о важном")
    @allure.description("Проверяем, что при клике на вопрос отображается ожидаемый текст ответа.")
    @pytest.mark.parametrize("question_index", list(expected_faq_texts.keys()))
    def test_faq_question_expands(self, driver, question_index):
        main_page = Main(driver)
        faq_page = FaqPage(driver)

        with allure.step("Открываем главную страницу и принимаем cookies"):
            main_page.open_main_page_and_accept_cookies()

        with allure.step(f"Скроллим и кликаем по вопросу #{question_index}"):
            faq_page.scroll_to_element_and_click(question_index)

        with allure.step(f"Получаем и проверяем текст ответа на вопрос #{question_index}"):
            answer_text = faq_page.get_answer_text(question_index)
            expected_text = expected_faq_texts[question_index]

            allure.attach(answer_text, name="Полученный ответ", attachment_type=allure.attachment_type.TEXT)
            assert expected_text in answer_text, f"Ожидали: {expected_text}\nПолучили: {answer_text}"
