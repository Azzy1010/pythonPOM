import os

import pytest
from pytest_html import extras
import datetime
from pathlib import Path

date = datetime.date.today()
f_date = date.strftime('%d-%m-%Y')


def ss(driver, value):
    global item,ss_directory
    item = value
    ss_directory = f"./Reports/{f_date}/SS"
    os.makedirs(ss_directory, exist_ok=True)
    driver.save_screenshot(f"{ss_directory}/{item}.png")
    return item,ss_directory


date = datetime.date.today()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report = f"./Reports/{f_date}/"
    os.makedirs(report, exist_ok=True)
    config.option.htmlpath = f'{report}' + 'Automation_reports ' + f_date + ".html"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport():
    outcome = yield
    report = outcome.get_result()
    main = str(Path.cwd())
    if report.when == "call" and report.failed:
        report.extra = [extras.image(f"{main}/Reports/{f_date}/SS/{item}.png", "Screenshot")]


def pytest_html_report_title(report):
    # change the title of the file
    report.title = f"Automation Report {date}"

# @pytest.hookimpl(hookwrapper=True)
