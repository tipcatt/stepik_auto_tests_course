from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    enterName = browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/form[1]/div[1]/div[1]/input[1]")
    enterName.send_keys("Monya")
    enterName = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    enterName.send_keys("Aydisha")
    enterName = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
    enterName.send_keys("ma@gov.com")
    

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    
    if welcome_text == "Congratulations! You have successfully registered!":
        print("it's match")
    else:
        print("wrong text")
    # закрываем браузер после всех манипуляций
    browser.quit()
