from base import Base, save_driver, run_on_failure
from html_components.wait_until import WaitUntil
from html_components.ajax import Ajax
from find_element import FindElement
from robot.api import logger
from robot.api.deco import keyword


class WebElement(Base):

    def __init__(self):
        super(WebElement, self).__init__()
        self.wait_until = WaitUntil()
        self.ajax = Ajax()
        self.find_element = FindElement()

    @keyword
    @save_driver
    @run_on_failure
    def click_element(self, locator):
        """clicks element based on the locator

        :param locator: element locator
        """
        logger.info('locating element with locator: {0}'.format(locator))
        self.ajax.wait_ajax_complete()
        self.wait_until_click_element_succeeds(locator)
        self.ajax.wait_ajax_complete()

    def wait_until_click_element_succeeds(self, locator):
        self.wait_until.no_exception(lambda: self._wait_and_click(locator))

    def _wait_and_click(self, locator):
        self.sl.wait_until_page_contains_element(locator)
        self.sl.click_element(locator)

    @keyword
    @save_driver
    @run_on_failure
    def get_element_css_value(self, locator, css_property):
        """Returns the CSS value of a element.

        Keyword arguments:
        ``locator`` -- element locator
        ``css_property`` -- desired CSS value
        """
        logger.info('locating element with locator: {0}'.format(locator))
        self.ajax.wait_ajax_complete()
        element = self.driver.find_element_by_xpath(locator)
        return element.value_of_css_property(css_property)
