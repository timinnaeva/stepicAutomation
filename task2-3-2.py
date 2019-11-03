from selenium import webdriver
import time
import math


def calc(x):
    return math.log(abs(12*math.sin(int(x))))


link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_id("input_value").text
    y = str(calc(int(x)))

    answer = browser.find_element_by_css_selector("input#answer.form-control")
    answer.send_keys(y)

    submit = browser.find_element_by_css_selector("button.btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()

