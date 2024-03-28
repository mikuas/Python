
# 复写

class Phone:

    IMEI = None
    producer = "IKUN"

    # @staticmethod
    def call_by_5G(self):
        print("父类5G")


class New_Phone(Phone):

    producer = "MIKU"       # 复写父类成员

    # @staticmethod
    def call_by_5G(self):   # 复写父类方法
        print('子类5G')

    def father_member(self):
        # 调用父类成员，方式1
        print(f"父类producer={Phone.producer}")
        Phone.call_by_5G(self)
        # 调用父类成员，方式2
        print(f"父类producer={super().producer}")
        super().call_by_5G()


"""
调用父类成员
    使用成员变量:父类名.成员变量
    使用成员方法:父类名.成员方法(self)
    
使用super()调用父类成员
    使用成员变量:super().成员变量
    使用成员方法:super().成员方法()    
"""

phone = New_Phone()
phone.call_by_5G()
phone.father_member()
















