"""
导入包
方式一：
import 包名.模块名
包名.模块名.目标
"""

# from my_package import module1
#
#
# my_list = [1, 2, 3, 4, 5]
#
# module1.for_list(my_list)
#
# module1.while_list(my_list)


# 练习案例

from my_package import my_tools
from my_package import my_file_tools

my_str = "hanser chrotte"

revers_str = my_tools.str_reverse(my_str)

print(f"字符串{my_str}反转后的结果是{revers_str}")


new_str = my_tools.str_slice(my_str, 0, 6)

print(f"字符串{my_str}按照起始,结束下标,步长0,6,1切片后结果为{new_str}")


my_file_tools.print_file_info("C:/bil.txt")

my_file_tools.append_to_file("C:/bill.txt", "Hello World!")


