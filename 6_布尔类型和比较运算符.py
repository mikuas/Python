"""

比较运算符

"""

result = 10 > 5
print(f"10 > 5 的结果是：{result}, 类型是：{type(result)}")

result = "hanser" == "charlotte"
print(f"字符串hanser是否和charlotte相等，结果是：{result}, 类型是：{type(result)}")

# 定义变量存储布尔类型

bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是：{bool_1}, 类型是：{type(bool_1)}")
print(f"bool_2的变量内容是：{bool_2}, 类型是：{type(bool_2)}")

"""

比较运算符的使用
==, !=, >, <, >=, <=

"""

num1 = 10
num2 = 10
print(f"10 == 10的结果是：{num1 == num2}")

num2 = 15
print(f"10 != 15的结果是：{num1 != num2}")

name1 = 'dadliya'
name2 = 'fenyvany'
print(f"dadliya == fenyvany的结果是：{name1 == name2}")

num1 = 10
num2 = 5
print(f"10 > 5的结果是：{num1 > num2}")
print(f"10 < 5的结果是：{num1 < num2}")

num1 = 10
num2 = 10
print(f"10 >= 5的结果是：{num1 >= num2}")
print(f"10 <= 5的结果是：{num1 <= num2}")