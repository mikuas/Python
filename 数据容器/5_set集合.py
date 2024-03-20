"""
集合的定义
基本语法：
定义集合字面量
{元素，元素，......，元素}
定义集合变量
变量名 = {元素，元素，......，元素}
定义空集合
变量名 = set()
"""

my_set = set()

print(type(my_set))

"""
集合的常用操作--修改
集合是无序的，所以集合不支持下标索引访问
"""

"""
添加新元素
语法：集合.add(元素) 将指定元素，添加到集合内
结果：集合本身被修改，添加了新元素
"""

my_set = {"Hello", "World"}

my_set.add("Miku")

# print(my_set)

"""
移除元素
语法：集合.remove(元素) 将指定元素，从集合内移除
结果：集合本身被修改，移除了元素
"""

my_set = {"Hello", "World", "Miku"}

my_set.remove("Miku")

# print(my_set)

"""
从集合中随机取出元素
语法：集合.pop() 功能：从集合中随机取出一个元素
结果：会得到一个元素的结果，同时集合本身被修改，元素被移除
"""

my_set = {"Hello", "World", "Miku"}

element = my_set.pop()

print(my_set)
print(element)


"""
清空集合
语法：集合.clear
"""

my_set = {"Hello", "World", "Miku"}

my_set.clear()

print(my_set)

"""
取出两个集合的差集
语法：集合1.difference(集合2) 功能：取出集合1和集合2的差集(集合1有而集合2没有的)
结果：得到一个新的集合，集合1和集合2不变
"""

set1 = {1, 1, 4, 5}
set2 = {1, 9, 1, 9}

set3 = set1.difference(set2)

# print(set3)

"""
消除两个几个的差集
语法：集合1.difference_update(集合2)
功能：对比集合1和集合2，在集合1内，删除集合2相同的元素。
结果：集合1被修改，集合2不变
"""

set1 = {1, 1, 4, 5}
set2 = {1, 9, 1, 9}

set1.difference_update(set2)

# print(set1)
# print(set2)

"""
两个集合合并为一个
语法：集合1.union(集合2)
功能：将集合1和集合2组成新集合
结果：得到新集合，集合1和集合2不变
"""

set1 = {1, 1, 4, 5}
set2 = {1, 9, 1, 9}

set3 = set1.union(set2)

# print(set3)

"""
统计集合元素数量
语法：len(集合)
"""

set1 = {1, 1, 4, 5}

# print(len(set1))

"""
集合的遍历
集合不支持下标索引，所以不能用while循环
"""


def set_for(my_set):
    """
    通过for循环遍历集合
    :param my_set: 要遍历的集合
    :return: None
    """

    for i in my_set:
        print(i)


set1 = {1, 2, 4, 5, 3, 6}

set_for(set1)

# 练习案例

my_list = ["hanser", "charlotte", "hanser", "charlotte", "miku", "ikun", "miku", "ikun"]

my_set = set()


def list_for(data):

    for i in data:
        my_set.add(i)


list_for(my_list)
print(my_set)


