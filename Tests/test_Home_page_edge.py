import pytest
from selenium import webdriver
from Tests.conftest import ss
global driver
import datetime

@pytest.fixture
def setup():
    global driver
    driver = webdriver.Edge()
    driver.maximize_window()
    yield
    driver.quit()


def test_website_title_edge(setup):
    date = datetime.date.today()
    driver.get('https://www.google.com')
    title = driver.title
    item = f'{test_website_title_edge.__name__}_{date.strftime(" %d-%m-%Y")}'
    if title == 'Facebook':
        assert True
    else:
        ss(driver, item)
        assert False, 'Title Mismatch'
