from selenium import webdriver
import time

from selenium.webdriver.common.by import By

link = 'https://rozetka.com.ua'
browser = webdriver.Edge()
browser.get(link)

search_string = browser.find_element(By.XPATH, "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/div/form/div/div/input")
search_string.send_keys("Ноутбук")
button = browser.find_element(By.XPATH, "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/div/form/div/div/input \n")
time.sleep(15)