import time
from base import Base
from robot.api import logger


class WaitUntil(Base):

    def __init__(self):
        super(WaitUntil, self).__init__()

    def no_exception(self, function):
        self.must_be_callable(function)
        got_exception = None
        end_time = time.time() + self.sl_timeout
        while time.time() < end_time:
            try:
                function()
            except Exception as e:
                logger.trace('For function() exception: {}'.format(e))
                got_exception = e
                time.sleep(1)
            else:
                return

        raise got_exception

    @staticmethod
    def must_be_callable(callable):
        if not hasattr(callable, '__call__'):
            raise TypeError('Is not callable:"{0}"'.format(callable))
