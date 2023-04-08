import logging

from tests.user_auth_data import LOGIN, PASSWORD
from utils.log_exceptions import log_exceptions

logger = logging.getLogger(__name__)


@log_exceptions
def test_sidebar(login_page_fixture, start_page_fixture, main_page_fixture, caplog):
    logger.info(f"Starting test_sidebar with login: {LOGIN}, password: {PASSWORD}")
    start_page_fixture.click_login_button()
    login_page_fixture.enter_login(LOGIN)
    login_page_fixture.get_email_value()
    login_page_fixture.enter_password(PASSWORD)
    login_page_fixture.click_submit_button()

    assert main_page_fixture.is_hub_button_visible()
    main_page_fixture.click_element(main_page_fixture.MENU_LOCATOR)

    assert main_page_fixture.is_element_visible(main_page_fixture.MENU_LOCATOR)
    assert main_page_fixture.is_element_visible(main_page_fixture.SETTINGS_BUTTON_LOCATOR)
    assert main_page_fixture.is_element_visible(main_page_fixture.HELP_BUTTON_LOCATOR)
    assert main_page_fixture.is_element_visible(main_page_fixture.LOGS_BUTTON_LOCATOR)
    assert main_page_fixture.is_element_visible(main_page_fixture.TERMS_OF_SERVICE_BUTTON_LOCATOR)
    assert main_page_fixture.is_element_visible(main_page_fixture.BUILD_LOCATOR)

    logger.info("Test passed")
