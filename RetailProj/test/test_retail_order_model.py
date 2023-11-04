import json
from unittest import TestCase
from RetailProj.model.retail_order_model import OrdersModel,OrdersDetailModel,SingleProductSoldModel

class TestRetailOrderModel(TestCase):
    def setUp(self) -> None:
        p = """
        {"discountRate": 1, "storeShopNo": "None", "dayOrderSeq": 2, "storeDistrict": "岳麓区", "isSigned": 0, "storeProvince": "湖南省", "origin": 0, "storeGPSLongitude": "112.9297582805157", "discount": 0, "storeID": 1534, "productCount": 1, "operatorName": "OperatorName", "operator": "NameStr", "storeStatus": "open", "storeOwnUserTel": 12345678910, "payType": "cash", "discountType": 2, "storeName": "鑫民批发部", "storeOwnUserName": "OwnUserNameStr", "dateTS": 1542438424000, "smallChange": 0, "storeGPSName": "None", "erase": 0, "product": [{"count": 1, "name": "白沙品包装", "unitID": 8, "barcode": "6901028191043", "pricePer": 10, "retailPrice": 10, "tradePrice": 7.63, "categoryID": 1}], "storeGPSAddress": "None", "orderID": "154243842370215347783", "moneyBeforeWholeDiscount": 10, "storeCategory": "normal", "receivable": 10, "faceID": "", "storeOwnUserId": 1435, "paymentChannel": 0, "paymentScenarios": "OTHER", "storeAddress": "StoreAddress", "totalNoDiscount": 10, "payedTotal": 10, "storeGPSLatitude": "28.16118309320758", "storeCreateDateTS": 1539943545000, "storeCity": "长沙市", "memberID": "0"}
        """
        self.order_model=OrdersModel(p)

    def test_order_generate_insert_sql(self):
        result=self.order_model.generate_insert_sql()
        print(result)
        expected="""
                INSERT IGNORE INTO orders(order_id,store_id,store_name,store_status,store_own_user_id,store_own_user_name,store_own_user_tel,store_category,store_address,store_shop_no,store_province,store_city,store_district,store_gps_name,store_gps_address,store_gps_longitude,store_gps_latitude,is_signed,operator,operator_name,face_id,member_id,store_create_date_ts,origin,day_order_seq,discount_rate,discount_type,discount,money_before_whole_discount,receivable,erase,small_change,total_no_discount,pay_total,pay_type,payment_channel,payment_scenarios,product_count,date_ts) VALUES('154243842370215347783', 1534, '鑫民批发部', 'open', 1435, 'OwnUserNameStr', '12345678910', 'normal', 'StoreAddress', Null, '湖南省', '长沙市', '岳麓区', Null, Null, '112.9297582805157', '28.16118309320758', 0, 'NameStr', 'OperatorName', Null, '0', 'None', '0', 2, 1, 2, 0, 10, 10, 0, 0, 10, 10, 'cash', 0, 'OTHER', 1, 'None')
        """
        self.assertEqual(expected,result)









