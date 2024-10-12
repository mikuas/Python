"""
字典的定义
字典的定义同样使用{}，不过存储的元素是一个个的：键值对，
定义字典字面量
{key:value,key:value......,key:value}
定义字典变量
my_dict = {key:value,key:value......,key:value}
定义空字典
my_dict = {}
my_dict = dict()
"""

# 定义字典

my_dict = {"王力鸿": 99, "周杰轮": 88, "林俊节": 77}

# 定义重复key的字典
my_dict = {"周杰轮": 99, "周杰轮": 88, "林俊节": 77}

# print(my_dict)

"""
字典数据的获取
字典同集合一样，不可以使用下标索引
但是字典可以通过key值来取得对应的value
"""

my_dict = {"王力鸿": 99, "周杰轮": 88, "林俊节": 77}

# print(my_dict["王力鸿"])
# print(my_dict["周杰轮"])
# print(my_dict["林俊节"])

"""
字典的嵌套
字典key和value可以是任意数据类型(key不可为字典)
"""

my_dict = {
    "王力鸿": {
        "语文": 77,
        "数学": 66,
        "英语": 55
    },
    "周杰轮": {
        "语文": 88,
        "数学": 77,
        "英语": 66
    },
    "林俊节": {
        "语文": 99,
        "数学": 88,
        "英语": 77
    }
}

# print(f"周杰轮的语文成绩是{my_dict["周杰轮"]["语文"]}")

# print(f"林俊节的英语成绩是{my_dict["林俊节"]["英语"]}")

"""
新增元素
语法：字典[key] = value 结果：字典被修改，新增了元素
"""

"""
更新元素
语法：字典[key] = [value] 结果：字典被修改，元素被更新
注意：字典key不可以重复，所以对已存在的key执行上述操作，就是更行value值
"""

my_dict = {"王力鸿": 99, "周杰轮": 88, "林俊节": 77}

# 新增元素
my_dict["蔡徐坤"] = 24

# print(my_dict)
# 更新元素
my_dict["周杰轮"] = 100

# print(my_dict)

"""
删除元素
语法：字典.pop(key)
结果：获得指定key的value，同时字典被修改，指定key的数据被删除
"""

my_dict = {"王力鸿": 99, "周杰轮": 88, "林俊节": 77}

value = my_dict.pop("王力鸿")

# print(value)
# print(my_dict)

"""
清空字典
语法：字典.clear() 
结果：字典被修改，元素被清空
"""

my_dict = {"王力鸿": 99, "周杰轮": 88, "林俊节": 77}

my_dict.clear()

# print(my_dict)

"""
获取全部的key
语法：字典.keys()
结果：得到字典中的全部key
"""

my_dict = {"王力鸿": 99, "周杰轮": 88, "林俊节": 77}

keys = my_dict.keys()

# print(keys)


# def dict_value_for(date):
#     """
#     通过传入字典，遍历key分别取出对应的value值
#     :param date: dict
#     :return: None
#     """
#
#     global keys
#
#     keys = date.keys()
#     for key in keys:
#
#         element = my_dict[key]
#         print(f"{key}的成绩是{element}")
#

def dict_for(my_dict):
    """
    通过传入字典，遍历key分别取出对应的value值
    :param my_dict: dict
    :return: None
    """

    for key in my_dict:
        print(f"{key}的成绩是{my_dict[key]}")


# dict_value_for(my_dict)
# dict_for(my_dict)

"""
统计字典的元素数量
语法：len(字典)
"""

my_dict = {"王力鸿": 99, "周杰轮": 88, "林俊节": 77}

# print(len(my_dict))

# 练习案例


my_dict = {
    "王力鸿": {
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    },
    "周杰轮": {
        "部门": "市场部",
        "工资": 5000,
        "级别": 2
    },
    "林俊节": {
        "部门": "市场部",
        "工资": 7000,
        "级别": 3
    },
    "张学油": {
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    },
    "刘德滑": {
        "部门": "市场部",
        "工资": 6000,
        "级别": 2
    }
}


# def employee_data(dict_data):
#     """
#     通过传入的数据查询key的value值
#     :param dict_data: dict
#     :return: None
#     """
#
#     print("全体员工的数据如下:")
#     for key in my_dict:
#         print(f"{key}: {my_dict[key]}")
#
#
# def employee_update_one(dict_date):
#     """
#     通过传入的字典吧级别为1的员工级别分别加1，薪水分别张1000
#     :param dict_date:
#     :return:
#     """
#
#     print("全体员工级别为一的员工完成升职加薪后为:")
#     for key in my_dict:
#         # 通过if判断级别是否为1
#         if my_dict[key]["级别"] == 1:
#             # 级别加1
#             my_dict[key]["级别"] += 1
#             # 工资加1000
#             my_dict[key]["工资"] += 1000
#
#     employee_data(my_dict)
#
#
# # employee_data(my_dict)
#
# employee_update_one(my_dict)

def printDictInfo(element: dict):
    for key, value in element.items():
        print(key, value)

def getNewSalary(element: dict):
    # 级别 1 的加 1000, 级别加 1
    for key in element.keys():
        if element[key]['级别'] == 1:
            element[key]['工资'] += 1000
            element[key]['级别'] += 1


printDictInfo(my_dict)
getNewSalary(my_dict)
print('-----------------------------------------------')
printDictInfo(my_dict)