"""
闭包
在函数嵌套的前提下,内部函数使用了外部函数的变量,并且外部函数返回了内部函数,我们把这个使用外部函数变量的内部函数称之为闭包

# 定义双层嵌套函数,内层函数可以访问外层函数的变量
# 将内层函数作为外层函数的返回,此内层函数就是闭包函数
"""


# def account_create(initial_amount=0):
#
#     def atm(num, deposits=True):
#         nonlocal initial_amount
#         if deposits:
#             initial_amount += num
#             print(f"存款:+{num}元,账户余额{initial_amount}元")
#         else:
#             initial_amount -= num
#             print(f"取款:-{num}元,账户余额{initial_amount}元")
#
#     return atm


# ATM = account_create()
#
# ATM(500)
# ATM(500, deposit=False)
#
# account_create()(500)
# account_create()(200)


def idName(name: str = 'miku'):

    def result(age: int):

        print(f'<{name}>, {age}, <{name}>')

    return result


idName()(24)

fn = idName('hanser')

fn(18)

print(type(fn))


def outer(initial_amount):

    def inner(num: int, bol: bool = True):

        # 修改外部变量的值,需要加nonlocal关键字
        nonlocal initial_amount
        if bol:
            initial_amount += num
            print(f'存款{num}元,余额{initial_amount}元')
        else:
            initial_amount -= num
            print(f'取{num}款元,余额{initial_amount}元')

    return inner


atm = outer(1000)

atm(50)
atm(550, bol=False)

"""
优点,使用闭包可以让我们得到:
    无需定义全局变量即可实现通过函数,持续的访问,修改某个值
    闭包使用的变量的所用于在函数内,难以被错误的调用修改
缺点:
    由于内部函数持续引用外部函数的值,所以会导致这一部分内存空间不被释放,一直占用内存
"""


