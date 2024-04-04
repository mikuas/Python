

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

n = 0
data_list = []
while n < 3:
    for line in result[n]:
        if n == 4:
            break
        n += 1
        # data_list.append(line)
        print(type(line))
        print(line)


print(data_list)

