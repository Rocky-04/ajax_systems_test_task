from appium.webdriver import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        """
        Constructs a new Page object.

        :param driver: The WebDriver instance.
        """
        self.driver = driver

    def find_element(self, locator: tuple) -> WebElement:
        """
        Finds an element by the specified locator.

        :param locator: The locator should be a tuple containing the search method and value
                        (e.g. ('id', 'com.ajaxsystems:id/login')).
        """
        return self.driver.find_element(*locator)

    def click_element(self, locator: tuple) -> None:
        """
        Waits for an element to be visible and clicks on it.

        :param locator: The locator should be a tuple containing the search method and value
                        (e.g. ('id', 'com.ajaxsystems:id/login')).
        """
        element = self.wait_for_visibility(locator)
        element.click()

    def enter_text(self, locator: tuple, text: str) -> None:
        """
        Enters text into an input field by the specified locator.

        :param locator: The locator should be a tuple containing the search method and value
                        (e.g. ('id', 'com.ajaxsystems:id/login')).
        :param text: The text to enter into the input field.
        """
        element = self.wait_for_visibility(locator)
        element.send_keys(text)

    def wait_for_visibility(self, locator: tuple, timeout: int = 10) -> WebElement:
        """
         Waits for an element to be visible by the specified locator.

        :param locator: The locator should be a tuple containing the search method and value
                        (e.g. ('id', 'com.ajaxsystems:id/login')).
        :param timeout: The maximum time in seconds to wait for the element to be visible
                        (default is 10 seconds).
        """
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def get_element_attribute(self, locator: tuple) -> str:
        """
        Returns the value of the specified attribute for the element found by the specified locator.

        :param locator: The locator should be a tuple containing the search method and value
                        (e.g. ('id', 'com.ajaxsystems:id/login')).
        """
        element = self.wait_for_visibility(locator)
        return element.text

    def is_element_visible(self, locator: tuple) -> bool:
        """
        Returns whether an element is visible by the specified locator.

        :param locator: The locator should be a tuple containing the search method and value
                        (e.g. ('id', 'com.ajaxsystems:id/login')).
        """
        element = self.wait_for_visibility(locator)
        return element.is_displayed()
