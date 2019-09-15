from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(url=link)

    num1 = int(browser.find_element_by_id(id_="num1").text)
    num2 = int(browser.find_element_by_id(id_="num2").text)
    sum_of_numbers = str(num1 + num2)

    select_obj = Select(browser.find_element_by_id(id_="dropdown"))
    select_obj.select_by_value(value=sum_of_numbers)

    submit_button = browser.find_element_by_class_name(name="btn")
    submit_button.click()
finally:
    time.sleep(20)
    browser.quit()
