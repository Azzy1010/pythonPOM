import pytest
from selenium import webdriver
from selenium.webdriver import Keys

from Pages.config import screen_size
from Pages.Login_page import Login
from selenium.webdriver.common.by import By
from Tests.tast_Signup_page import credentials_for_login
from Tests.conftest import val
import Pages.config

import time
import random


@pytest.fixture()
def setup():
    global driver, name, email, password

    driver = webdriver.Chrome()
    driver.maximize_window()
    yield
    driver.quit()


def ss(item):
    driver.save_screenshot(f"/Volumes/D_Drive/SS_reports/{item}.png")


# def test_login_open(setup):
#     driver.get('https://soluber.com/login')
#     size = screen_size
#     driver.execute_script(size.size)

def test_New_log_in(setup):
    # login_locators = login
    # credentials_from_signup = credentials_for_login
    driver.get('https://soluber.com/login')
    # # size = screen_size
    # # driver.execute_script(size.size)
    # driver.find_element(By.ID, login_locators.login_user_name).send_keys(credentials_from_signup.email_login)
    # driver.find_element(By.ID, login_locators.login_password).send_keys(credentials_from_signup.password_login + Keys.ENTER)
    # time.sleep(3)
    if driver.title == 'hi':
        assert True
    else:
        item = 'bol'
        ss(item)
        val(item)
        assert False
