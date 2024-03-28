"""
私有成员
类中提供了私有成员的形式来支持
    私有成员变量
    私有成员方法

定义私有成员变量的方式非常简单，只需要：
    私有成员变量：变量名以__开头(2个下滑线)
    私有成员方法：方法名以__开头(2个下划线)
即可完成私有成员的设定
"""


class Phone:
    IMEI = None
    Name = None

    __WF5 = '我是5G网络'
    __CPU_HZ = 2.4

    @staticmethod
    def __CPU_ONEHZ():

        print("CPU以单核模式运行")

    # 私有成员变量/方法只能在内部使用
    # 类对象无法直接访问私有成员，类中的其他成员可以访问私有成员
    def call_by_5g(self):

        if self.__CPU_HZ > 3:
            print(f"已开启5G通话")
        else:
            self.__CPU_ONEHZ()


# phone = Phone()
# phone.IMEI = 114514
# phone.Name = 'HUAWEI'

# print(f"IMEI={phone.IMEI}\nName={phone.Name}")

# phone.call_by_5g()


class Phone_HUAWEI:

    def __init__(self, imem, name):
        self.IMEI = imem
        self.Name = 'HUAWEI_' + name

    __is_5G_enable = False

    def __check_5G(self):

        if self.__is_5G_enable:
            print("5G开启")
        else:
            print("5G关闭，使用4G网络")

    def call_by_5G(self):

        self.__check_5G()


phone = Phone_HUAWEI(114514, "Meat_60Pro")

print(f"IMEI={phone.IMEI}\nName={phone.Name}")
phone.call_by_5G()
