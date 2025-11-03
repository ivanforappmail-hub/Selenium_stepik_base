import math
from idlelib.browser import browseable_extension_blocklist

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

try:
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100')
    )
    knopka = browser.find_element(By.ID, "book").click()
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    ur = browser.find_element(By.ID, 'input_value').text
    y = calc(ur)
    otvet = browser.find_element(By.ID, 'answer')
    otvet.send_keys(str(y))
    sub = browser.find_element(By.ID, 'solve')
    sub.click()
finally:
    time.sleep(10)
    browser.quit()