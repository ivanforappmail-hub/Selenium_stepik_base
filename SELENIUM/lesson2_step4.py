from selenium import webdriver
from selenium.webdriver.common import by
import time
import math

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'
browser.get(link)

try:
    knopka = browser.find_element(By.TAG_NAME, 'button')
    knopka.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    chislo = browser.find_element(By.ID, 'input_value').text
    y = calc(chislo)
    otvet = browser.find_element(By.ID, 'answer')
    otvet.send_keys(str(y))
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    time.sleep(5)
    browser.quit()