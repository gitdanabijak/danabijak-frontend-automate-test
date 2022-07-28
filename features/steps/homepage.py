from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Common

@given('open browser')
def open_browser(context):
    context.driver=webdriver.Chrome()

@when('open danabijak site')
def homepage_show_up(context):
    context.driver.get('https://danabijak.com')

@then('close browser')
def close_browser(context):
    context.driver.close()

# Others

@then('user can see tkb90 info')
def see_tkb_info(context):
    context.driver.find_element(By.XPATH, '//*[@id="nav-collapse"]/ul/li[4]/button/span[2]')

@then('user can click login button')
def click_login_button(context):
    element = context.driver.find_element(By.LINK_TEXT, "Masuk")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    context.driver.find_element(By.LINK_TEXT, "Masuk").click()

@then('user can click register button')
def click_register_button(context):
    element = context.driver.find_element(By.XPATH, '//*[@id="nav-collapse"]/ul/li[3]/button')
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    context.driver.find_element(By.XPATH, '//*[@id="nav-collapse"]/ul/li[3]/button').click()