from PySide6.QtWidgets import *


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
            data = list(data)

            for line in data:
                if line == '\n':
                    del data[data.index(line)]
            return set(data)
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


class Stats:

    def __init__(self, win_width, win_height, apptitle, text_width, text_height):
        # 创建主窗口对象
        self.window = QMainWindow()
        self.window_two = QMainWindow()
        # 设置窗口的大小
        self.window.resize(win_width, win_height)
        # 设置窗口显示的位置
        self.window.move(300, 300)
        # 设置窗口的标题
        self.window.setWindowTitle(apptitle)

        # 设置文本控件
        self.file_path = QPlainTextEdit(self.window)
        # 设置提示内容
        self.file_path.setPlaceholderText('请输入要处理的文件路径')
        # 设置文本控件位置
        self.file_path.move(10, 10)
        # 处理文件文本控件大小
        self.file_path.resize(text_width, text_height)

        self.text = QPlainTextEdit(self.window_two)
        self.text.resize(100, 100)

        # 保存文件文本控件大小
        self.save_path = QPlainTextEdit(self.window)
        self.save_path.setPlaceholderText('请输入保存路径')
        self.save_path.move(10, 110)
        self.save_path.resize(text_width, text_height)

        # 设置按钮
        self.button = QPushButton('执行', self.window)
        self.button.move(text_width + 20, text_height / 3 + text_height)

        # 按钮点击事件
        self.button.clicked.connect(self.handeCale)

    def handeCale(self):

        # 获取文本控件内容
        files_path = self.file_path.toPlainText()
        saves_path = self.save_path.toPlainText()
        try:
            repeat = RepeatDataClear(files_path, saves_path)
            repeat.file_write(repeat.clear_repeat(repeat.file_read()))
        except Exception:
            self.window_two.show()
            self.window_two.resize(100, 100)
            self.window_two.move(350, 350)
            self.text.setPlainText('文件不存在')
            pass


if __name__ == '__main__':
    app = QApplication([])
    stats = Stats(500, 500, 'RepeatDataClear', 200, 50)
    stats.window.show()
    app.exec()
