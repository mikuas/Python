
import random
import json
"""
类型注解
支持：
    变量的类型注解
    函数(方法)形参列表和返回值的类型注解
"""


"""
为变量设置类型注解
语法：变量: 类型
"""
# 基础数据类型注解
var_1: int = 1145
var_2: float = 11.45
var_3: bool = True
var_4: str = 'miku'

my_list: list = [1, 1, 4, 5]
my_tuple: tuple = (1, 1, 4, 5)
my_set: set = {1, 2, 3}
my_dict: dict = {'key': 'value'}
my_str: str = 'miku'

# 容器类型详细注解
my_list: list[int] = [1, 1, 4, 5]
my_tuple: tuple[int, str, bool] = (1, 'ikun', True)
my_set: set[int] = {1, 2, 3}
my_dict: dict[str] = {'key': 'value'}
my_str: str = 'miku'
# !元组类型设置类型详细注解，需要将每一个元素都标记出来
# !字典类型设置类型详细注解，需要2个类型，第一个是Key，第二个是Value


# 类对象类型注解
class Student:
    name = None


stu: Student = Student()

stu.name = 18

# 注释类型注解
# 语法：
#     #type: 类型


def fuck():

    return 24


var_1 = random.randint(1, 10)       # type: int
var_2 = json.loads('{"miku": 123}')      # type: dict[str, int]
var_3 = fuck()                           # type: int

"""
为变量设置类型注解，显示的变量定义，一般无需注解
一般，无法直接看出变量类型之时会添加变量的类型注解
"""

















