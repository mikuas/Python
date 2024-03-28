import random

i = 0
while i < 100:
    print("小美，我喜欢你")
    i += 1

# 1-100
num = 1
add = 0
while num <= 100:
    add += num
    num += 1
print(add)
"""
# 猜数字
# 获取随机数
num = random.randint(1, 100)
t = True
# 设置次数提示
i = 0
# 无限循环，直到猜中
while t:
    # 每猜一次就加1
    i += 1
    # 获取键盘的输入
    one = int(input("请输入您猜的数："))
    if one == num:
        print(f"恭喜你猜对了，你一共猜了{i}次")
        # 如果猜对就结束
        t = False
    else:
        if one > num:
            print("大了")
        else:
            print("小了")

"""
# 定义外层循环的变量
a = 1
while a <= 9:
    # 定义内存循环的变量
    i = 1
    while i <= a:
        # 内层循环输出不换行 end='' 对齐\t
        print(f"{i} * {a} = {a * i}\t", end="")
        i += 1
    a += 1
    # 空的print输出一个换行
    print()

# print输出不换行

print("Hello", end='')
print("World")

# 制表符\t
print("Hello\t World")
print("hanser\t qiuck")
