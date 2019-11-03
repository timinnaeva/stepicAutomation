from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x1 = browser.find_element_by_id("num1").text
    x2 = browser.find_element_by_id("num2").text

    summa = str(int(x1) + int(x2))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(summa)

    submit = browser.find_element_by_css_selector("button.btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()