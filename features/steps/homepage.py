from behave import *
from selenium import webdriver

@given('we have behave installed')
def step_impl(context):
    context.driver=webdriver.Chrome()

@when('we implement a test')
def step_impl(context):
    context.driver.get('https://danabijak.com')

@then('behave will test it for us!')
def step_impl(context):
    context.driver.close()