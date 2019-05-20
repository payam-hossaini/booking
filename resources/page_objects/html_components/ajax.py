from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from base import Base
from robot.api import logger


class Ajax(Base):

    def __init__(self):
        super(Ajax, self).__init__()

    def wait_ajax_complete(self):
        """waits until Ajax is complete

        Use this wait for web pages that use Ajax. The wait is suitable for
        actions that trigger angular once like: selections, buttons, tabs etc.
        """
        WebDriverWait(self.driver, self.short_timeout, 0.2).until(
            self._ajax_ready, 'Timeout waiting for Ajax to complete.')

    @staticmethod
    def _ajax_ready(driver):
        try:
            status = driver.execute_script("return angular.element(document).injector().get('$http').pendingRequests.length === 0")
        except WebDriverException:
            return True
        except:
            raise

        logger.info("jQuery still active: {0}".format(status))
        return 0 == status
