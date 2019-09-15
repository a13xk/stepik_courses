from selenium import webdriver


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

browser.implicitly_wait(time_to_wait=5)

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")


assert "successful" in message.text

browser.quit()
