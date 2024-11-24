
"""
选择排序
"""

my_list = [1, 2, 4, 114, 514, 19, 19, 81, 0]

for i in range(len(my_list)):
    for j in range(i, len(my_list)):
        if my_list[i] > my_list[j]:

            my_list[i], my_list[j] = my_list[j], my_list[i]

print(my_list)

"""
冒泡排序
"""

my_list = [1, 2, 4, 114, 514, 19, 19, 81, 0]

for i in range(len(my_list)):

    for j in range(len(my_list) - i - 1):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

print(my_list)
