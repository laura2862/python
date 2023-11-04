from unittest import TestCase
from RetailProj.util import str_util
class TestStrUtil(TestCase):
    def setUp(self) -> None:
        pass
    def test_str_util(self):
        s='NONE'
        result= str_util.check_null(s)
        self.assertEqual(True,result)
        s = 'NULL'
        result = str_util.check_null(s)
        self.assertEqual(True, result)
        s = 'UNDEFINED'
        result = str_util.check_null(s)
        self.assertEqual(True, result)
        s = ' '
        result = str_util.check_null(s)
        self.assertEqual(True, result)
        s = 'hello'
        result = str_util.check_null(s)
        self.assertEqual(False, result)
    def test_check_str_null_and_transfer_to_sql_null(self):
        str='null'
        result=str_util.check_str_null_and_transfer_to_sql_null(str)
        self.assertEqual('Null',result)

        str='none'
        result=str_util.check_str_null_and_transfer_to_sql_null(str)
        self.assertEqual('Null',result)
        str = ' '
        result = str_util.check_str_null_and_transfer_to_sql_null(str)
        self.assertEqual('Null', result)
        str = 'undefined'
        result = str_util.check_str_null_and_transfer_to_sql_null(str)
        self.assertEqual('Null', result)
        str = 'laura'
        result = str_util.check_str_null_and_transfer_to_sql_null(str)
        self.assertEqual("'laura'" ,result)


