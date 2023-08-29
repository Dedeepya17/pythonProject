import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

use_step_matcher("re")
driver=webdriver.Chrome()



@given(":the user is on the login page")
def step_impl(context):
    print("browser name=" +driver.name)
    driver.maximize_window()


@when(":load the url")
def step_impl(context):
    driver.get("https://www.jotform.com/login/")
    print("title -" + driver.title)



@when(":enter (?P<Username>.+) and (?P<password>.+)")
def step_impl(context, Username, password):
    Username = driver.find_element(By.XPATH, "//input[@class='xcl-inp']").send_keys("Neelima ")
    password = driver.find_element(By.XPATH, "//input[@class='xcl-inp']").send_keys("1234567")
    time.sleep(6)


@when(":click on login button")
def step_impl(context):
    login = driver.find_element(By.ID, "signinButton")


@then(":login should be successful")
def step_impl(context):
    driver.close()