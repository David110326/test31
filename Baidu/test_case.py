print("Start test********************************")
from selenium.webdriver.chrome import webdriver
from time import sleep
driver=webdriver.WebDriver()
driver.maximize_window()
driver.get("https://www.baidu.com")
print(driver.title)
sleep(2)
sleep(3)
driver.quit()
#add som
