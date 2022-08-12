from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Common Method

@given('open browser')
def open_browser(context):
    options = Options()
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    context.driver=webdriver.Chrome(chrome_options=options)

@when('open danabijak site')
def homepage_show_up(context):
    context.driver.get('https://sandbox.danabijak.com')

@then('close browser')
def close_browser(context):
    context.driver.close()

# Others Implementation

@then('user can see tkb90 info')
def see_tkb_info(context):
    context.driver.find_element(By.XPATH, '//*[@id="nav-collapse"]/ul/li[4]/button/span[2]')

@then('user can click login button')
def click_login_button(context):
    context.driver.find_element(By.XPATH, '//*[@id="main-calculator"]/div[1]/div/p[2]/a/u').click()

@then('user can click register button')
def click_register_button(context):
    context.driver.find_element(By.XPATH, '//*[@id="nav-collapse"]/ul/li[3]/button').click()

@then('user can click tentangkami page')
def click_tentangkami_button(context):
    context.driver.execute_script("window.scrollTo(0, 3000)")
    time.sleep(3)
    tk = context.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[4]/div/footer/div/div[1]/div[2]/h5/a')
    at = ActionChains(context.driver)
    at.click(on_element=tk).perform();
    time.sleep(10)

@then('user can click agendakegiatan page')
def click_tentangkami_button(context):
    context.driver.execute_script("window.scrollTo(0, 3000)")
    time.sleep(3)
    tk = context.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[4]/div/footer/div/div[1]/div[2]/ul/li[1]/a')
    at = ActionChains(context.driver)
    at.click(on_element=tk).perform();
    time.sleep(10)    