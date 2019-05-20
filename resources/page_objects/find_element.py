
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from robot.api import logger
from html_components.ajax import Ajax


class FindElement(object):
    strategies = {'id': By.ID,
                  'name': By.NAME,
                  'xpath': By.XPATH,
                  'css': By.CSS_SELECTOR}

    def __init__(self):
        self.ajax = Ajax()

    def find_element(self, driver, locator, timeout=5):
        """Looks up elements from DOM tree using implicit wait.

        The keyword returns a list of web elements or fails when element with
        the locator is not found.

        Supported strategies are:id, name, xpath, and css

        The keyword uses implicit wait for locating elements. Implicit wait
        is needed when a page uses AJAX (java script) to update it's content
        (DOM).

        :param driver: driver
        :param locator: locator of element
        :param timeout: timeout
        :return: element

        Locator example:
        xpath | //a or xpath=//a
        id    | id=element_id
        name  | name=element_name
        css   | css=.myCSS
        """
        prefix, criteria = self._parse_locator(locator)
        strategy = "xpath" if prefix is None else prefix
        if strategy not in self.strategies.values():
            logger.error('no element lookup strategy found for prefix{0}!\nSupported strategies:{1}'
                         .format(prefix, self.strategies.keys()))
            raise KeyError
        logger.info('waiting Ajax to resolve....')
        self.ajax.wait_ajax_complete()
        logger.info('finding elements with locator:{0}'.format(locator))
        elements = WebDriverWait(driver, timeout).until(
            ec.presence_of_all_elements_located(
                (strategy, criteria)
            ),
            message='Element not found with locator:{0}'.format(locator)
        )
        return elements

    @staticmethod
    def _parse_locator(locator):
        prefix = None
        criteria = locator
        if not locator.startswith('//'):
            locator_parts = locator.partition('=')
            if len(locator_parts[1]) > 0:
                prefix = locator_parts[0]
                criteria = locator_parts[2].strip()
        return prefix, criteria
