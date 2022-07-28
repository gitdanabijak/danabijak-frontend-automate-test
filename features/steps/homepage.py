from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('user open danabijak site')
def open_browser(context):
    context.driver=webdriver.Chrome()

@when('homepage presence')
def homepage_show_up(context):
    context.driver.get('https://danabijak.com')

@then('user can see tkb90 info')
def see_tkb_info(context):
    context.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/nav/div/div[2]/div/ul/li[4]/button/span[2]")
    context.driver.close()