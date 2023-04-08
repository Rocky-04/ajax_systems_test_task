from .page import Page


class StartPage(Page):
    """Page object for the start page."""

    LOGIN_BUTTON_LOCATOR = ('id', 'com.ajaxsystems:id/login')
    SIGNUP_BUTTON_LOCATOR = ('id', 'com.ajaxsystems:/')

    def click_login_button(self) -> None:
        """Clicks on the 'Login' button on the welcome page."""

        self.click_element(self.LOGIN_BUTTON_LOCATOR)

