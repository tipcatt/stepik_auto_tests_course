from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    redirectButton = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    redirectButton.click()
    print('ok 1')
    confirm = browser.switch_to.alert
    confirm.accept()
    print('ok 2')
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)
    print('ok 3')
    time.sleep(1)
    value = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = value.text
    y = calc(x)
    print('ok 4')
    answerField = browser.find_element(By.CSS_SELECTOR, "#answer")
    answerField.send_keys(y)
    print('ok 5')
    submitButton = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submitButton.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    print(browser.switch_to.alert.text)

    # закрываем браузер после всех манипуляций
    browser.quit()
