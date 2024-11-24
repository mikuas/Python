
from record import Record
import json


class FileReader:

    def file_read(self) -> list[Record]:
        """
        读取文件的内容，读到的每一条数据都转换为Record对象，将他们封装到list内返回
        :return: None
        """
        pass


class TextFileReader(FileReader):

    def __init__(self, path):       # 定义成员变量，记录文件路径
        self.path = path

    # 复写(实现抽象方法)父类的方法
    def file_read(self) -> list[Record]:

        file_r = open(self.path, 'r', encoding='UTF-8')

        record_list: list[Record] = []
        for line in file_r.readlines():
            line_list = line.strip()         # 消除每一行的\n
            record = Record(line_list.split(',')[0], line_list.split(',')[1],
                            line_list.split(',')[2], line_list.split(',')[3])
            record_list.append(record)
        file_r.close()
        # print(type(record_list))
        return record_list


class JsonFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    # 复写(实现抽象方法)父类的方法
    def file_read(self) -> list[Record]:

        file_r = open(self.path, 'r', encoding='UTF-8')

        record_list: list[Record] = []
        for line in file_r:

            line = json.loads(line)
            record = Record(line['date'], line['order_id'], line['money'], line['province'])
            record_list.append(record)
        file_r.close()
        return record_list


if __name__ == '__main__':
    list1 = TextFileReader('C:/2011年1月销售数据.txt').file_read()

    list2 = JsonFileReader("C:/2011年2月销售数据JSON.txt").file_read()

    for i in list1:
        print(i)

    for i in list2:
        print(i)



