"""
Union类型
使用Union类型可以定义联合类型注解
语法: Union[类型,...,类型]
"""

from typing import Union

my_list: list[Union[int, str, float]] = [1145, 11.45, 'Hello']

my_dict: dict[str, Union[str, int]] = {'name': 'jocker', 'age': 1145}


# 函数(方法)注解
def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:

    return a + b







