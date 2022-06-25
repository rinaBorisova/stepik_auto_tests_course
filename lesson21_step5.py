from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    #Вычислить X
    x_element = browser.find_element(By.CSS_SELECTOR, "label .nowrap:nth-child(2)")
    x = x_element.text
    y = calc(x)

    # Ввести значение
    past = browser.find_element(By.ID, "answer")
    past.send_keys(y)

    # Выбрать чекбокс я робот
    option = browser.find_element(By.ID, "robotCheckbox")
    option.click()

    # Выбрать радиобаттон с роботами
    option1 = browser.find_element(By.ID, "robotsRule")
    option1.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
