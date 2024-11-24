"""
多态
多态，指的是：多种状态，及完成某个行为时，使用不同的对象会得到不同的状态
"""
import random


class Animal:

    def speak(self):
        pass


class Dog(Animal):

    def speak(self):
        print("汪汪汪")


class Cat(Animal):

    def speak(self):
        print("喵喵喵")


def make_noise(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()
# 同样的行为(函数),传入不同的对象,得到不同的状态
make_noise(dog)
make_noise(cat)

"""
多态常作用在继承关系上
比如：
    函数(方法)形参声明接收父类对象
    实际传入父类的子类对象进行工作
即：
    以父类做定义声明
    以子类做实际工作
    用以获得同一种行为，不同状态
"""

"""
抽象类(接口)
父类a的b方法，是空实现(pass)
这种设计的含义是：
    父类用来确定有哪些方法
    具体的方法实现，由子类自行决定
这种写法，就叫做抽象类(也可以称之为接口)
抽象类:含有抽象方法的类称之为抽象类
抽象方法:方法体是空实现的(pass)称之为抽象方法
"""


class KT:

    def cool_wind(self):
        print("---制冷---")

    def hot_wind(self):
        print("---制热---")

    def wind_L_R(self):
        print("---左右摆风---")


class GELI(KT):

    def cool_wind(self):
        print('---格力空调快速制冷---')

    def hot_wind(self):
        print('---格力空调快速制热---')

    def wind_L_R(self):
        print('---格力空调左右快速摆风---')


class MEIDI(KT):

    def cool_wind(self):
        print("---美的空调省电制冷---")

    def hot_wind(self):
        print("---美的空调省电制热---")

    def wind_L_R(self):
        print("---美的空调省电左右摆风---")


def kt_All(kt: KT, mode):
    if mode == 'cool':
        kt.cool_wind()
    elif mode == 'hot':
        kt.hot_wind()
    elif mode == 'wind':
        kt.wind_L_R()


Geli = GELI()
Meidi = MEIDI()

kt_All(Geli, 'cool')
kt_All(Meidi, 'cool')









