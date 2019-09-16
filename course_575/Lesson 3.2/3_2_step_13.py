import unittest
from selenium import webdriver
import time


class TestRegistration(unittest.TestCase):

    def test_registration1(self):

        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector('.first_block .first')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('.first_block .second')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('.first_block .third')
        input3.send_keys("simpl@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual(first="Congratulations! You have successfully registered!",
                         second=welcome_text)

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()
    #

    def test_registration2(self):

        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector('.first_block .first')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('.first_block .second')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('.first_block .third')
        input3.send_keys("simpl@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual(first="Congratulations! You have successfully registered!",
                         second=welcome_text)

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()
    #


if __name__ == '__main__':
    unittest.main()
