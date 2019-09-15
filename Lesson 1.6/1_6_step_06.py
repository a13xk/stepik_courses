from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/simple_form_find_task.html"

browser = webdriver.Chrome()
browser.get(url=url)
button = browser.find_element(By.ID, "submit")
button.click()

browser.quit()

