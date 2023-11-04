from unittest import TestCase
from RetailProj.util import logging_util
import logging
class TestLoggingUtil(TestCase):
    def setUp(self) -> None:
        pass
    def test_get_logger(self):
        logger=logging_util.init_logger()
        # way 1: to judge the return obj type is logging.RootLogger
        # self.assertIsInstance('s',str)
        self.assertIsInstance(logger,logging.RootLogger)
        # way 2 : to judge the return obj type is logging.RootLogger, isinstance return a bool
        result= isinstance(logger,logging.RootLogger)
        self.assertEqual(result,True)


