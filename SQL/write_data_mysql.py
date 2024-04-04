"""
通过python写入数据到MySQL
"""

import json
from pymysql import *


class Data:

    def __init__(self, date, orders_id, money, province):

        self.date = date
        self.orders_id = orders_id
        self.money = int(money)
        self.province = province

    def __str__(self):

        return f'{self.date},{self.orders_id},{self.money},{self.province}'


class Write_file:

    def file_read(self) -> list[Data]:

        pass


class Text_file(Write_file):

    def __init__(self, path):

        self.path = path

    def file_read(self) -> list[Data]:

        file_list: list[Data] = []
        file_r = open(self.path, 'r', encoding='UTF-8')
        for line in file_r.readlines():
            line = line.strip()
            line = line.split(',')
            data = Data(line[0], line[1], line[2], line[3])
            # data = Data(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3])
            file_list.append(data)
        file_r.close()
        return file_list


class Json_file(Write_file):

    def __init__(self, path):

        self.path = path

    def file_read(self) -> list[Data]:

        file_r = open(self.path, 'r', encoding='UTF-8')
        file_list: list[Data] = []
        for js in file_r:
            dict_file = json.loads(js)
            # print(dict_file)
            data = Data(dict_file['date'], dict_file['order_id'], dict_file['money'], dict_file['province'])
            file_list.append(data)
        file_r.close()
        return file_list


conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    autocommit=True
)
# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db('commodity_data')

cursor.execute('create table object(date date, order_id varchar(255), money float, province varchar(24))')

text_result = Text_file('C:/2011年1月销售数据.txt').file_read()
json_result = Json_file("C:/2011年2月销售数据JSON.txt").file_read()

all_data = text_result + json_result

for lines in all_data:
    sql = f"insert into object(date, order_id, money, province)" \
            f" values ('{lines.date}', '{lines.orders_id}', {lines.money}, '{lines.province}')"

    # print(sql)

    cursor.execute(sql)


if __name__ == '__main__':

    pass
    result = Text_file("C:/2011年1月销售数据.txt").file_read()
    for i in result:
        print(i)
    js_result = Json_file("C:/2011年2月销售数据JSON.txt").file_read()
    for j in js_result:
        print(j)



