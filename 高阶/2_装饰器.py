"""
装饰器
装饰器其实可是一种闭包,其功能就是在不破坏目标函数原有的代码和功能的前提下,为目标函数增加新功能

# 装饰器就是使用创建一个闭包函数,在闭包函数内调用目标函数
# 可以达到不改动目标函数的同时,增加额外的功能
"""

# 一般写法(闭包写法)


def outer(func):

    def inner():

        print('我要睡觉了')
        func()
        print("我起床了")

    return inner


def sleep():

    import random
    import time
    print('睡眠中......')
    time.sleep(random.randint(1, 5))


# outer(sleep)()


# 装饰器的语法糖写法


def outer_(func):

    def inner():
        print('我要睡觉了')
        func()
        print('我起床了')

    return inner


@outer_
def sleep_():
    import random
    import time
    print('睡眠中......')
    time.sleep(random.randint(1, 5))


sleep_()

