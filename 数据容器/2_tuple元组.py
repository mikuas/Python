"""
元组同列表一样，都是可以封装多个，不同类型的元素在内
但最大的不同点在于：
元组一旦定义完成，就不可以修改

定义元组：定义元组使用小括号()，且使用逗号隔开各个数据，数据可以是不同的数据类型

定义元组字面量
(元素， 元素， 元素， ...... ，元素)

定义元组变量
变量名 = (元素， 元素， 元素， ...... ，元素)

定义空元组
变量名 = ()
变量名 = tuple()

注意：元组只有一个数据，这个数据后面要添加括号
"""

# 定义单个元素

tp = ("hello", )
print(type(tp), tp)

# 元组也支持嵌套

tp = ("hello", "world", ("hello", "world"))

# 通过下标索引取出内容
print(tp[2][0])

# 查找某个数据
print(tp.index("world"))

# 统计某个数据在当前元组出现的次数
print(tp.count("hello"))

# 统计元组内的元素个数
print((len(tp)))


# 元组的变量：while


def tuple_while(element_tuple):
    """
    通过while循环遍历元组
    :param element_tuple: 要遍历的元组
    :return: None
    """

    index = 0
    while index < len(element_tuple):
        print(f"元组的内容是{element_tuple[index]}")
        index += 1


# 元组的遍历：for
def tuple_for(element_tuple):
    """
    通过for循环遍历元组
    :param element_tuple: 要遍历的元组
    :return: None
    """

    for i in element_tuple:
        print(f"元组的内容是{i}")


my_tuple = (1, 2, 3, 4, 5)

tuple_while(my_tuple)

my_tuple = ("hello", "world", "element", "for", "ikun")

tuple_for(my_tuple)

# 修改元组内容

lstp = (1, 2, ["Hello", "World"])

print(lstp)
lstp[2][0] = "World"
lstp[2][1] = "Hello"
print(lstp)

# 练习案例

tp = ("周杰伦", 11, ['football', 'music'])

print(f"年龄所在的下标是{tp.index(11)}")

print(f"学生的姓名是{tp[0]}")

del tp[2][0]
print(f"删除学生爱好football后结果是{tp}")

tp[2].insert(0, "coding")
print(f"增加爱好coding后结果是{tp}")
