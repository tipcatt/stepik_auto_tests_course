from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # применяем рассчеты
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    enterAnswer = browser.find_element(By.CSS_SELECTOR, "#answer")
    enterAnswer.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox[type='checkbox']")
    checkbox.click()

    radioButton = browser.find_element(By.CSS_SELECTOR, "label[for ='robotsRule']")
    radioButton.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)

    print("Good job")

    # закрываем браузер после всех манипуляций
    browser.quit()
