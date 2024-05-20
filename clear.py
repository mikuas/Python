# 清除重复元素

class RepeatDataClear:

    def __init__(self, file_path, save_path):
        # reception file incoming path | save path
        self.file_path = file_path
        self.save_path = save_path

    def file_read(self) -> list:

        try:
            file = open(self.file_path, 'r', encoding='utf-8')

            element = file.readlines()

            try:
                if '\n' not in element[-1]:
                    element[-1] += '\n'

                return element
            except Exception as a:
                print(a)

        except Exception as a:
            print(f'文件不存在:{a}')

    @staticmethod
    def clear_repeat(data) -> set:

        try:
            data = set(data)
            data.remove('\n')
            data = list(data)

            return data
            # for line in data:
            #     if line == '\n':
            #         del data[data.index(line)]
            # return set(data)
        except Exception as a:
            print(f'传入的文件为空:{a}')

    def file_write(self, data):
        if data == '':
            pass
        else:
            file = open(self.save_path, 'w', encoding='utf-8')
            try:
                for i in data:
                    file.write(i)
                print('执行完毕')
            except Exception as a:
                print(a)


if __name__ == '__main__':

    clear = RepeatDataClear('C:/passwd.txt', 'C:/test.txt')
    clear.file_write(clear.clear_repeat(clear.file_read()))



