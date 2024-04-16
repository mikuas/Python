"""
单列模式
单例模式就是一种编程套路
使用特定的套路得到特定的效果
    单例模式就是对一个类,只获取其唯一的示例对象,持续复用它
        节省内存
        节省创建对象的开销
"""

from test_module import str_tools


s1 = str_tools
s2 = str_tools

print(f'{id(s1)}\n{id(s2)}')



