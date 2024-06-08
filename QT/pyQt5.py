from PySide6.QtWidgets import *
import tkinter as tk
from tkinter import filedialog


class RepeatDataClear:

    def __init__(self, file_path, save_path):
        # reception file incoming path | save path
        self.file_path = file_path
        self.save_path = save_path

    def open_file(self):
        root = tk.Tk()
        root.withdraw()  # 隐藏主窗口

        # 让用户选择文件
        self.file_path = filedialog.askopenfilename(
            title="打开文件",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]  # 文件类型过滤器
        )
        root.destroy()  # 销毁主窗口

    def save_file(self):
        root = tk.Tk()
        root.withdraw()  # 隐藏主窗口

        # 让用户选择保存文件的路径
        self.file_path = filedialog.asksaveasfilename(
            title="保存文件",
            defaultextension=".txt",  # 默认扩展名
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]  # 文件类型过滤器
        )
        root.destroy()  # 销毁主窗口

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
    def clear_repeat(data) -> list:

        try:
            data = set(data)
            data.remove('\n')
            return list(data)
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

    def __init__(self, apptitle='RepeatDataClear', win_width=500, win_height=200):
        # 创建主窗口对象
        self.window = QMainWindow()
        # 设置窗口的大小
        self.window.resize(win_width, win_height)
        # 设置窗口显示的位置
        self.window.move(600, 400)
        # 设置窗口的标题
        self.window.setWindowTitle(apptitle)

        self.win_width = win_width
        self.win_height = win_height
        self.rError = QMessageBox(self.window)
        self.wError = QMessageBox(self.window)

        self.file_path = None
        self.save_path = None

        self.box = QMessageBox(self.window)
        self.info = QMessageBox(self.window)

        # 设置按钮
        self.button = QPushButton('执行', self.window)
        self.button.move(win_width * 0.6, win_height * 0.3)
        # set button size
        self.button.setFixedSize(100, 50)

        self.file_read_button = QPushButton('选择读取的文件', self.window)
        self.file_read_button.move(20, 20)
        self.file_read_button.setFixedSize(150, 50)

        self.file_save_button = QPushButton('选择保存路径', self.window)
        self.file_save_button.move(20, 100)
        self.file_save_button.setFixedSize(150, 50)
        # 按钮点击事件
        self.button.clicked.connect(self.handeCale)

        self.file_read_button.clicked.connect(self.open_file)
        self.file_save_button.clicked.connect(self.save_file)

    def handeCale(self):

        try:
            repeat = RepeatDataClear(self.file_path, self.save_path)
            repeat.file_write(repeat.clear_repeat(repeat.file_read()))
            self.info.show()
            self.info.setInformativeText('执行完毕!')
            self.info.move(self.win_width + 300, self.win_height + 250)

            if self.file_path is None:
                self.rError.resize(100, 100)
                self.rError.setInformativeText('文件不存在！')
                self.rError.move(350, 350)
                # self.window_two.resize(100, 100)
                # self.text.setPlainText('文件不存在')
                # self.window_two.move(350, 350)

            if self.save_path is None:
                self.wError.resize(100, 100)
                self.wError.setInformativeText('文件不存在！')
                self.wError.move(350, 350)
        except Exception:
            if not self.file_path:
                self.rError.show()
                self.rError.resize(self.win_width * 0.5, self.win_height * 0.5)
                self.rError.move(self.win_width + 200, self.win_height + 200)
                self.rError.setInformativeText('请选择文件!')
            elif not self.save_path:
                self.wError.show()
                self.wError.resize(self.win_width * 0.5, self.win_height * 0.5)
                self.wError.move(self.win_width + 200, self.win_height + 200)
                self.wError.setInformativeText('请选择保存路径!')
            pass

    def open_file(self):
        root = tk.Tk()
        root.withdraw()  # 隐藏主窗口
        # 让用户选择文件
        self.file_path = filedialog.askopenfilename(
            title="打开文件",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]  # 文件类型过滤器
        )
        root.destroy()  # 销毁主窗口

    def save_file(self):
        root = tk.Tk()
        root.withdraw()  # 隐藏主窗口

        # 让用户选择保存文件的路径
        self.save_path = filedialog.asksaveasfilename(
            title="保存文件",
            defaultextension=".txt",  # 默认扩展名
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]  # 文件类型过滤器
        )
        root.destroy()  # 销毁主窗口

    def information(self):
        self.box.show()
        self.box.setInformativeText('这是一个可以清理重复元素的软件,接收一个传入文件,清除每一行相同的元素')
        self.box.setWindowTitle('Information')
        self.box.move(self.win_width + 200, self.win_height + 250)


if __name__ == '__main__':
    app = QApplication([])
    stats = Stats()
    stats.information()
    stats.window.show()
    app.exec()


