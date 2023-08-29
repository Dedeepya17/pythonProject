
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://www.redbus.in/")
driver.implicitly_wait(20)
driver.find_element(By.XPATH,"//span[@class='name_rb_secondary_item']").click()
driver.find_element(By.ID,"//li[@id='user_sign_in_sign_up']").click()
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='modalIframe']"))
time.sleep(5)