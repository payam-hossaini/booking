from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError
from base import Base, run_on_failure, save_driver
from selenium_extensions.selenium_extensions import SeleniumExtensions


class SignIn(Base):
    """Login library
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        super(SignIn, self).__init__()
        self.sl_extensions = SeleniumExtensions()
        self.builtin = BuiltIn()

    @keyword
    @save_driver
    @run_on_failure
    def sign_in_to_booking(self, username, password):
        """Signs in to user account page

        :param username: username
        :param password: password

        Example:
        | Sign In To Booking | user@abc.com | pass123 |
        """
        self.sl_extensions.open_browser(self.sign_in_url)
        sign_in_xpath = '(//div[@class="sign_in_wrapper"])[last()]'
        self.sl.wait_until_page_contains_element(sign_in_xpath)
        self.sl.click_element(sign_in_xpath)
        self.sl.wait_until_page_contains_element('id:username')
        self.sl.input_text('id:username', username)
        self.sl.click_button('//button[@type="submit"]')
        self.sl.wait_until_page_contains_element('id:password')
        self.sl.input_text('id:password', password)
        self.sl.click_button('//button[@type="submit"]')
        self.sl.wait_until_page_contains_element('id:cross-product-bar')

    @property
    def sign_in_url(self):
        try:
            return self.builtin.get_variable_value('${HOST}')
        except RobotNotRunningError:
            return 'variable not found!'
