"""
工厂模式
将对象的创建由使用原生类本身创建  转换到有特定的工厂方法来创建

好处:
    大批量创建对象的时候有统一的入口,易于代码维护
    当发生修改时,进修改工厂类的创建方法即可
    符合现实世界的模式,即由工厂来制作产品(对象)
"""


# factory
# get
# person


class Person:
    pass


class Worker(Person):
    pass


class Student(Person):
    pass


class Teacher(Person):
    pass


class PersonFactory:

    @staticmethod
    def get_person(p_type):

        if p_type == 'w':

            return Worker()

        elif p_type == 's':

            return Student()

        else:

            return Teacher()


pf = PersonFactory()

worker = pf.get_person('w')
student = pf.get_person('s')
teacher = pf.get_person(None)

print(
    type(worker), '\n',
    type(student), '\n',
    type(teacher), '\n',
)


