import pymysql
conn=pymysql.Connection(
    host="localhost",
    port=3306,
    user='root',
    password='wyypnqtyhj199121',
    charset='utf8',
    autocommit='True'
)
####when autocommit set as True
conn.select_db('bigdata_db')
cursor=conn.cursor()
cursor.execute('select * from  category')
####when autocommit set as False
# conn.commit()
result=cursor.fetchall()
print(result, len(result))
r1=cursor.execute("SHOW tables")
print(r1)


conn.select_db('retail')
cursor=conn.cursor()
r2=cursor.execute("SHOW tables")
print(r2)