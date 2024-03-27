"""
多个返回值
如果一个函数要有多个返回值，只需按照返回值的顺序，写对应顺序的多个变量接受即可
变量之间用逗号隔开
支持不同类型的数据return
"""


def test_return():

    return 11, 45


x, y = test_return()

print(x, y)
















