"""
数据的通用转换功能

list(容器) --> 将给定容器转换为列表

str(容器) --> 将给定容器转换为字符串

tuple(容器) --> 将给定容器转换为元组

ser = t(容器) --> 将给定容器转换为集合

"""

my_list = [1, 2, 3, 4, 5]

my_tuple = (1, 2, 3, 4, 5)

my_dict = {'a': 1, 'b': 2, 'c': 3}

my_set = {1, 2, 3, 4, 5}

my_str = 'hello world'

# 容器转列表

"""
print(list(my_list))

print(list(my_tuple))

print(list(my_dict))

print(list(my_set))

print(list(my_str))
"""

# 容器转元组
"""
print(tuple(my_list))

print(tuple(my_tuple))

print(tuple(my_dict))

print(tuple(my_set))

print(tuple(my_str))
"""

# 容器转字符串
"""
print(str(my_list))

print(str(my_tuple))

print(str(my_dict))

print(str(my_set))

print(str(my_str))
"""

# 容器转集合
"""
print(set(my_list))

print(set(my_tuple))

print(set(my_dict))

print(set(my_set))

print(set(my_str))

"""

strs = str(my_list)

print(strs)

strs = strs.split("[],")

print(strs)

lists = list(strs)

print(lists)

"""
容器的通用排序功能
sorted(容器,[revers=True])
<revers默认是False,True表示将结果进行反转>
将给定容器进行排序,排序的结果会变为列表
"""

lists = [1, 1, 4, 5, 1, 4, 1, 9, 1]

new = sorted(lists)

print(lists)

print(new)

print(sorted(my_tuple))
print(sorted(my_str))
print(sorted(my_set))
print(sorted(my_dict))

print(sorted(my_tuple, reverse=True))
print(sorted(my_str, reverse=True))
print(sorted(my_set, reverse=True))
print(sorted(my_dict, reverse=True))

