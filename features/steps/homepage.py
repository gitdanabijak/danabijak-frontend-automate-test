from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

# Common Method

@given('open browser')
def open_browser(context):
    context.driver=webdriver.Chrome()

@when('open danabijak site')
def homepage_show_up(context):
    context.driver.get('https://danabijak.com')

@then('close browser')
def close_browser(context):
    context.driver.close()

# Others Implementation

@then('user can see tkb90 info')
def see_tkb_info(context):
    context.driver.find_element(By.XPATH, '//*[@id="nav-collapse"]/ul/li[4]/button/span[2]')

@then('user can click login button')
def click_login_button(context):
    context.driver.find_element(By.LINK_TEXT, "Masuk").click()

@then('user can click register button')
def click_register_button(context):
    context.driver.find_element(By.XPATH, '//*[@id="nav-collapse"]/ul/li[3]/button').click()