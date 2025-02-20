print("Start test********************************")
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.hao123.com")
sleep(1)
driver.quit()