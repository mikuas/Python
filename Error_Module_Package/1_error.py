"""
异常的捕获的作用在于：提前假设某处会出现异常，做好提前准备，当真的出现异常的时候，可以有后续手段

捕获常规异常
语法：try:
        可能发生错误的代码
    except:
        如果出现异常执行的代码
"""

# try:
#     file_r = open("C:/IKUN", 'r', encoding='UTF-8')
#
# except:
#     print("捕获CG")

"""
捕获指定异常
语法：try:
        print(name)
    :except [异常 as 别名]:
        print('name变量名称未定义错误')

注意：如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常
一般try下方只放一行尝试执行的代码
"""

# try:
#     print(name)
#
# except NameError as e:
#     print('name变量名称未定义错误')

"""
捕获多个异常
当捕获多个异常时，可以把要捕获的异常类型的名字，放到except后，并使用元组的方式进行书写
语法：try:
    print(1/0)
    except(ZeroDivisionError, NameError):
    print(ZeroDivisionError错误)
"""

# try:
#     print(name)
#     1 / 0
#
# except(ZeroDivisionError, NameError):
#     print('!!!')

"""
捕获所有异常
语法：try:
        print(name)
     except [Exception as 别名]:
      print('')
"""

# try:
#     open('C:/IKUN', 'r')
#
# except Exception as a:
#     print("出现异常了")


"""
异常else
else表示的是如果没有异常要执行的代码
语法：try:
        print(name)
     except [Exception as 别名]:
     print('')
     else:
        print('')
"""


# try:
#     # with open('C:/IKUN', 'r', encoding='UTF') as f:
#     #     print(f.read())
#     print(True)
# except Exception as a:
#     print('!')
#
# else:
#     print(None)

"""
异常的finally
finally表示的是无论是否异常都要执行的代码，列如关闭文件
语法：try:
        print(name)
     except [Exception as 别名]:
     print('')
     else:
        print('')
     finally:
        f.close()
"""


"""
异常的传递性
"""


# 定义一个有异常的方法
def fuck_a():
    print("--1--")
    Eroor = 1 / 0


# 定义一个无异常的方法，调用有异常的方法
def fuck_b():
    print("--2--")
    fuck_a()


# 定义一个方法，调用上面的方法
def try_except():
    try:
        fuck_b()
    except Exception as er:
        print(er)


try_except()

