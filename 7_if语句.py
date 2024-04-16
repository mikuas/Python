import random

# age = 24
#
# if age >= 18:
#     print("成年了，进去爽吧！")
# else:
#     print("没满18还想进来，鬼！")
# print("24岁，是man")
#
# # 成年人判断
#
# print("欢迎来到tiwat，儿童免费，成人收费")
# # 获取键盘输入
# age = int(input("请输入您的年龄"))
# # 通过if判断是否是成年人
# if age >= 18:
#     print("您已成年，游玩需要补票10元")
# else:
#     print("您未成年，可以免费游玩")
# print("祝您游玩愉快！")
#
# # 练习案例：我要买票吗
#
# # 通过input获取键盘输入的身高
# m = float(input("请输入您的身高(cm)："))
# # 判断身高是否超过120cm
# if m > 120:
#     print("您的身高超过120cm，游玩需要购票10元")
# else:
#     print("您的身高未超出120cm，可以免费游玩")
# print("祝您游玩愉快")
#
# # elif
#
# print("欢迎来到乐土")
# height = float(input("请输入您的身高(cm)："))
# vip = int(input("请输入您的VIP等级(1~5)"))
# if height < 120:
#     print("您的身高小于120cm，可以免费游玩")
# elif vip > 3:
#     print("您的VIP等级大于3，可以免费游玩")
# else:
#     print("条件都不满足，需要购票24元")
# print("祝您游玩愉快！")
#
# # 猜数字
# num = 24
# if int(input("请输入第一次猜的数：")) == num:
#     print("恭喜你第一次就猜对了！")
# elif int(input("不对，再猜一次：")) == num:
#     print("恭喜你第二次猜对了")
# elif int(input("不对，再猜最后一次：")) == num:
#     print("恭喜你最后一次猜对了")
# else:
#     print(f"Sorry，全猜错了，我想的是{num}")

# 定义随机数范围

"""
num = random.randint(1, 10)
nu = int(input("您有三次机会，请输入您猜的数："))
if nu == num:
    print("恭喜你第一次就猜对了!")
else:
    if nu > num:
        print("大了")
    else:
        print("小了")
    nu = int(input("还有两次机会，请输入您猜的数："))
    if nu == num:
        print("恭喜你第二次猜对了")
    else:
        if nu > num:
            print("大了")
        else:
            print("小了")
        nu = int(input("还有最后一次机会，请输入您猜的数："))
        if nu == num:
            print("恭喜你最后一次猜对了")
        else:
            print(f"Sorry，全部猜错了，我想的是{num}")
"""
# if 拓展

# 逻辑运算符：用于连接多个条件，构建复杂的条件表达式。
"""
# and（与）
# or（或）
# not（非）
"""
# 成员运算符：用于检查一个值是否存在于另一个集合中。
"""
# in（存在于）
# not in（不存在于
"""

# 身份运算符：用于比较两个对象的内存地址。
"""
# is（是同一对象）
# is not（不是同一对象）
"""
# 其他可调用的布尔函数：用于检查给定条件的真假。
"""
# all()：如果可迭代对象中的所有元素都为真，则返回 True。
# any()：如果可迭代对象中的任何元素都为真，则返回 True。
"""
a = 5
b = 4
c = [a, b]

if a < 5 or b > 3:
    print("Hello World1")

if a > 2 and b > 4:
    print("Hello World2")

if not a > 2:
    print("Hello World3")

if any([a > 10, b < 20]):
    print("a 大于 10 或者 b 小于 20")

if a is not None:
    print("Hello World4")

if a in c:
    print("Hello World5")

