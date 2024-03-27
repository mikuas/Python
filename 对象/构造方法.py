"""
构造方法
__init__()方法，称之为构造方法
可以实现：
        在创建类对象(构造类)的时候，会自动执行
        在创建类对象(构造类)的时候，将传入参数自动传递给__init__方法使用，借此特性可以给成员变量赋值
在构造方法内定义成员变量，需要使用self关键字
"""


class Id:

    # name = None
    # age = None
    # gender = None
    # 可以省略

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


id_1 = Id("miku", 18, 114514)

print(f"Hi大家好,我是{id_1.name},{id_1.age}岁,性别{id_1.gender}")




