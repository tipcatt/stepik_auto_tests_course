import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
)

bookButton = browser.find_element(By.ID, "book")
bookButton.click()

browser.execute_script("window.scrollBy(0, 150);")

value = browser.find_element(By.ID, "input_value")
x = value.text
y = calc(x)

answerField = browser.find_element(By.ID, "answer")
answerField.send_keys(y)

submitButton = browser.find_element(By.ID, "solve")
submitButton.click()

time.sleep(5)
browser.quit()