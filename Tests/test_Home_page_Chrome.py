import pytest
from selenium import webdriver
from Tests.conftest import ss
import datetime
import pyautogui
global driver


@pytest.fixture
def setup():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield
    driver.quit()


def test_website_title_chrome(setup):
    date = datetime.date.today()
    driver.get('https://www.facebook.com')
    title = driver.title
    item = f'{test_website_title_chrome.__name__}_{date.strftime(" %d-%m-%Y")}'
    # pyautogui.alert(text = f'{item}')
    if title == 'Facebook':
        assert True
    else:
        ss(driver, item)
        assert False, 'Title Mismatch'
