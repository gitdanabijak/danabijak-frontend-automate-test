from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@when('open danabijak login site')
def homepage_show_up(context):
    context.driver.get('https://sandbox.danabijak.com/login')

@then('user input email')
def user_input_email(context):
    element = context.driver.find_element(By.NAME, 'login')
    element.send_keys("ibnutest30@danabijak.com")

@then('user input password')
def user_input_password(context):
    element = context.driver.find_element(By.NAME, 'password') 
    element.send_keys("123123")
    
@then('user click login') 
def user_click_login(context):
    context.driver.find_element(By.XPATH, "//button[@type='commit']").click()
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Selamat datang, ibnu test tiga puluh!']")))
    

