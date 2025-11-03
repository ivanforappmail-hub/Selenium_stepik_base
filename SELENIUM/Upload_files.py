from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter first name']")
    input1.send_keys("Vasya")
    input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter last name']")
    input1.send_keys("Petrov")
    input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter email']")
    input1.send_keys("1111@ddwd.rr")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file2.txt')  # добавляем к этому пути имя файла
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)
    element = browser.find_element(By.XPATH, ".btn.btn-primary")
    element.click()

finally:
    time.sleep(5)
    browser.quit()
