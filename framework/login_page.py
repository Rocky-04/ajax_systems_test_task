from .page import Page


class LoginPage(Page):
    """Page object for the login page."""

    LOGIN_INPUT_LOCATOR = ('id', 'com.ajaxsystems:id/login')
    PASSWORD_INPUT_LOCATOR = ('id', 'com.ajaxsystems:id/password')
    SUBMIT_BUTTON_LOCATOR = ('id', 'com.ajaxsystems:id/next')
    SNACKBAR_LOCATOR = ('id', 'com.ajaxsystems:id/snackbar_text')

    def click_submit_button(self) -> None:
        """Clicks the submit button to log in."""

        self.click_element(self.SUBMIT_BUTTON_LOCATOR)

    def enter_login(self, login: str) -> None:
        """
        Enters the specified login into the login input field.

        :param login: The login to enter.
        """
        self.enter_text(self.LOGIN_INPUT_LOCATOR, login)

    def enter_password(self, password: str) -> None:
        """
        Enters the specified password into the password input field.

        :param password: The password to enter.
        """
        self.enter_text(self.PASSWORD_INPUT_LOCATOR, password)

    def get_email_value(self) -> str:
        """
        Returns the value of the email input field.
        """
        return self.get_element_attribute(self.LOGIN_INPUT_LOCATOR)

    def get_password_value(self) -> str:
        """
        Returns the value of the password input field.
        """
        return self.get_element_attribute(self.PASSWORD_INPUT_LOCATOR)

    def get_snackbar_value(self) -> str:
        """
        Returns the value of the password input field.
        """
        return self.get_element_attribute(self.SNACKBAR_LOCATOR)
