from selenium import webdriver
driver = webdriver.chrome(executable_path=""C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe"")
driver.chrome()

driver.get("https://whc.unesco.org/en/list/252/")
print(driver.current_url)
driver.close()


