from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    # Ваш код, который заполняет обязательные поля
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element(By.CSS_SELECTOR, '.nowrap#input_value')
    x = x_element.text

    button = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script("window.scrollBy(0, 150);", button)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(str(calc(x)))
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option1 = browser.find_element(By.ID, "robotsRule")
    option1.click()

    button.click()
#   button = browser.find_element(By.CSS_SELECTOR, "button.btn")             # Отправляем заполненную форму
#   button.click()


#   input1 = browser.find_element(By.CSS_SELECTOR, "[type='text']")
#    input1.send_keys(y)
#    option1 = browser.find_element(By.ID, "robotCheckbox")
#    option1.click()
#    option1 = browser.find_element(By.ID, "robotsRule")
#    option1.click()








#    time.sleep(1)                            # Проверяем, что смогли зарегистрироваться # ждем загрузки страницы


finally:
    time.sleep(5)                           # ожидание чтобы визуально оценить результаты прохождения скрипта
    browser.quit()                           # закрываем браузер после всех манипуляций