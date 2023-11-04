from RetailProj.util import file_util,logging_util
from RetailProj.util.mysql_util import MySQLUtil, get_processed_files
from RetailProj.config import proj_config as config
from RetailProj.model.retail_order_model import OrdersModel, OrdersDetailModel
import sys
import time

logger=logging_util.init_logger()
logger.info("visited jason_service, start to process jason file....")
''' file path is located in config file'''
# step1: get files need to be processed
# get all filename list
files=file_util.get_dir_files_list(config.json_data_root_path)
logger.info(f'get filelist : {files}')
# get all processed file list from metadata_db
metadata_db_util=MySQLUtil()
# shift MySQLUtil to target db
target_db_util = MySQLUtil(
    config.target_host,
    config.target_data_user,
    config.target_data_password,
    config.target_port,

)
processed_files=get_processed_files(metadata_db_util)
logger.info(f'these file in filelist have already been processed: {processed_files}')
# get new non-proccessed fileslist
need_to_process_files=file_util.get_new_by_cmp_lists(files, processed_files)
logger.info(f'these files need to be processed: {need_to_process_files}')
# step1: processing files
global_count = 0 # count toal processed lines
processed_files_record_dict={} # count processed records in one file
for file in need_to_process_files:
    file_processed_lines_count=0
    order_model_list = []
    order_detail_model_list = []
    for line in open(file, "r", encoding='UTF-8') :
        global_count+=1
        file_processed_lines_count+=1
            # line 就是每一行数据，先将里面的 回车符先删除
        line = line.replace("\n", "")
        order_model = OrdersModel(line)
        order_detail_model = OrdersDetailModel(line)
        order_model_list.append(order_model)
        order_detail_model_list.append(order_detail_model)
    # 数据中有许多的测试数据，receivable的金额非常大，我们做一个简单的判断，大于10000的这个数据我们就不要了
    reserved_models = []
    for model in order_model_list:
        if model.receivable <= 10000:
            reserved_models.append(model)
    order_csv_write_f = open(
        config.retail_output_csv_root_path + config.retail_orders_output_csv_file_name, 'a',
        encoding='UTF-8')

    order_detail_csv_write_f = open(
        config.retail_output_csv_root_path + config.retail_orders_detail_output_csv_file_name, 'a',
        encoding='UTF-8')
        # process the orders: write the reserved orders into the file: order_csv_write_f
    csv_count=0
    for model in reserved_models:
        csv_line = model.to_csv()
        order_csv_write_f.write(csv_line)
        order_csv_write_f.write('\n')
        csv_count+=1
        if csv_count%1000==0:
             order_csv_write_f.flush()
    order_csv_write_f.close()
    # process the order details: write the detail orders into the file: order_detail_csv_write_f
    for model in order_detail_model_list:
        for single_product_model in model.products_detail:
            csv_line = single_product_model.to_csv()
            order_detail_csv_write_f.write(csv_line)
            order_detail_csv_write_f.write('\n')
            csv_count += 1
            if csv_count % 1000 == 0:
                order_detail_csv_write_f.flush()
    order_detail_csv_write_f.close()
    logger.info(f'complete csv file process, saved to : {config.retail_output_csv_root_path}')

    target_db_util.check_table_exists_and_create(
        config.target_db_name,
        config.target_orders_table_name,
        config.target_orders_table_create_cols
    )
    target_db_util.check_table_exists_and_create(
        config.target_db_name,
        config.target_order_details_table_name,
        config.target_order_details_table_create_cols
    )
    logger.info(f'created order table in {config.target_db_name}')
    logger.info(f'created order detail table in {config.target_db_name}')
    for model in reserved_models:
        insert_sql = model.generate_insert_sql()
        target_db_util.select_db(config.target_db_name)
        target_db_util.execute(insert_sql)
        logger.info(f'inserted {model.order_id} into {config.target_db_name}')

    for model in order_detail_model_list:
        insert_sql = model.generate_insert_sql()
        target_db_util.select_db(config.target_db_name)
        target_db_util.execute(insert_sql)
    logger.info(f'inserted {model.order_id}\'s details into {config.target_db_name}')
# file is the processed file name as the dict key, file_processed_lines_count is processed record count as value
    processed_files_record_dict[file]=file_processed_lines_count
    for file_name in processed_files_record_dict.keys():
        # get file processed lines count
         file_processed_lines=processed_files_record_dict[file_name]
         insert_sql=f' insert into {config.metadata_file_monitor_table_name} (file_name,process_lines) values({file_name},{file_processed_lines})'
         metadata_db_util.execute(insert_sql)

metadata_db_util.close_conn()
target_db_util.close_conn()





