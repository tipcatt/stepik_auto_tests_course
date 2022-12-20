from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    journeyButton = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    journeyButton.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    value = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = value.text
    y = calc(x)

    answerField = browser.find_element(By.CSS_SELECTOR, "#answer")
    answerField.send_keys(y)

    submitButton = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submitButton.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    print(browser.switch_to.alert.text)

    # закрываем браузер после всех манипуляций
    browser.quit()
