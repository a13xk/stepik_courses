from selenium import webdriver
import time


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

time.sleep(2)

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")


assert "successful" in message.text

browser.quit()
