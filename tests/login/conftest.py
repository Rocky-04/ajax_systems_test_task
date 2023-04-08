import pytest

from framework.login_page import LoginPage
from framework.main_page import MainPage
from framework.start_page import StartPage


@pytest.fixture(scope='function')
def login_page_fixture(driver):
    yield LoginPage(driver)


@pytest.fixture(scope='function')
def main_page_fixture(driver):
    yield MainPage(driver)


@pytest.fixture(scope='function')
def start_page_fixture(driver):
    yield StartPage(driver)
