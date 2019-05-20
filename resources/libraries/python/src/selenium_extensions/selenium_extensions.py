from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError


class SeleniumExtensions(object):
    """Selenium extensions library.

    SeleniumExtensions class extends Selenium Library
    keywords.
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self._builtin = None
        self._sl = None

    @property
    def builtin(self):
        """
        Robot Framework Builtin
        """
        if not self._builtin:
            try:
                self._builtin = BuiltIn()
            except RobotNotRunningError:
                self._builtin = None
        return self._builtin

    @property
    def sl(self):
        """
        Selenium library
        """
        if not self._sl:
            try:
                self._sl = self.builtin.get_library_instance('SeleniumLibrary')
            except RobotNotRunningError:
                self._sl = None
        return self._sl

    @keyword
    def open_browser(self, url):
        self.sl.open_browser(url, self.builtin.get_variable_value('${BROWSER_TYPE}'))
        self.sl.maximize_browser_window()
