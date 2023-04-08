import logging

import pytest

from tests.user_auth_data import LOGIN, PASSWORD
from utils.log_exceptions import log_exceptions

logger = logging.getLogger(__name__)


@log_exceptions
@pytest.mark.parametrize('login, password, expected_result', [
    (LOGIN, PASSWORD, True),
    ('wrong@gmail.com', 'wrong_password', False),
    (LOGIN, 'wrong_password', False),
    ('wrong@email.com', PASSWORD, False),
    ('', '', False),
    (LOGIN, '', False),
    ('', PASSWORD, False)
])
def test_authorization_with_valid_and_invalid_credentials(login, password, expected_result,
                                                          login_page_fixture, start_page_fixture,
                                                          main_page_fixture, caplog):
    logger.info((f"Starting test_authorization_with_valid_and_invalid_credentials with login: "
                 f"{login}, password: {password}, expected result: {expected_result}"))
    start_page_fixture.click_login_button()
    login_page_fixture.enter_login(login)
    login_page_fixture.get_email_value()
    if login:
        assert login_page_fixture.get_email_value() == login

    login_page_fixture.enter_password(password)
    if password:
        assert len(login_page_fixture.get_password_value()) == len(password)
    login_page_fixture.click_submit_button()

    if expected_result:
        assert main_page_fixture.is_hub_button_visible() == expected_result
        main_page_fixture.logout()
        logger.info("Authorization passed")
    else:
        if login and password:
            assert login_page_fixture.get_snackbar_value() in ('Wrong login or password',
                                                               'No Connection')
        else:
            assert login_page_fixture.get_snackbar_value() == 'Please fill all required fields.'
        logger.info(f"Authorization failed with login: {login}, password: {password}")
