from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math
import time

link = 'http://suninjuly.github.io/explicit_wait2.html'


def calc(x):
    return math.log(abs(12*math.sin(int(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_id("book")
    button.click()

    x = browser.find_element_by_id("input_value").text
    y = str(calc(x))

    answer = browser.find_element_by_css_selector("input#answer.form-control")
    answer.send_keys(y)

    submit = browser.find_element_by_id("solve")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()