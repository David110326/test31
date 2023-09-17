print("Start test********************************")
from selenium.webdriver.chrome import webdriver
from time import sleep
driver=webdriver.WebDriver()
driver.maximize_window()
driver.get("https://www.baidu.com")
print(driver.title)
sleep(3)
sleep(4)
driver.quit()
#add som
#ffsfsfs
