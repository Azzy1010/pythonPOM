import os

import pytest
from pytest_html import extras
import datetime

date = datetime.date.today()
f_date = date.strftime('%d-%m-%Y')


def ss(driver, value):
    global item
    item = value
    SS_directory = f"./Reports/{f_date}/SS"
    os.makedirs(SS_directory, exist_ok=True)
    driver.save_screenshot(f"{SS_directory}/{item}.png")
    return item


date = datetime.date.today()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # check if the the folder to save reports is present or not, if not then it will create the folder
    # if not os.path.exists(f'C:\D--/Reports/{f_date}/SS'):
    #     os.makedirs(f'C:\D--/Reports/{f_date}/SS')
    # Change the name of the HTML report
    report = f"./Reports/{f_date}/"
    os.makedirs(report, exist_ok=True)
    config.option.htmlpath = f'{report}' + 'Automation_reports ' + f_date + ".html"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport():
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        report.extra = [extras.image(f"C:\D--/Reports/{f_date}/SS/{item}.png", "Screenshot")]


def pytest_html_report_title(report):
    # change the title of the file
    report.title = f"Automation Report {date}"

# @pytest.hookimpl(hookwrapper=True)
