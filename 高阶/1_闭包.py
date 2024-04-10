"""
闭包
在函数嵌套的前提下,内部函数使用了外部函数的变量,并且外部函数返回了内部函数,我们把这个使用外部函数变量的内部函数称之为闭包

"""


def account_create(initial_amount=0):

    def atm(num, deposit=True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"存款:+{num}元,账户余额{initial_amount}元")
        else:
            initial_amount -= num
            print(f"取款:-{num}元,账户余额{initial_amount}元")

    return atm


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



