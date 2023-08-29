#window_handles
#switch_to.window

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID,"openwindow")
win = driver.window_handles
driver.switch_to.window(win[1])
time.sleep(2)
address = driver.find_element(By.XPATH,"//img[contains(@src,'images')]//following-sibling::span").text
print(address)