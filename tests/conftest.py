import subprocess
from datetime import datetime

import pytest
from appium import webdriver

from utils.android_utils import android_get_desired_capabilities


@pytest.fixture(scope='session')
def run_appium_server():
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )


@pytest.fixture(scope='session')
def driver(run_appium_server):
    driver = webdriver.Remote('http://localhost:4723/wd/hub', android_get_desired_capabilities())
    yield driver
    driver.quit()


def pytest_configure(config):
    """ Create a log file if log_file is not mentioned in *.ini file"""
    if not config.option.log_file:
        timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d_%H-%M-%S')
        config.option.log_file = 'logs/' + timestamp + '.log'
