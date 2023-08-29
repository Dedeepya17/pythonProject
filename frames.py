#switch_to.frame()
#switch_to.default_content()
from selenium import webdriver
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.switch_to.frame("courses-iframe")
txt = driver.find_element(By.XPATH,"span[contains(@,'fa-envelope')]/parent::li").text
print(txt)
driver.switch_to.default_content()
txt1 = driver.find_element(By.ID,"mousehover").text
print(txt1)


