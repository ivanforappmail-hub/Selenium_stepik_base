from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # Считываем x
    x_element = browser.find_element(By.CSS_SELECTOR, ".nowrap#input_value")
    x = x_element.text
    y = calc(x)

    # Скроллим до кнопки + чуть ниже, чтобы футер не перекрывал
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, 150);", button)

    # Вводим ответ
    browser.find_element(By.ID, "answer").send_keys(y)

    # Отмечаем чекбокс и радиокнопку
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()

    # Отправляем
    button.click()

    # Считываем результат
    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()