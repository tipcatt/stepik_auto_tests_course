from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    enterFname = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    enterFname.send_keys("Kot")
    enterLname = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    enterLname.send_keys("Kotosey")
    enterEmail = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    enterEmail.send_keys("koto@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'myFile.txt')

    uploadButton = browser.find_element(By.CSS_SELECTOR, "#file")
    uploadButton.send_keys(file_path)

    time.sleep(0.5)
    submitButton = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submitButton.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    print("Good job")

    # закрываем браузер после всех манипуляций
    browser.quit()
