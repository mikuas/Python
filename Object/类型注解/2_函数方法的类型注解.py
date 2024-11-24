
"""
函数(方法)的类型注解-形参注解
语法：
    def 函数方法名(形参名: 类型, 形参名: 类型,......)
    pass
"""


def add(a: int, b: int, *data: list):

    return a + b


num = add(1, 1)
print(num)

"""
函数(方法)的类型注解-返回值注解
"""


def del_(a: int, b: int) -> int:

    return a - b


del_(1, 1)







