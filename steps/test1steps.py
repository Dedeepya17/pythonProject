import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

use_step_matcher("re")
driver =webdriver.Chrome()


@step(":open the browser")
def step_impl(context):
    print("browser name=" +driver.name)
    driver.maximize_window()



@when(":load url")
def step_impl(context):
   driver.get("https://www.google.com/")
   print("title -"+driver.title)


@then(":verify textbox is present")
def step_impl(context):
    textbox =driver.find_element(By.ID,"APjFqb")
    assert textbox.is_displayed()


@then(":close the browser")
def step_impl(context):
   driver.close()


@then(":search for (?P<item>.+)")
def step_impl(context, item):
    driver.find_element(By.ID,"APjFqb").send_keys(item)
    time.sleep(5)