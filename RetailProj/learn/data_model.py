import json
p="""
{"discountRate": 1, "storeShopNo": "None", "dayOrderSeq": 2, "storeDistrict": "岳麓区", "isSigned": 0, "storeProvince": "湖南省", "origin": 0, "storeGPSLongitude": "112.9297582805157", "discount": 0, "storeID": 1534, "productCount": 1, "operatorName": "OperatorName", "operator": "NameStr", "storeStatus": "open", "storeOwnUserTel": 12345678910, "payType": "cash", "discountType": 2, "storeName": "鑫民批发部", "storeOwnUserName": "OwnUserNameStr", "dateTS": 1542438424000, "smallChange": 0, "storeGPSName": "None", "erase": 0, "product": [{"count": 1, "name": "白沙品包装", "unitID": 8, "barcode": "6901028191043", "pricePer": 10, "retailPrice": 10, "tradePrice": 7.63, "categoryID": 1}], "storeGPSAddress": "None", "orderID": "154243842370215347783", "moneyBeforeWholeDiscount": 10, "storeCategory": "normal", "receivable": 10, "faceID": "", "storeOwnUserId": 1435, "paymentChannel": 0, "paymentScenarios": "OTHER", "storeAddress": "StoreAddress", "totalNoDiscount": 10, "payedTotal": 10, "storeGPSLatitude": "28.16118309320758", "storeCreateDateTS": 1539943545000, "storeCity": "长沙市", "memberID": "0"}
"""
p_dict=json.loads(p)
print(p_dict,type(p_dict))
#
# class Person:
#     def __init__(self,id,name,addr):
#         self.id=id,
#         self.name=name,
#         self.addr=addr
#     def to_csv(self,deli=','):
#         return f"{self.id}{deli}{self.name}{deli}{self.addr}"
#     def generate_insert_sql(self):
#         return f"insert into person values ({self.id},{self.name},{self.addr})"
#
# p1=Person(1,'laura','sfdgfbd')
# p2=Person(2,'eric','sfdgfbd')
# print(p1.to_csv(),p2.generate_insert_sql())
#
# str="123.."
# str1=str[:-2]
# print(str,str1)