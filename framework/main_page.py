from .page import Page


class MainPage(Page):
    """Page object for the main page."""

    MENU_LOCATOR = ('id', 'com.ajaxsystems:id/menuDrawer')
    ADD_HUB_BUTTON_LOCATOR = ('id', 'com.ajaxsystems:id/hubAdd')
    SETTINGS_BUTTON_LOCATOR = ('id', 'com.ajaxsystems:id/settings')
    HELP_BUTTON_LOCATOR = ('id', 'com.ajaxsystems:id/help')
    LOGOUT_BUTTON_LOCATOR = ('id', 'com.ajaxsystems:id/accountInfoLogoutNavigate')
    LOGS_BUTTON_LOCATOR = ('id', 'com.ajaxsystems:id/logs')
    TERMS_OF_SERVICE_BUTTON_LOCATOR = ('id', 'com.ajaxsystems:id/documentation_text')
    BUILD_LOCATOR = ('id', 'com.ajaxsystems:id/build')

    def logout(self) -> None:
        """Logs out of the app."""

        if self.is_element_visible(self.ADD_HUB_BUTTON_LOCATOR):
            self.click_element(self.MENU_LOCATOR)
            self.click_element(self.SETTINGS_BUTTON_LOCATOR)
            self.click_element(self.LOGOUT_BUTTON_LOCATOR)

    def is_hub_button_visible(self):
        """Returns whether a hub_button is visible by the specified locator."""

        return self.is_element_visible(self.ADD_HUB_BUTTON_LOCATOR)
