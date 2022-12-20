from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def func(x, y):
    return str(int(x) + int(y))

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_value = (browser.find_element(By.CSS_SELECTOR, "#num1")).text
    second_value = (browser.find_element(By.CSS_SELECTOR, "#num2")).text
    sum = func(first_value, second_value)

    print('ok 1')
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum)
    print('ok 2')
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()
    print('ok 3')
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)

    print("Good job")

    # закрываем браузер после всех манипуляций
    browser.quit()
