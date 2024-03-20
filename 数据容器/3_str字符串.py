"""
字符串的下标(索引)
和其他容器列表/元组一样，字符串也可以通过下标进行访问
从前向后，下标从0开始
从后往前，下标从-1开始

字符串是一个无法修改的数据容器
"""

my_str = "fuck you"

# 通过下标索引取出元素
print(my_str[5])

# 通过指定元素查找指定下标索引
# 语法：字符串.index(字符串)
print(my_str.index("y"))

"""
字符串的替换
语法：字符串.replace(字符串1,字符串2)
功能：将字符串内的全部内容：字符串1，替换为字符串2
注意：不是修改字符串本身，而是得到了一个新的字符串
"""

my_str = "fuck in the fuck"

new_my_str = my_str.replace("fuck", "good")

print(new_my_str)


"""
字符串的分割
语法：字符串.split(分隔字符串)
功能：按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中
注意：字符串本身不变，而是得到了一个列表对象
"""

my_str = "Hello World Fan Ikun"

new_list = my_str.split(' ')

print(new_list)

"""
字符串的规整操作(去除前后空格,回车换行符)
语法：字符串.strip()
字符串本身不变，而是得到了一个新的字符串
字符串的规整操作(去除前后指定字符串)
语法：字符串.strip(字符串)-->按照单个字符
"""

my_str = " Hello World "

new_str = my_str.strip()

print(my_str)
print(new_str)

my_str = "114Hello World114"

new_str = my_str.strip("14")

print(my_str)
print(new_str)

# 统计字符串中某字符串出现的次数,count

my_str = "114Hello World114"

count = my_str.count("l")

print(f"字符串{my_str}中l出现的次数是{count}次")

# 统计字符串的长度,len

my_str = "114Hello World114"

print(len(my_str))


def while_str(my_str):
    """
    while循环遍历字符串
    :param my_str: 要遍历的字符串
    :return: None
    """

    index = 0
    while index < len(my_str):
        print(my_str[index])

        index += 1


def for_str(my_str):
    """
    for循环遍历字符串
    :param my_str: 要遍历的字符串
    :return: None
    """

    for i in my_str:
        print(i)


st = "Hello World"

while_str(st)

for_str(st)

# 练习案例

my_str = "itheima itcast boxuegu"

nu = my_str.count("it")
print(f"字符串{my_str}中有{nu}个it")

new_str = my_str.replace(" ", "|")
print(f"将{my_str}中的空格替换为|后为{new_str}")

new_str = new_str.split("|")
print(f"按照|分隔后为{new_str}")
