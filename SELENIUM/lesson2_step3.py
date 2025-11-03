from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

try:
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
    time.sleep(1)
    confirm = browser.switch_to.alert
    confirm.accept()
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    chislo = browser.find_element(By.ID, 'input_value')
    x = chislo.text
    otvet = browser.find_element(By.ID, 'answer')
    otvet.send_keys(str(calc(x)))
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    button.click()

finally:
    time.sleep(5)
    browser.quit()
