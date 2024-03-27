"""

列表的定义格式

"""

"""
字面量
[元素1, 元素2, 元素., 元素4, ...]

定义变量
变量名称 = [元素1, 元素2, 元素., 元素4, ...]

定义空列表
变量名称 = []
变量名称 = list()

列表内的每一个数据,称之为元素
以[]作为标识
"""

# 定义一个嵌套列表
name_list = ['hanser', 'charlotte', 'json', 'flashlight', ['honkai', 'genshin', 'starl', [123, True]]]

print(name_list)
print(type(name_list))

# 注意:列表可以一次存储多个数据,且可以为不同的数据类型,支持嵌套

"""
列表的下表索引(从零开始,依次递增)
反向索引,从后往前:从-1开始,依次递减
语法:   列表[下标索引]
如果列表是嵌套的列表,同样也支持下标索引
语法:   列表[下标索引][下标索引]
"""

# print(name_list[0])
# print(name_list[1])

# print(name_list[-1])
# print(name_list[-2])

print(name_list[4][3][1])
print(name_list[-1][-1][-1])

"""
# 列表的功能
1.插入元素
2.删除元素
3.清空列表
4.修改元素
5.统计元素个数
等等这些功能,都称之为:列表的方法
"""

"""
# 列表的查询功能(方法)
# 查找某元素的下标
功能：查找指定元素在列表的下标，如果找不到，报错ValueError
语法：列表.index(元素)
index就是列表的对象(变量)内置的方法(函数)
"""

name_list = ['hanser', 'charlotte', 'json', 'flashlight', ['honkai', 'genshin', 'starl', [123, True]]]

# print(name_list.index("honkai"))

my_list = ['honkai', 'genshin', 'honkai', 'starl']

index = my_list.index("honkai")

print(f"honkai在列表中的下标是{index}")

"""
列表的修改功能(方法)
修改特定位置(索引)的元素值：
语法：列表[下标] = 值
"""
my_list = [1, 2, 3, 4, 5]

# 正向下标
my_list[1] = 1145
print(f"修改下标5后的值是{my_list}")

# 反向下标
my_list[-4] = 1145
print(f"修改下标-4后的值是{my_list}")

"""
插入元素
语法：列表.insert(下标，元素)，在指定的下标位置，插入指定的元素
"""

my_list = [1, 2, 3, 4, 5, 6]

my_list.insert(1, "python")

print(f"在下标1插入元素后是{my_list}")

"""
追加元素：
语法：列表.append(元素)，将指定元素，追加到列表的尾部
"""

i_list = [1, 2, 3, 4, 5, 6]
# 追加单个元素
i_list.append("IKUN")

print(f"在列表中追加元素后是{i_list}")

# 追加一批元素
"""
追加元素方式2
语法：列表.extend(其他数据容器)，将其它数据容器的内容依次取出，依次追加到列表尾部
"""
key_list = [1, 2, 3, 4, 5, 6]

key_list2 = [6, 5, 4, 3, 2, 1]

key_list.extend(key_list2)

print(f"追加{key_list2}后是{key_list}")


"""
删除元素：
语法1：del 列表 [下标]
语法2：列表.pop(下标)
"""

key_list = [1, 2, 3, 4, 5, 6]

del key_list[-1]

print(f"删除-1下标后结果是:{key_list}")

returns = key_list.pop(0)

print(f"删除0下标后结果是:{key_list}, 取出的元素是:{returns}")

"""
删除某元素在列表中的第一个匹配项
语法：列表.remove(元素)
"""

my_list = [1, 1, 4, 5, 1, 4]

my_list.remove(1)

print(f"删除元素1后的结果是:{my_list}")

"""
清空列表内容
语法：列表.clear()
"""

my_list = [1, 1, 4, 5, 1, 4]

my_list.clear()

print(f"清空列表后结果是：{my_list}")

"""
统计某元素在列表内的数量
语法：列表.count(元素)
"""

my_list = [1, 1, 4, 5, 1, 4]

num = my_list.count(1)

print(f"元素1在{my_list}中出现的次数是{num}")

"""
统计列表内，有多少元素
语法：len(列表)
可以得到一个int数字，表示列表内的元素数量
"""

my_list = [1, 1, 4, 5, 1, 4]

print(len(my_list))

# 练习案例

num_list = [21, 25, 21, 23, 22, 20]

num_list.append(31)

print(f"追加31到尾部后结果是:{num_list}")

ps_list = [29, 33, 30]

num_list.extend(ps_list)

print(f"追加{ps_list}到尾部结果是:{num_list}")

print(f"取出第一个元素是:{num_list[0]}")

print(f"取出最后一个元素结果是:{num_list[-1]}")

num = num_list.index(31)
print(f"元素31在{num_list}的下标为{num}")

"""
列表的sort方法
语法：sort(Key=选择排序依据的函数,reverse=True|False)
    参数Key,是要求传入一个函数,表示将列表的每一个元素都传入函数中,返回排序的依据
    参数reverse,是否反转排序结果,True表示降序,False表示升序
"""

ts_list = [['a', 33], ['b', 55], ['c', 11]]


# 定义排序方法
def choose_sort_key(element):
    return element[0]


ts_list.sort(key=choose_sort_key, reverse=False)
print('!!!', ts_list)

# 匿名函数lambda形式
ts_list.sort(key=lambda element: element[1], reverse=True)

print('!!!!', ts_list)

"""
反转列表
语法：列表.reverse()

"""

my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print("!!!!!", my_list)

"""
列表的遍历-while循环
语法：
index = 0
while index < len(list):
    元素 = 列表[index]
    对元素进行处理
    index += 1
"""


def list_while_func():
    """
    使用while循环遍历列表
    :return: None
    """
    my_list = [1, 2, 3, 4, 5]

    # 定义一个变量标记下标的值
    index = 0
    while index < len(my_list):
        # 通过index取出对应的元素
        element = my_list[index]
        print(f"列表的元素:{element}")

        index += 1


"""
列表的遍历-for遍历
语法：
for 临时变量 in 数据容器:
    对临时变量进行处理
"""


def list_for_func():
    """
    使用for循环遍历列表
    :return: None
    """
    my_list = ["one", "two", "three", "four", "five"]

    for i in my_list:
        print(f"列表的元素:{i}")


list_while_func()
list_for_func()


# 练习案例：取出列表内的偶数

def list_while_evenNumber(list_project):
    """
    通过while循环遍历列表，并取出列表里为偶数的元素
    :param list_project: 要遍历的列表
    :return: None
    """

    num_list = []

    index = 0
    while index < len(list_project):
        num = list_project[index]
        if num % 2 == 0:
            num_list.append(num)
        index += 1
    print(f"通过while循环，从列表:{list_project}中取出偶数，组成新列表是:{num_list}")


def list_for_evenNumber(list_project):
    """
    通过fore循环遍历列表，并取出列表里为偶数的元素
    :param list_project: 要遍历的列表
    :return: None
    """

    num_list = []

    for i in list_project:
        if i % 2 == 0:
            num_list.append(i)
    print(f"通过for循环，从列表:{list_project}中取出偶数，组成新列表是:{num_list}")


mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_while_evenNumber(mylist)
list_for_evenNumber(mylist)

