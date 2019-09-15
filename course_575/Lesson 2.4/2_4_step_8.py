from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
#


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(driver=browser, timeout=15).until(EC.text_to_be_present_in_element(locator=(By.ID, "price"), text_="$100"))
button = browser.find_element_by_id("book")
button.click()

x_value = browser.find_element_by_id(id_="input_value").text
y_value = calc(x=x_value)

answer_form = browser.find_element_by_id(id_="answer")
answer_form.send_keys(y_value)

submit_button = browser.find_element_by_id(id_="solve")
submit_button.click()

time.sleep(15)
browser.quit()
