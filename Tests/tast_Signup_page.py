import pytest
from selenium import webdriver
import time
import random
from Pages.signup_page import sign_up_login
from Pages.config import screen_size
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# -----------------Generators-----------------
name = random.choice(['cbiyqbc', 'cuvcyquc', 'veqvewqf', 'ewfvwefw', 'wfwef3'])
email = f'{name}@{random.randint(0, 1000)}.com'
password = random.choice(['cbiyqbc12', 'cuvcyquc12', 'veqvewqf12', 'ewfvwefw12', 'wfwef323'])


class credentials_for_login():
    email_login = email
    password_login = password


@pytest.fixture
def setup():
    global driver, name, email, password
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield
    driver.quit()


def test_sign_page_check(setup):
    driver.get('https://soluber.com/register')
    size = screen_size
    driver.execute_script(size.size)
    assert driver.find_element(By.XPATH,
                               '//*[@id="login-background"]/div/div[3]/div/h2').text == 'Sign Up To Soluber', 'Signup assert error'


def test_username_password(setup):
    driver.get('https://soluber.com/register')
    size = screen_size
    driver.execute_script(size.size)
    locators = sign_up_login
    name = random.choice(['cbiyqbc', 'cuvcyquc', 'veqvewqf', 'ewfvwefw', 'wfwef3'])
    driver.find_element(By.ID, locators.User_name).send_keys(name)
    driver.find_element(By.ID, locators.user_email).send_keys('121@12.com')
    driver.find_element(By.ID, locators.password).send_keys('1231')
    driver.find_element(By.ID, locators.confirm_password).send_keys('1231' + Keys.ENTER)
    # time.sleep(2)
    assert driver.find_element(By.XPATH,
                               '//span[@class="invalid-feedback d-block"]').text == 'The password must be at least 8 characters.', 'Password validation failed'


def test_Existing_email_validation(setup):
    driver.get('https://soluber.com/register')
    size = screen_size
    driver.execute_script(size.size)
    locators = sign_up_login
    name = random.choice(['cbiyqbc', 'cuvcyquc', 'veqvewqf', 'ewfvwefw', 'wfwef3'])
    password = random.choice(['cbiyqbc', 'cuvcyquc', 'veqvewqf', 'ewfvwefw', 'wfwef3'])
    driver.find_element(By.ID, locators.User_name).send_keys(name)
    driver.find_element(By.ID, 'email').send_keys('padawi3282@soremap.com')
    driver.find_element(By.ID, 'password-input').send_keys(password)
    driver.find_element(By.ID, 'password-confirm').send_keys(password + Keys.ENTER)
    assert driver.find_element(By.XPATH,
                               "//span[@role='alert']").text == 'The email has already been taken.', 'Email Validation Error'


def test_New_signup(setup):
    driver.get('https://soluber.com/register')
    size = screen_size
    driver.execute_script(size.size)
    driver.find_element(By.ID, 'name').send_keys(name)
    driver.find_element(By.ID, 'email').send_keys(email)
    driver.find_element(By.ID, 'password-input').send_keys(password)
    driver.find_element(By.ID, 'password-confirm').send_keys(password + Keys.ENTER)
    time.sleep(2)
    assert driver.find_element(By.XPATH,
                               "//div[@class='toast-message']").text == ('''Congratulation! You can now proceed to
                                                                        login with your email'), 'Unable to sign-in''')
