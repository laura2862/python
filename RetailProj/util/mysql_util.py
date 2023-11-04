
import pymysql
from RetailProj.config import proj_config as conf
from RetailProj.util import logging_util as init_log

logger=init_log.init_logger()
class MySQLUtil():
    def __init__(self,
            host=conf.meta_host,
            user=conf.meta_user,
            password=conf.meta_password,
            port=conf.meta_port,
            charset=conf.meta_charset,
            autocommit=False):
# create a db connection by pymysql
        self.conn = pymysql.Connection(
            host=host,
            user=user,
            password=password,
            port=port,
            charset=charset,
            autocommit=autocommit,

        )
    logger.info(f'connected {conf.meta_host}:{conf.meta_port} with db ')

    def close_conn(self):
        if self.conn:
            self.conn.close()
    def query(self,sql):
        cursor=self.conn.cursor()
        cursor.execute(sql)
        # after cursor execute the sql, fetchall() is freturning all the records of the table as a tuple((),(),())
        result = cursor.fetchall()
        cursor.close()
        # len(cursor.fetchall())is the number of the records
        logger.info(f'executed sql the result includes {len(result)} records, the executed sql is {sql}')
        return result

    def select_db(self,db):
        self.conn.select_db(db)

    def execute(self,sql):
        cursor=self.conn.cursor()
        cursor.execute(sql)
        logger.info(f'force executed sql :{sql}')
        if not self.conn.get_autocommit():
            self.conn.commit()
        cursor.close()
    def execute_without_autocommit(self,sql):
        cursor=self.conn.cursor()
        cursor.execute(sql)
        logger.debug(f'executed sql :{sql}')
    def check_table_exists(self,db_name,table_name):
        self.conn.select_db(db_name)
        # the result of the 'SHOW TABLE' is returning a tuple like ((table1,),(table2,))
        result= self.query("SHOW TABLES")
        logger.info(f'checking table {db_name}.{table_name} exists')
        return (table_name,) in result
    def check_table_exists_and_create(self,db_name,table_name, create_col):
        if not self.check_table_exists(db_name,table_name):
            create_sql=f'create table {table_name} ({create_col})'
            self.conn.select_db(db_name)
            self.execute(create_sql)
            logger.info(f'create table {table_name} in {db_name}, the create table sentance is {create_sql}')
        else:
            logger.info(f'table {table_name} has already existed in {db_name}')

def get_processed_files(db_util,
                                db_name=conf.metadata_db_name,
                                monitor_table_name= conf.metadata_file_monitor_table_name,
                                file_monitor_table_create_cols=conf.metadata_file_monitor_table_create_cols):

    db_util.check_table_exists_and_create(
        db_name,
        monitor_table_name,
        file_monitor_table_create_cols
    )
    db_util.select_db(conf.metadata_db_name)
    result=db_util.query(f"SELECT file_name from {monitor_table_name}")
    logger.info(f'accessed metadata_db, and get all processed file list {result} in table{monitor_table_name}')
    processed_files=[]
    for i in result:
        processed_files.append(i[0])
    return processed_files






