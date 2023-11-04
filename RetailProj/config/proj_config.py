import time
##################### config log root path start ################################
log_root_path= "/Users/liuwenxuan/Workspace/pythonProject1/RetailProj/log/"
log_name= f'pyETL-{time.strftime("%Y%m%d-%H",time.localtime(time.time()))}.log'
log_path=log_root_path+log_name
##################### config log root path end ################################

##################### config json root path start ################################
json_data_root_path=f"/Users/liuwenxuan/Workspace/testdata"
# 写出CSV的根目录配置
retail_output_csv_root_path = "/Users/liuwenxuan/Workspace/csv/"
# 写出订单模型，CSV的文件名字配置
retail_orders_output_csv_file_name = f'orders-{time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))}.csv'
# 写出订单详情（带商品信息）模型，CSV的文件名字配置
retail_orders_detail_output_csv_file_name = f'orders-detail-{time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))}.csv'

##################### config mysql relates start ################################
######metadata db configuration########
meta_host = 'localhost'
meta_user = 'root'
meta_password = 'wyypnqtyhj199121'
meta_port = 3306
meta_charset = 'utf8'


# save processed data into metadata_file_monitor_table
metadata_db_name = 'metadata'
metadata_file_monitor_table_name = 'processed_file'
metadata_file_monitor_table_create_cols ="""
 id int PRIMARY KEY AUTO_INCREMENT,
    file_name varchar(100) UNIQUE not NULL,
    process_line int comment 'the total line no of processed record',
    processed_time TIMESTAMP DEFAULT current_timestamp COMMENT 'processed time'"""
######data source db configuration########

######target db configuration########
target_host=meta_host
target_data_user=meta_user
target_data_password=meta_password
target_port=meta_port
auth_plugin = 'mysql_native_password'

target_db_name='retail'
target_orders_table_name='orders'
target_orders_table_create_cols = \
    f"order_id VARCHAR(255) PRIMARY KEY, " \
    f"store_id INT COMMENT '店铺ID', " \
    f"store_name VARCHAR(30) COMMENT '店铺名称', " \
    f"store_status VARCHAR(10) COMMENT '店铺状态(open,close)', " \
    f"store_own_user_id INT COMMENT '店主id', " \
    f"store_own_user_name VARCHAR(50) COMMENT '店主名称', " \
    f"store_own_user_tel VARCHAR(15) COMMENT '店主手机号', " \
    f"store_category VARCHAR(10) COMMENT '店铺类型(normal,test)', " \
    f"store_address VARCHAR(255) COMMENT '店铺地址', " \
    f"store_shop_no VARCHAR(255) COMMENT '店铺第三方支付id号', " \
    f"store_province VARCHAR(10) COMMENT '店铺所在省', " \
    f"store_city VARCHAR(10) COMMENT '店铺所在市', " \
    f"store_district VARCHAR(10) COMMENT '店铺所在行政区', " \
    f"store_gps_name VARCHAR(255) COMMENT '店铺gps名称', " \
    f"store_gps_address VARCHAR(255) COMMENT '店铺gps地址', " \
    f"store_gps_longitude VARCHAR(255) COMMENT '店铺gps经度', " \
    f"store_gps_latitude VARCHAR(255) COMMENT '店铺gps纬度', " \
    f"is_signed TINYINT COMMENT '是否第三方支付签约(0,1)', " \
    f"operator VARCHAR(10) COMMENT '操作员', " \
    f"operator_name VARCHAR(50) COMMENT '操作员名称', " \
    f"face_id VARCHAR(255) COMMENT '顾客面部识别ID', " \
    f"member_id VARCHAR(255) COMMENT '顾客会员ID', " \
    f"store_create_date_ts TIMESTAMP COMMENT '店铺创建时间', " \
    f"origin VARCHAR(255) COMMENT '原始信息(无用)', " \
    f"day_order_seq INT COMMENT '本订单是当日第几单', " \
    f"discount_rate DECIMAL(10, 5) COMMENT '折扣率', " \
    f"discount_type TINYINT COMMENT '折扣类型', " \
    f"discount DECIMAL(10, 5) COMMENT '折扣金额', " \
    f"money_before_whole_discount DECIMAL(10, 5) COMMENT '折扣前总金额', " \
    f"receivable DECIMAL(10, 5) COMMENT '应收金额', " \
    f"erase DECIMAL(10, 5) COMMENT '抹零金额', " \
    f"small_change DECIMAL(10, 5) COMMENT '找零金额', " \
    f"total_no_discount DECIMAL(10, 5) COMMENT '总价格(无折扣)', " \
    f"pay_total DECIMAL(10, 5) COMMENT '付款金额', " \
    f"pay_type VARCHAR(10) COMMENT '付款类型', " \
    f"payment_channel TINYINT COMMENT '付款通道', " \
    f"payment_scenarios VARCHAR(15) COMMENT '付款描述(无用)', " \
    f"product_count INT COMMENT '本单卖出多少商品', " \
    f"date_ts TIMESTAMP COMMENT '订单时间', " \
    f"INDEX (receivable), INDEX (date_ts)"
target_order_details_table_name='order_details'
target_order_details_table_create_cols=\
    f"order_id VARCHAR(255) COMMENT '订单ID', " \
    f"barcode VARCHAR(255) COMMENT '商品条码', " \
    f"name VARCHAR(255) COMMENT '商品名称', " \
    f"count INT COMMENT '本单此商品卖出数量', " \
    f"price_per DECIMAL(10, 5) COMMENT '实际售卖单价', " \
    f"retail_price DECIMAL(10, 5) COMMENT '零售建议价', " \
    f"trade_price DECIMAL(10, 5) COMMENT '贸易价格(进货价)', " \
    f"category_id INT COMMENT '商品类别ID', " \
    f"unit_id INT COMMENT '商品单位ID(包、袋、箱、等)', " \
    f"PRIMARY KEY (order_id, barcode)"

##################### config mysql relates  end################################