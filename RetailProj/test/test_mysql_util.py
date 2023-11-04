
from RetailProj.util.mysql_util import MySQLUtil,get_processed_files
from unittest import TestCase
from RetailProj.config import proj_config
class TestMySQLUtil(TestCase):
    def setUp(self) -> None:
        self.db_util = MySQLUtil()

    def test_mysql_util_query(self):
        self.db_util.select_db("bigdata_db")
        self.db_util.check_table_exists_and_create(
            "bigdata_db",
            "for_unittest_table",
            "id int primary key, name varchar(20)")
        self.db_util.execute("TRUNCATE table for_unittest_table")
        self.db_util.execute(f"INSERT INTO for_unittest_table values (1,'laura'),(2,'eric')")
        result=self.db_util.query("SELECT * FROM for_unittest_table ORDER BY id")
        expected=((1,'laura'),(2,'eric'))
        self.assertEqual(expected,result)

        self.db_util.execute("DROP TABLE for_unittest_table")
        self.db_util.close_conn()
    def test_execute_without_autocommit(self):
        self.db_util.conn.autocommit(True)
        self.db_util.select_db('bigdata_db')
        self.db_util.check_table_exists_and_create(
            "bigdata_db",
            "for_unit_test2",
            "id int primary key, name varchar(20)"
        )
        self.db_util.execute("TRUNCATE for_unit_test2")
        self.db_util.execute_without_autocommit("insert into for_unit_test2 values(1,'laura'),(2,'eric')")
        result=self.db_util.query("SELECT * FROM for_unit_test2")
        expected=((1,'laura'),(2,'eric'))
        self.assertEqual(expected,result)
        self.db_util.conn.close()

        new_util = MySQLUtil()
        new_util.select_db("bigdata_db")
        new_util.conn.autocommit(False)
        new_util.execute_without_autocommit("insert into for_unit_test2 values(3,'alisa')")
        new_util.conn.close()

        new_util2=MySQLUtil()
        new_util2.select_db("bigdata_db")
        result=new_util2.query("SELECT count(*)  FROM for_unit_test2")
        print(type(result),result)
        self.assertEqual(result,((2,),))
        new_util2.execute("DROP TABLE for_unit_test2")
        new_util2.conn.close()
    def test_get_processed_files(self):
        self.db_util.select_db('metadata')
        self.db_util.check_table_exists_and_create(
            "metadata",
            "test_metadata_file_monitor",
            proj_config.metadata_file_monitor_table_create_cols
        )
        self.db_util.execute(f"truncate test_metadata_file_monitor")
        self.db_util.execute("""
        insert into test_metadata_file_monitor values (3, 'path://asdf/1', 3,'2023-11-11 01:02:03')
        """)
        result= get_processed_files(self.db_util,monitor_table_name="test_metadata_file_monitor")
        self.assertEqual([('path://asdf/1')],result)
        self.db_util.execute("DROP TABLE test_metadata_file_monitor")
        self.db_util.conn.close()









