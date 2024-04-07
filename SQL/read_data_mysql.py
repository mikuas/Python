"""
通过
"""

from pymysql import *


conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456'
)
# 打印MySQL数据库软件信息
print(conn.get_server_info())

cursor = conn.cursor()

cursor.execute('use commodity_data')

cursor.execute('show tables')
cursor.execute('select * from object')

result: tuple = cursor.fetchall()

mysql_commodity = []

for line in result:

    mysql_commodity.append([line[0], line[1], line[2], line[3]])


print(mysql_commodity)

