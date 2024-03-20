"""

函数：是组织好的，可重复使用的，用来实现特定功能的代码段。

"""

# 统计字符串长度

strs = "hanser_charlotte"
n = 0
for i in strs:
    n += 1
print(n)

"""

函数的定义：
def 函数名(传入参数):
    函数体
    return 返回值
    
函数的调用：
函数名(参数)

注意事项
1.参数如果不需要，可以省略
2.返回值如果不需要，可以省略
3.函数必须先定义后使用

"""


def my_len(lenght):
    count = 0
    for i in lenght:
        count += 1
    print(f"字符串{lenght}的长度是{count}")


my_len(strs)


# 定义函数
def hei():
    print("Hi 我是颠佬")


# 调用函数
hei()


def add():
    result = 1 + 2
    print(f"1 + 2的结果是:{result}")


add()


def add(a, b):
    result = a + b
    print(f"{a}+{b}的结果是:{a + b}")


add(2, 5)


def calc(x, y, z):
    if y == "+":
        print(f"{x}+{z}={x + z}")
    elif y == "-":
        print(f"{x}-{z}={x - z}")
    elif y == "*":
        print(f"{x}*{z}={x * z}")
    elif y == "/":
        print(f"{x}/{z}={x / z}")
    elif y == "%":
        print(f"{x}%{z}={x % z}")
    elif y == "**":
        print(f"{x}**{z}={x ** z}")
    elif y == "//":
        print(f"{x}//{z}={x // z}")
    else:
        print("输入错误，请重新输入！")


calc(1145, '+', 1919)


def temperature(C):
    if C <= 37.5:
        print("欢迎来到lt，请出示您的体温")
        print(f"体温测量中，您的体温是：{C}度，体温正常请进")
    else:
        print("欢迎来到lt，请出示您的体温")
        print(f"体温测量中，您的体温是：{C}度，需要gl")


temperature(15)


"""

程序中的返回值

"""


def nd(a, b):
    result = a + b
    return result
# return后的代码都不会执行


r = nd(1, 3)
print(r)


"""

None类型
None表示：空的，无实际意义的意思
函数返回的None，就表示，这个函数没有返回什么有意义的内容
也就是返回了空的意思
在if判断中，None等同于False

"""

# 定义变量，但暂时不需要变量有具体值，可以用None来代替
name = None


# None用于if判断
def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None


result = check_age(16)
# not 取反
if not result:
    # 进入if表示result是None值，也就是False
    print("<18")

# 函数的说明文档


def quick(x, z):
    """
    quick函数可以接收两个参数，进行两数相加的功能
    :param x:   形参x表示相加的其中一个数
    :param z:   形参y表示相加的另一个数
    :return:    None
    """
    print(f"{x} + {z} = {x + z}")


quick(24, 14)

# 函数的嵌套调用


def fuck_b():
    print("---2---")


def fuck_a():
    print("---1---")

    # 嵌套调用fuck_b
    fuck_b()

    print("---3---")


fuck_a()

"""

局部变量
所谓局部变量就是定义在函数体内部的变量，即只在函数体内部生效
局部变量的作用：在函数体内部，临时保存数据，即当函数调用完成后，则销毁局部变量

全局变量
所谓全局变量，指的是在函数体内，外都能生效的变量

"""

"""

global关键字声明全局变量

"""

two = 100


def testA():
    print(two)


def testB():
    # global 关键字声明two是全局变量
    global two
    two = 200
    print(two)


testA()
testB()
print(f"全局变量two={two}")

# ATM
# 定义全局变量
money = 5000000
name = None


name = input("请输入您的姓名：")


# 定义主菜单函数
def atm():
    print("----------主菜单----------")
    print(f"{name}，欢迎来到银行ATM，请选择操作：")
    print("查询余额\t[输入1]")    # 通过\t制表符对齐
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")


# 定义查询余额函数
def luck_money(shel):
    if shel:
        print("----------查询余额----------")
    print(f"{name}，您的余额剩余：{money}元")


# 定义存款函数
def cun_kuai():
    print("----------存款----------")
    global money
    qu_money = int(input("请输入您要存的金额："))
    money += qu_money
    print(f"{name}，您存款{qu_money}元成功")
    luck_money(False)


# 定义取款函数
def qu_kuan():
    print("----------取款----------")
    global money
    cun_money = int(input("请输入您要取的金额："))
    # 通过if判断余额是否大于或等于取款金额,如果小于则提示余额不足
    if money - cun_money < 0:
        print(f"您的余额不足，还有{money}元")
    else:
        money -= cun_money
        print(f"{name}，您取款{cun_money}元成功")
        luck_money(False)


# 通过无限循环,确保程序不退出
while True:
    keybody_num = atm()
    if keybody_num == "1":
        luck_money(True)
    elif keybody_num == "2":
        cun_kuai()
    elif keybody_num == "3":
        qu_kuan()
    elif keybody_num == "4":
        break
    else:
        print("您的输入有误,请重新输入!")
