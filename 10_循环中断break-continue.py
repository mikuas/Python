"""

continue

"""

"""

for i in range(1):
    print(1)
    for j in range(1):
        print(2)
        continue
        print(3)
    print(4)

"""

import random

for i in range(5):
    print(1)
    for j in range(5):
        break
        print(2)
    break
    print(3)

# 练习案例：发工资

# 定义账户余额
money = 10000

for i in range(1, 21):
    num = random.randint(1, 10)
    if money < 1000:
        print("工资发完了，下个月领取吧。")
        break
    elif num > 5:
        money -= 1000
        print(f"向员工{i}发放工资1000元，账户余额还剩{money}元。")
    else:
        print(f"员工{i}，绩效分{num}，低于5，不发工资，下一位。")
