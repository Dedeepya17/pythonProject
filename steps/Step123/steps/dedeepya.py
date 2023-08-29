import time

from behave import *
from selenium import webdriver
use_step_matcher("re")
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
@given("The user is on the registration page")
def step_impl(context):
    driver.get('https://www.codebrainer.com/user/register')


@when('They enter  "(.+)" and  "(?P<email>.+)"')
def step_impl(context, arg0, email):

        First_name = driver.find_element(By.NAME, "firstName").send_keys('Dedeepya')
        email = driver.find_element(By.NAME, "email").send_keys('chdedeepya17@gmail.com')



@when('enter "(.+)"')
def step_impl(context, arg0):
    Last_Name = driver.find_element(By.NAME, "lastName").send_keys('Chilla')


@step('Set the password to "(?P<password>.+)"')
def step_impl(context, password):
    password = driver.find_element(By.NAME, "password").send_keys('1234567')

@step('Confirm the password "(?P<confirmpwd>.+)"')
def step_impl(context, confirmpwd):
    Confirm_password = driver.find_element(By.NAME, "confirmPassword").send_keys('1234567')


@step('Click the "checkbox1","checkbox2"')
def step_impl(context):
    checkbox1 = driver.find_element(By.XPATH, "//input[@id='chkTerms']")
    checkbox1.click()
    assert checkbox1.is_displayed()
    checkbox2 = driver.find_element(By.XPATH, "//input[@id='chkOffersNews']")
    checkbox2.click()
    assert checkbox2.is_displayed()


@then("click the register button")
def step_impl(context):
    registration=driver.find_element(By.XPATH,"//button[@class='btn btn-block']")
    registration.click()
    time.sleep(5)

@then("registration succefull,close the browser")
def step_impl(context):
    driver.close()


'''import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

use_step_matcher("re")
driver =webdriver.Chrome()


@given(":The user is on the registration page")
def step_impl(context):
    driver.get("https://www.codebrainer.com/user/register")
    #driver.maximize_window()

@when(':They enter  "(.+)" and  "(?P<email>.+)"')
def step_impl(context, arg0, email):
    First_name= driver.find_element(By.NAME,"firstName").send_keys("chilla")
    email=driver.find_element(By.NAME,"email").send_keys("chilla.dedee@gmail.com")

@when(': enter "(.+)"')
def step_impl(context, arg0):
    Last_Name=driver.find_element(By.NAME,"lastName").send_keys("Dedee")


@when(':Set the password to "(?P<password>.+)"')
def step_impl(context, password):
    password=driver.find_element(By.NAME,"password").send_keys("1234567")


@step(':Confirm the password "(?P<confirmpwd>.+)"')
def step_impl(context, confirmpwd):
    Confirm_password = driver.find_element(By.NAME, "confirmPassword").send_keys("1234567")


@when(':Click the "checkbox1","checkbox2"')
def step_impl(context):
    checkbox1=driver.find_element(By.XPATH,"//input[@id='chkTerms']")
    checkbox1.click()
    assert checkbox1.is_selected()
    checkbox2=driver.find_element(By.XPATH,"//input[@id='chkOffersNews']")
    checkbox2.click()
    assert checkbox2.is_selected()
    time.sleep(5)

@then(":The registration should be successful")
def step_impl(context):
    registration=driver.find_element(By.XPATH,"//button[@class='btn btn-block']")
    registration.click()
    driver.close()



'''


