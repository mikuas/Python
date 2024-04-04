"""
连接到mysql数据库
"""

from pymysql import Connection

# 获取到MySQL数据库的链接对象
conn = Connection(
    host='localhost',       # 主机名(IP地址)
    port=3306,              # 端口，默认3306
    user='root',            # 账户名
    password='123456',   # 密码
    autocommit=True         # 自动提交
)

# 打印MySQL数据库软件信息
# print(conn.get_server_info())
# 关闭到数据库的链接
# conn.close()

# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db('ikun')

# 使用游标对象，执行sql语句
# 执行非查询性质的SQL语句：
# cursor.execute("create table student(id int)")

# 执行查询性质的SQL语句：
# conn.select_db('object')
# cursor.execute("select * from object")

# 获取查询结果
# result: tuple = cursor.fetchall()
# for i in result:
#     print(i)
#     for line in i:
#         print(line)

# cursor.execute("create table test(id int, name varchar(10), age int)")

# cursor.execute("insert into object values (12, 'js', 114, '男'), (24, 'vue', 115, '女')")
# 通过commit确认
# conn.commit()

# cursor.execute("select * from object")

result: tuple = cursor.fetchall()
for i in result:
    print(i)

conn.close()
