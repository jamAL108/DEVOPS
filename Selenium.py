import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import *

driver=webdriver.Chrome()

driver.maximize_window()
driver.get(url="https://www.google.com")
driver.find_element(By.NAME, "q").send_keys("bing")
driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
driver.find_element(By.PARTIAL_LINK_TEXT,"Microsoft Bing").click()
time.sleep(5)
print("Program finished")
time.sleep(100)
driver.close()

