print("请告诉我你是谁？")
name = input()
print(f"你是：{name}")
"""

input语句可以在要求使用者输入内容前，输出提示内容
注：无论键盘输入什么类型的数据，获取到的数据永远都是字符串类型

"""
name = input("请告诉我你是谁？")
print(f"你是：{name}")

num = input("亲告诉我你的银行卡密码：")
# 数据类型转化
num = int(num)
print("你的银行卡密码类型是：", type(num))

# 欢迎登录小程序

# 定义变量
user_name = input("请告诉我你的名字：")
user_type = input("请告诉我你的VIP等级：")
print(f"您好：{user_name}, 您是尊贵的 {user_type} 用户, 欢迎您的光临")
