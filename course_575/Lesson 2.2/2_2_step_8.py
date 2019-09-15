from selenium import webdriver
import time

import pathlib

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_first_name = browser.find_element_by_name(name="firstname")
    input_first_name.send_keys("Ivan")

    input_last_name = browser.find_element_by_name(name="lastname")
    input_last_name.send_keys("Petrov")

    input_email = browser.find_element_by_name(name="email")
    input_email.send_keys("ivan.petrov@email.ru")

    current_dir = pathlib.Path(__file__).parent
    file_path = str(pathlib.Path(current_dir).joinpath("textfile.txt"))

    input_file = browser.find_element_by_css_selector(css_selector='[type="file"]')
    input_file.send_keys(file_path)

    button = browser.find_element_by_css_selector(".btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

