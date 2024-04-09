"""
通过MySQL数据库取出数据
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
# 获取游标对象
cursor = conn.cursor()
# 通过execute调用库
cursor.execute('use commodity_data')

cursor.execute('show tables')
cursor.execute('select * from object')
# 通过fetchall返回值获取object表的内容
result: tuple = cursor.fetchall()

file_w = open("C:/Users/Administrator/Desktop/mysql.txt", 'w', encoding="UTF-8")

mysql_commodity = []
dict_mysql_commodity = {}
num = 1
# for循环,把object的内容依次追加到列表中
for line in result:
    """
    # 通过下标取得对应的元素
    mysql_commodity.append([line[0], line[1], line[2], line[3]])
    dict_mysql_commodity[num] = {}
    dict_mysql_commodity[num]['date'] = str(line[0])
    dict_mysql_commodity[num]['order_ID'] = line[1]
    dict_mysql_commodity[num]['money'] = line[2]
    dict_mysql_commodity[num]['province'] = line[3]
    num += 1
    """
    # 将数据写入文件
    file_w.writelines('{'f'"date":"{str(line[0])}", "orders_id":"{line[1]}",'
                      f' "money":{int(line[2])}, "province":"{line[3]}"''}\n')
    # try:
    #     dict_mysql_commodity[str(l[0]ine[0])].append((line[1], line[2], line[3]))
    #
    # except KeyError:
    #     dict_mysql_commodity[str(line[0])] = []
    #     dict_mysql_commodity[str(line[0])].append((line[1], line[2], line[3]))

# print(mysql_commodity)
# print(dict_mysql_commodity)

# 关闭文件
file_w.close()

