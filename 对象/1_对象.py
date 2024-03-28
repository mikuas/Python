
"""
使用对象组织数据
在程序中设计表格，我们称之为：设计类(class)
class Student:
    name = None

在程序中打印生产表格，我们称之为：创建对象
# 基于类创建对象
    stu_1 = Student()
    stu_2 - Student()

在程序中填写表格，我们称之为：对象属性赋值
    stu_1.name = 'ikun'     为学生1对象赋予名称属性值
    stu_2.name = 'miku'     为学生2对象赋予名称属性值


类的定义和使用
语法： 类名称:
    类的属性
    类的行为
        class是关键字，表示要定义类了
        类的属性，即定义在类中的变量(成员变量)
        类的行为，即定义在类中的函数(成员方法)

创建类对象的语法：
对象 = 类名称()
"""


class Student:

    name = None                 # 记录学生姓名
    gender = None               # 记录学生性别
    nationality = None          # 记录学生国籍
    native_place = None         # 记录学生籍贯
    age = None                  # 记录学生年龄

    def hi(self):
        print(f"Hi大家好，我是{self.name}")


stu_1 = Student()
stu_2 = Student()

stu_1.name = 'hanser'
stu_1.gender = 'man.reverse'
stu_1.nationality = 'China'
stu_1.native_place = '1145'
stu_1.age = 24

stu_2.name = 'miku'
stu_2.gender = 'man.reverse'
stu_2.nationality = 'China'
stu_2.native_place = '0721'
stu_2.age = 18


print(f"学生{stu_1.name}的性别是{stu_1.gender},国籍是{stu_1.nationality},籍贯是{stu_1.native_place},年龄是{stu_1.age}岁")
print(f"学生{stu_2.name}的性别是{stu_2.gender},国籍是{stu_2.nationality},籍贯是{stu_2.native_place},年龄是{stu_2.age}岁")

stu_1.hi()

"""
定义成员方法的定义语法
def 方法名(self，形参1，......，形参N):
    方法体
self关键字是成员方法定义的时候，必须填写的
    它用来表示类对象自身的意思
    当我们使用类对象调用方法时，self会自动被python传入
    在方法内部，想要访问类的成员变量，必须使用self
"""


class Clock:

    id = None
    price = None

    # def ring(self):
    #     import winsound
    #     winsound.Beep(1000, 2000)


clock_1 = Clock()

# clock_1.ring()




