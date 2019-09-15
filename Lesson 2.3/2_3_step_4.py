from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
#


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(url=link)

    journey_button = browser.find_element_by_tag_name(name="button")
    journey_button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    time.sleep(2)

    x_value = browser.find_element_by_id(id_="input_value").text
    y_value = calc(x=x_value)

    answer_form = browser.find_element_by_id(id_="answer")
    answer_form.send_keys(y_value)

    submit_button = browser.find_element_by_class_name(name="btn")
    submit_button.click()
finally:
    time.sleep(20)
    browser.quit()
