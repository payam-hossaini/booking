
import copy
from decorator import decorate
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError
from robot.utils import timestr_to_secs
try:
    from SeleniumLibrary.errors import SeleniumLibraryException
except ImportError:
    class SeleniumLibraryException(Exception):
        ROBOT_SUPPRESS_NAME = True


def save_driver(func):
    """decorator for keywords that use browser."""
    def inner(func, self, *args, **kwargs):
        self._set_driver()
        return func(self, *args, **kwargs)
    return decorate(func, inner)


def run_on_failure(func):
    """
    Decorator for keywords that need SeleniumLibrary run_on_failure.

    Screenshot of browser is captured when function raises exception
    """
    def inner(func, self, *args, **kwargs):
        self.suppress_run_on_failure()
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            if not (hasattr(e, '_deco_has_run_on_failure')):
                self.return_run_failure_keyword()
                BuiltIn().get_library_instance('SeleniumLibrary').failure_occurred()
                setattr(e, '_deco_has_run_on_failure', True)
            raise
        finally:
            self.return_run_failure_keyword()
    return decorate(func, inner)


class Base(object):
    """Base class for all page objects and navigation classes"""
    sl = None
    driver = None
    old_run_on_failure_kw = None
    builtin = None

    def __init__(self):
        super(Base, self).__init__()

    @staticmethod
    def join_arguments_into_dictionary(args, **kwargs):
        """Joins arguments into a dictionary and returns it

        :param args: when dictionary then update it with kwargs
        :param kwargs: dictionary: firstname=James   title=Mr
        :return: dictionary
        """
        if isinstance(args, dict):
            args.update(kwargs)
        else:
            args = kwargs
        return copy.deepcopy(args)

    @staticmethod
    def poll_keyword(tryout=5, each_wait=1, func=None, *args):
        """ Uses RF wait_until_keyword_succeeds to poll keyword

        for more info check the wait_until_keyword_succeeds docs

        :param tryout: number of tryouts
        :param each_wait: time for waiting between tries
        :param func: keyword name
        :param args: keyword arguments
        """
        BuiltIn().wait_until_keyword_succeeds(tryout, each_wait, func, *args)

    def _set_driver(self):
        """Saves the latest state of current browser.

        Use @save_driver decorator instead of using this keyword directly
        """
        try:
            Base.sl = BuiltIn().get_library_instance('SeleniumLibrary')
        except RobotNotRunningError:
            Base.sl = None
        try:
            Base.driver = self.sl.driver
        except RuntimeError:
            Base.driver = None
        except SeleniumLibraryException:
            Base.driver = None

    @save_driver
    def suppress_run_on_failure(self):
        """Disables SeleniumLibrary run on failure functionality"""
        old_kw = self.sl.register_keyword_to_run_on_failure('Nothing')
        is_none = old_kw is None or 'No keyword' == old_kw
        if not is_none:
            Base.old_run_on_failure_kw = old_kw

    @save_driver
    def return_run_failure_keyword(self):
        """Restores the previous run on failure keyword to Selenium2Library."""
        self.sl.register_keyword_to_run_on_failure(
            Base.old_run_on_failure_kw)

    @property
    def browser_type(self):
        try:
            return BuiltIn().get_variable_value('${BROWSER_TYPE}')
        except RobotNotRunningError:
            return 'Chrome'

    @property
    def sl_timeout(self):
        if self.sl:
            timeout = self.sl.get_selenium_timeout()
        else:
            timeout = BuiltIn().get_variable_value('${SYS_VAR_PAGE_TIMEOUT}')
        return timestr_to_secs(timeout)
