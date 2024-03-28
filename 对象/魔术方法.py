
"""
构造方法
__init__()方法，称之为构造方法
可以实现：
        在创建类对象(构造类)的时候，会自动执行
        在创建类对象(构造类)的时候，将传入参数自动传递给__init__方法使用，借此特性可以给成员变量赋值
在构造方法内定义成员变量，需要使用self关键字
"""


class Student:

    # name = None
    # age = None
    # 可以省略

    # __init__构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__魔术方法,将内存地址转换为字符串
    def __str__(self):

        return f"Student类对象,name:{self.name},age:{self.age}"

    # __lt__魔术方法,大于/小于符号比较
    def __lt__(self, other):

        return self.age < other.age
        # 返回True/False

    # __le__魔术方法,大于等于/小于等于符号比较
    def __le__(self, other):

        return self.age <= other.age

    # __eq__魔术方法,比较两个对象是否相等
    def __eq__(self, other):

        return self.age == other.age


stu_1 = Student('miku', 18)
stu_2 = Student('hanser', 24)

# print(sut_1)
# print(str(sut_1))

print(stu_1 < stu_2)
print(stu_1 > stu_2)

print(stu_1 <= stu_2)
print(stu_1 >= stu_2)

print(stu_1 == stu_2)
# 练习案例

# class Id:
#
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#
# for i in range(1, 11):
#     print(f"当前录入第{i}位学生信息,总共需录入10位学生信息")
#     name_ = input("请输入学生姓名:")
#     age_ = input("请输入学生年龄:")
#     address_ = input("请输入学生地址:")
#     id_1 = Id(name_, age_, address_)
#     print(f"学生{i}信息录入完成,信息为:[学生姓名:{id_1.name},年龄{id_1.age},地址{id_1.address}]")


