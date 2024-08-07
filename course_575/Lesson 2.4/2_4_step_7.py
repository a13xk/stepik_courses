from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver

browser = webdriver.Chrome()
# # говорим WebDriver ждать все элементы в течение 5 секунд
# browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait2.html")

# button = browser.find_element_by_id("verify")
button = WebDriverWait(driver=browser, timeout=5).until(EC.element_to_be_clickable(locator=(By.ID, "verify")))
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text
