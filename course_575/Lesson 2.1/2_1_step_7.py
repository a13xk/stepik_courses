from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
#


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(url=link)

    chest_image = browser.find_element_by_id(id_="treasure")
    x_value = chest_image.get_attribute(name="valuex")
    y_value = calc(x=x_value)

    input_form = browser.find_element_by_id(id_="answer")
    input_form.send_keys(y_value)

    robots_checkbox = browser.find_element_by_id(id_="robotCheckbox")
    robots_checkbox.click()

    robots_rule_radiobutton = browser.find_element_by_id(id_="robotsRule")
    robots_rule_radiobutton.click()

    submit_button = browser.find_element_by_class_name(name="btn")
    submit_button.click()

finally:
    time.sleep(20)
    browser.quit()

