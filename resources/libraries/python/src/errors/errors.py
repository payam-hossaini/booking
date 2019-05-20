from robot.api import logger
from robot.api.deco import keyword
from selenium_extensions.selenium_extensions import SeleniumExtensions


class Errors(SeleniumExtensions):
    """Library for errors and exceptions"""
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        super(Errors, self).__init__()

    @keyword
    def log_error(self):
        self._common_test_dump()
        try:
            self.sl.maximize_browser_window()
            self.sl.capture_page_screenshot()
            current_location = self.sl.get_location()
            logger.info('Current location:\n{}'.format(current_location))
            self.sl.log_source()
        except:
            msg = 'Unable to generate browser-related error information.'
            logger.trace(msg)
            raise

    def _common_test_dump(self):
        """
        function calls that are common to all "log_error" keyword
        """
        case_name = self.builtin.get_variable_value('${TEST NAME}')
        suite_documentation = self.builtin.get_variable_value(
            '${SUITE DOCUMENTATION}')
        tags = self.builtin.get_variable_value('@{TEST TAGS}', '@{EMPTY}')
        source = self.builtin.get_variable_value('${SUITE SOURCE}')
        logger.info('Test suite path:\n{}'.format(source))
        logger.info('Test suite documentation:\n{}'.format(suite_documentation))
        logger.info('Test case name:\n{}'.format(case_name))
        logger.info('Test case tags:\n{}'.format(tags))
