import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(19)

browser.get("http://suninjuly.github.io/explicit_wait2.html")
try:
    WebDriverWait(browser, 14).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    browser.find_element(By.ID,"book").click()
    numb = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc(numb))
    browser.find_element(By.ID, "solve").click()
    print("Success !!!")
    time.sleep(10)
    browser.quit()
    print("Closed")

except:
    print("Not found good enough price")
    browser.quit()


