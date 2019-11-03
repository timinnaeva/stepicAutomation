from selenium import webdriver
import time
import os

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_name("firstname")
    name.send_keys("Ваня")
    surname = browser.find_element_by_name("lastname")
    surname.send_keys("Иванов")
    email = browser.find_element_by_name("email")
    email.send_keys("bbb@bb.bu")
    choose_file = browser.find_element_by_id("file")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    choose_file.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

