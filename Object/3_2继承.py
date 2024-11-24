"""
单继承
语法：
    class 类名(父类名):
    类内容体
"""


class Phone:

    # IMEI = None
    # producer = None

    def __init__(self, imei, producer):

        self.IMEI = imei
        self.producer = producer

    @staticmethod
    def call_by_4G():

        print('4G')


class Phone2024(Phone):

    # face_id = None
    def __init__(self, imei, producer, face_id):
        super().__init__(imei, producer)
        self.IMEI = imei
        self.producer = producer
        self.face_id = face_id

    @staticmethod
    def call_by_5G():
        print('5G')


phone = Phone2024(114514, 'ikun', 666)
print(f'IMEi={phone.IMEI}\nproducer ={phone.producer}\nface_id={phone.face_id}')
phone.call_by_5G()


"""
多继承
python的类之间也支持多继承，即一个类，可以继承多个父类
如果父类有同名方法或属性，先继承的优先级高于后继承
"""


class Phone_XM:

    IMEI = None
    producer = None


class NFC_reader:

    __NFC_type = 5
    NFC_producer = 'Miku'

    @staticmethod
    def read_card():
        print('读取NFC卡')

    @staticmethod
    def write_card():
        print('写入NFC卡')

    def NFC_read_version(self):
        return self.__NFC_type


class RemoteControl:

    __RC_type = "红外遥控"

    @staticmethod
    def control():
        print('开启红外遥控')


class MyPhone(Phone_XM, NFC_reader, RemoteControl):
    pass


my_phone = MyPhone()
my_phone.IMEI = 1145141919810
my_phone.producer = 'hanser'

print(f"IMEI={my_phone.IMEI}\nproducer={my_phone.producer}\nNFC_version={my_phone.NFC_read_version()}")








