from selenium import webdriver
import time
import math


link = 'http://suninjuly.github.io/redirect_accept.html'


def calc(x):
    return math.log(abs(12*math.sin(int(x))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.trollface.btn")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_css_selector("#input_value").text
    y = str(calc(x))

    answer = browser.find_element_by_css_selector("input#answer.form-control")
    answer.send_keys(y)

    submit = browser.find_element_by_css_selector("button.btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()







