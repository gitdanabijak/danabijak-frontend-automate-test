from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@when('open danabijak login site')
def homepage_show_up(context):
    context.driver.get('https://danabijak.com/login')

@then('user input email')
def user_input_email(context):
    element = context.driver.find_element(By.NAME, 'login')
    element.send_keys("ibnutest3@danabijak.com")

@then('user input password')
def user_input_password(context):
    element = context.driver.find_element(By.NAME, 'password')
    element.send_keys("230998")
    
@then('user click login')
def user_click_login(context):
    context.driver.find_element(By.XPATH, "//button[@type='commit']").click()
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Selamat datang, Ibnu Testing!']")))
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@name='loan_purpose']")))
    context.driver.find_element(By.XPATH, "//select[@name='loan_purpose']/option[10]").click()
    time.sleep(5)
    context.driver.find_element(By.LINK_TEXT, "Mohon Maaf").click()
    time.sleep(3)
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h3[@class='fm-form-subheading']")))
    

