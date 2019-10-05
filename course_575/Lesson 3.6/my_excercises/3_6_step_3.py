import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


answer = math.log(int(time.time()))


links = ["https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1"]


# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()


@pytest.mark.parametrize(argnames='link', argvalues=links)
def test_links(browser, link):
    browser.get(link)
    text_area = WebDriverWait(driver=browser, timeout=10).until(
        ec.presence_of_element_located(locator=(By.CLASS_NAME, "ember-text-area"))
    )
    # answer = math.log(int(time.time()))
    text_area.send_keys(str(math.log(int(time.time()))))

    # Locate "Send" button
    button = WebDriverWait(driver=browser, timeout=5).until(
        ec.element_to_be_clickable(locator=(By.CLASS_NAME, "submit-submission")))
    button.click()

    # Feedback
    feedback_pre = WebDriverWait(driver=browser, timeout=5).until(
        ec.presence_of_element_located(locator=(By.CLASS_NAME, "smart-hints__hint"))
    )
    assert "Correct!" == feedback_pre.text
#

