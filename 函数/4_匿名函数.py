"""
函数作为参数传递

函数本身是可以作为参数，传入另一个函数中进行使用的
将函数传入的作用在于：传入计算逻辑，而非传入数据
"""


def test_fuck(coms):
    result = coms(1, 2)
    print(result)


def compute(x, y):
    return x + y


def coms(x, y):
    return x * y


test_fuck(coms)
test_fuck(compute)

"""
lambda匿名函数
函数的定义中
    def关键字，可以定义带有名称的函数
    lambda关键字，可以定义匿名函数(无名称)
有名称的函数，可以基于名称重复使用
无名称的函数，只可临时使用一次
语法：lambda 传入参数: 函数体(一行代码)
    lambda是关键字，表示定义匿名函数
    
"""

test_fuck(lambda x, y: x - y)

lambdas = lambda x, y: x / y

test_fuck(lambdas)






