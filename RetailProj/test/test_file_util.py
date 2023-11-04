from unittest import TestCase
from RetailProj.util import file_util
import os
class TestFileUtil(TestCase):
    def setUp(self) -> None:
        # to get current file's root path'
        self.project_root_path=os.path.dirname(os.getcwd())
    def test_get_dir_files_list(self):
        test_path=f"{self.project_root_path}/test/test_dir"
        result = file_util.get_dir_files_list(test_path,recursion=False)
        names=[]
        for i in result:
            names.append(os.path.basename(i))
        names.sort()
        self.assertEqual(['1','2'], names)

        result = file_util.get_dir_files_list(test_path, recursion=True)
        names = []
        for i in result:
            names.append(os.path.basename(i))
        names.sort()
        self.assertEqual( names,['1', '2','3','4','5'])

    def test_new_by_compare_lists(self):
        """测试new_by_compare_lists方法"""
        b_list = ['e:/a.txt', 'e:/b.txt']
        a_list = ['e:/a.txt', 'e:/b.txt', 'e:/c.txt', 'e:/d.txt']
        result = file_util.get_new_by_cmp_lists(a_list, b_list)

        self.assertEqual(['e:/c.txt', 'e:/d.txt'], result)


