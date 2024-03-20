"""

for循环遍历字符串

语法格式
for 临时变量 in 待处理的数据集 (序列):
    循环满足条件时执行的代码

序列类型包括：
字符串
列表
元组
等...

"""

strs = "charlotte"
for i in strs:
    print(i)

# 联系案例：数a
name = "i m yours a fack you a list"
a = 0

for i in name:
    if i == "a":
        a += 1

print(a)

"""
range语句

语法1：
range(num)
获取一个从零开始，到num结束的数字序列(不包含num本身)
如range(5)取得的数据是：[0, 1, 2, 3, 4]

语法2：
range(nu1， num2)
获得一个从num1开始，到num2结束的数字序列(不含num2本身)
如，range(5, 10)取得的数据是：[5, 6, 7, 8, 9]

语法3：
range(num1, num2, step)
获得一个从num1开始，到num2结束的数字序列(不含num2本身)
数字之间的步长，以step为准(step默认是1)
如，range(5, 10, 2)取得的数据是：[5, 7, 9]

"""

for i in range(10):
    print(i)

for i in range(5, 10):
    print(i)

for i in range(5, 10, 2):
    print(i)

# 联系案例：有几个偶数

num = 0

for i in range(1, 100):
    if i % 2 == 0:
        num += 1

print(f"1到100(不含100本身)范围内，有{num}个偶数")

"""
x = 1145
for x in range(5):
    print(x)
print(x)
"""

# for循环嵌套

i = 0
for i in range(1, 101):
    print(f"今天是向美表白的第{i}天")
    for j in range(1, 11):
        print(f"今天送了小美{j}朵玫瑰花")
print(f"表白第{i}天，表白成功")

# for循环打印99乘法表

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {j * i}\t", end='')
    print()
