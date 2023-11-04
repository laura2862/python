from unittest import TestCase
from RetailProj.util.time_util import ts10_to_date_str,ts13_to_date_str
class TestTimeUtil(TestCase):
    def setUp(self) -> None:
        pass
    def tset_ts10_to_date_str(self):
        test_ts=1692457344
        result= ts10_to_date_str(test_ts)
        print(result)
        self.assertEqual('2023-08-19 23:02:24',result)
    def tset_ts13_to_date_str(self):
        test_ts=1692457344123
        result= ts10_to_date_str(test_ts)
        print(result)
        self.assertEqual('2023-08-19 23:02:24',result)

